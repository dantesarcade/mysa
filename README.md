# Mysa Thermostat for Home Assistant

This is a custom Home Assistant integration that enables direct cloud control of your Mysa smart thermostats. Designed to be installed through [HACS (Home Assistant Community Store)](https://hacs.xyz/), it eliminates the need for MQTT or Docker and works entirely through the Mysa cloud API.

## 🚀 Features
- Full Home Assistant UI-based setup (no YAML required)
- Supports setting target temperature and HVAC mode
- Secure cloud authentication using AWS Cognito
- Easily extendable for service calls and automation

## 📁 Directory Structure
```
custom_components/
└── mysa/
    ├── __init__.py            # Entry point for the integration
    ├── climate.py             # Home Assistant climate platform implementation
    ├── config_flow.py         # UI-based configuration flow
    ├── const.py               # Shared constants
    ├── manifest.json          # Integration metadata and dependencies
    ├── mysa_api.py            # API wrapper for cloud communication
    ├── services.yaml          # (Optional) future Home Assistant service support
    └── translations/
        └── en.json            # English translations for UI
```

## 🧠 Requirements
- Home Assistant 2023.5 or later
- A valid Mysa account (email + password)
- Installed via HACS or manually placed in the `custom_components/` directory

## 📦 Installation via HACS
1. Open Home Assistant → HACS → Integrations
2. Click the 3-dot menu in the top-right → **Custom repositories**
3. Add: `https://github.com/dantesarcade/mysa` with type `Integration`
4. Find **Mysa Thermostat** in the list and install
5. Reboot Home Assistant

## 🔧 Configuration
1. Go to **Settings → Devices & Services → Add Integration**
2. Search for "Mysa Thermostat"
3. Enter your Mysa **email** and **password** when prompted
4. Devices will be auto-discovered and added

No YAML configuration needed!

## 🔐 Authentication
This integration uses AWS Cognito to securely authenticate against the Mysa cloud API. Credentials are stored safely in Home Assistant's encrypted storage.

## 🛠 Services (Planned)
The file `services.yaml` is scaffolded to support future features such as:
- Manual temperature override
- Energy usage reporting

## 🌐 Translations
Includes localization support in English for all setup screens and device states.

## 👷 Development Notes
If you want to contribute:
```bash
git clone https://github.com/dantesarcade/mysa.git
cd mysa
```
Then copy the contents into your `config/custom_components/mysa/` folder in Home Assistant.

## 📄 License
MIT License © 2025 dantesarcade

---
Want more features like MQTT fallback or zone grouping? Open an issue or pull request!

---

# Original Source Code & Scaffold Overview Below
### HACS Integration for Mysa Thermostats

# Directory structure:
```
# custom_components/
# └── mysa/
#     ├── __init__.py
#     ├── climate.py
#     ├── config_flow.py
#     ├── const.py
#     ├── manifest.json
#     ├── mysa_api.py
#     ├── services.yaml
#     └── translations/
#         └── en.json
```
# Basic scaffold and module outline below:

# const.py
```
DOMAIN = "mysa"
PLATFORMS = ["climate"]
CONF_EMAIL = "email"
CONF_PASSWORD = "password"
```

# manifest.json
```
manifest = {
    "domain": "mysa",
    "name": "Mysa Thermostat",
    "version": "0.1.0",
    "documentation": "https://github.com/dantesarcade/mysa",
    "dependencies": [],
    "codeowners": ["@dantesarcade"],
    "requirements": [
        "aiohttp>=3.9.0",
        "pycognito>=2023.5.0"
    ],
    "config_flow": True
}
```
# services.yaml
```
# Placeholder for future service call definitions

# Example:
# set_temperature:
#   description: "Set the target temperature manually."
#   fields:
#     entity_id:
#       description: "Target climate entity."
#       example: "climate.mysa_living_room"
#       required: true
#       selector:
#         entity:
#           domain: climate
#     temperature:
#       description: "New target temperature in Celsius."
#       example: 22.5
#       required: true
#       selector:
#         number:
#           min: 5
#           max: 35
```

# translations/en.json
```
# UI strings for Home Assistant frontend
translations = {
  "config": {
    "step": {
      "user": {
        "title": "Mysa Thermostat Setup",
        "description": "Enter your Mysa credentials to connect."
      }
    },
    "error": {
      "cannot_connect": "Cannot connect to Mysa API.",
      "invalid_auth": "Invalid email or password."
    },
    "abort": {
      "already_configured": "Mysa thermostat is already configured."
    }
  },
  "entity": {
    "climate": {
      "mysa": {
        "name": "Mysa Thermostat",
        "state": {
          "heat": "Heating",
          "off": "Off"
        }
      }
    }
  }
}
```