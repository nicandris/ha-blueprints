"""Validate each blueprint with Home Assistant's own blueprint and automation schemas.

Usage: python validate_blueprints.py automation/*.yaml
Required inputs get a placeholder of the selector's type; defaults are used for the rest.
"""

import asyncio
import sys
import tempfile

from homeassistant import loader
from homeassistant.components.automation.config import _async_validate_config_item
from homeassistant.components.blueprint import models, schemas
from homeassistant.core import HomeAssistant
from homeassistant.helpers import condition, trigger
from homeassistant.util import yaml as yaml_util

PLACEHOLDERS = {
    "entity": lambda cfg: "{}.placeholder".format(_domain(cfg)),
    "number": lambda cfg: cfg.get("min", 1),
    "text": lambda cfg: "placeholder",
    "select": lambda cfg: [] if cfg.get("multiple") else "placeholder",
}


def _domain(cfg):
    domain = (cfg or {}).get("domain", "sensor")
    return domain[0] if isinstance(domain, list) else domain


def _placeholder(spec):
    (kind, cfg), = spec["selector"].items()
    value = PLACEHOLDERS[kind](cfg or {})
    if kind == "entity" and (cfg or {}).get("multiple"):
        value = [value]
    return value


async def main(paths):
    with tempfile.TemporaryDirectory() as config_dir:
        hass = HomeAssistant(config_dir)
        loader.async_setup(hass)
        await condition.async_setup(hass)
        await trigger.async_setup(hass)
        failed = False
        for path in paths:
            try:
                blueprint = models.Blueprint(
                    yaml_util.load_yaml(path), path=path,
                    expected_domain="automation", schema=schemas.BLUEPRINT_SCHEMA,
                )
                inputs = {
                    key: _placeholder(spec)
                    for key, spec in blueprint.inputs.items()
                    if "default" not in (spec or {})
                }
                config = models.BlueprintInputs(
                    blueprint, {"use_blueprint": {"path": path, "input": inputs}}
                ).async_substitute()
                await _async_validate_config_item(hass, config, True, False)
                print(f"OK   {path}")
            except Exception as err:  # noqa: BLE001 - report every failure
                failed = True
                print(f"FAIL {path}: {err!r}")
        await hass.async_stop(force=True)
        return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main(sys.argv[1:])))
