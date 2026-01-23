from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import EntityCategory

from .const import DOMAIN

SENSORS = {
    "pm1": ("PM1", "µg/m³"),
    "pm2_5": ("PM2.5", "µg/m³"),
    "pm10": ("PM10", "µg/m³"),
}

async def async_setup_entry(hass, entry, async_add_entities):
    from .coordinator import VilniusAirCoordinator

    coordinator = VilniusAirCoordinator(
        hass,
        entry.data["sensor_index"],
    )

    await coordinator.async_config_entry_first_refresh()

    async_add_entities(
        VilniusAirSensor(coordinator, key, name, unit)
        for key, (name, unit) in SENSORS.items()
    )

class VilniusAirSensor(SensorEntity):
    def __init__(self, coordinator, key, name, unit):
        self.coordinator = coordinator
        self._key = key
        self._attr_name = f"Vilnius {name}"
        self._attr_native_unit_of_measurement = unit
        self._attr_unique_id = f"vilnius_air_{key}"

    @property
    def native_value(self):
        return self.coordinator.data.get(self._key)

    async def async_update(self):
        await self.coordinator.async_request_refresh()
