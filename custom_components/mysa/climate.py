# Climate platform entity logic
import logging
from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import HVAC_MODE_HEAT, HVAC_MODE_OFF, SUPPORT_TARGET_TEMPERATURE
from homeassistant.const import TEMP_CELSIUS, ATTR_TEMPERATURE

from .const import DOMAIN
from .mysa_api import MysaAPI

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    data = hass.data[DOMAIN][config_entry.entry_id]
    api = MysaAPI(data["email"], data["password"])
    await api.login()
    devices = await api.get_devices()

    _LOGGER.debug("Devices returned from API: %s", devices)

    if not devices:
        _LOGGER.warning("No Mysa devices found.")
        return

    entities = [MysaThermostat(device) for device in devices]
    async_add_entities(entities)

class MysaThermostat(ClimateEntity):
    def __init__(self, device):
        self._device = device
        self._attr_name = device.get("name", "Mysa Thermostat")
        self._attr_unique_id = device.get("id")
        self._attr_temperature_unit = TEMP_CELSIUS
        self._attr_hvac_modes = [HVAC_MODE_HEAT, HVAC_MODE_OFF]
        self._attr_supported_features = SUPPORT_TARGET_TEMPERATURE
        self._attr_hvac_mode = HVAC_MODE_HEAT
        self._attr_current_temperature = device.get("roomTemp")
        self._attr_target_temperature = device.get("target")

    async def async_set_temperature(self, **kwargs):
        target = kwargs.get(ATTR_TEMPERATURE)
        if target:
            self._attr_target_temperature = target
            self.async_write_ha_state()

    async def async_set_hvac_mode(self, hvac_mode):
        self._attr_hvac_mode = hvac_mode
        self.async_write_ha_state()