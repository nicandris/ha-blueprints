# ha-blueprints

Home Assistant blueprints by nicandris. The Aqara H2 blueprints are based on
[Jonybat's](https://gist.github.com/Jonybat) gists.

| Blueprint | Import |
|---|---|
| [UPS battery test](automation/ups_battery_test.yaml) — monthly cut of UPS mains via a smart plug, with aborts, failsafes and notifications | [![Import](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fnicandris%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fups_battery_test.yaml) |
| [Sensor threshold alert](automation/sensor_threshold_alert.yaml) — any sensor above/below its threshold for a while, per-sensor overrides, optional spoken + AI announcement | [![Import](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fnicandris%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fsensor_threshold_alert.yaml) |
| [Appliance alert](automation/appliance_alert.yaml) — alert while an entity is in a problem state (bucket full, salt low), auto-clear when it leaves, optional spoken + sanity-checked AI line | [![Import](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fnicandris%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Fappliance_alert.yaml) |
| [Aqara H2 EU Double rocker (WS-K08E)](automation/aqara_ws-k08e_event_entity.yaml) — Zigbee2MQTT event entity → single/double/hold/release actions per button. Cloned from [Jonybat's gist](https://gist.github.com/Jonybat/729e534537fa8903b1269ef722ca2999), modernised syntax, no helper entities needed | [![Import](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fnicandris%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Faqara_ws-k08e_event_entity.yaml) |
| [Aqara H2 EU Single rocker (WS-K07E)](automation/aqara_ws-k07e_event_entity.yaml) — same for the single rocker. Cloned from [Jonybat's gist](https://gist.github.com/Jonybat/f93cbff0be1733f37e5ac5b95f8c10c7), modernised syntax, no helper entities needed | [![Import](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fnicandris%2Fha-blueprints%2Fblob%2Fmain%2Fautomation%2Faqara_ws-k07e_event_entity.yaml) |

## Requirements

| Blueprint | Home Assistant | Needs |
|---|---|---|
| UPS battery test | 2024.10+ | A switch feeding the UPS mains; UPS battery, load and runtime sensors plus an online binary sensor or status sensor (e.g. the [NUT](https://www.home-assistant.io/integrations/nut/) integration) |
| Sensor threshold alert | 2026.10+ | Optional: [Music Assistant](https://www.home-assistant.io/integrations/music_assistant/) player and a TTS engine for announcements; an [AI Task](https://www.home-assistant.io/integrations/ai_task/) entity for AI lines |
| Appliance alert | 2026.10+ | Same optional announcement and AI Task pieces as above |
| Aqara H2 double / single rocker | 2024.10+ | [Zigbee2MQTT](https://www.zigbee2mqtt.io/) with the switch's `action` event entity (MQTT integration) |

## Validation

CI runs `yamllint --strict .` and loads every blueprint with Home Assistant's own
blueprint and automation schemas (`.github/scripts/validate_blueprints.py`).
