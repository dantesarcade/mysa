# Config flow logic for UI setup
from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN, CONF_EMAIL, CONF_PASSWORD

class MysaConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for the Mysa integration."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title=user_input[CONF_EMAIL], data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_EMAIL): str,
                vol.Required(CONF_PASSWORD): str,
            })
        )
