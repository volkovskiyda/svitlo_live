from __future__ import annotations
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.config_entries import ConfigEntry
from .const import DOMAIN


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
coord = hass.data[DOMAIN][entry.entry_id]["coordinator"]
async_add_entities([SvitloOffNow(coord)])


class SvitloOffNow(CoordinatorEntity, BinarySensorEntity):
_attr_has_entity_name = True
_attr_name = "Svitlo Off Now"


@property
def is_on(self) -> bool:
d = self.coordinator.data or {}
return (d.get("next") or {}).get("status") == "off_now"


@property
def extra_state_attributes(self):
d = self.coordinator.data or {}
return {
"updated_at": d.get("updated_at"),
"address": d.get("address"),
"gpv": d.get("gpv"),
"today": d.get("today")
}
