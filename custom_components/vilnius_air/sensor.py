"""Vilnius Air Quality sensors."""
from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, CONF_SENSOR_INDEX

SENSORS = {
    "pm1": ("PM1", "µg/m³"),
    "pm2_5": ("PM2.5", "µg/m³"),
    "pm10": ("PM10", "µg/m³"),
}


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up Vilnius Air Quality sensors."""
    from .coordinator import VilniusAirCoordinator

    coordinator = VilniusAirCoordinator(
        hass,
        entry.data[CONF_SENSOR_INDEX],
    )

    await coordinator.async_config_entry_first_refresh()

    async_add_entities(
        VilniusAirSensor(coordinator, entry.entry_id, key, name, unit)
        for key, (name, unit) in SENSORS.items()
    )


class VilniusAirSensor(CoordinatorEntity, SensorEntity):
    """Vilnius Air Quality sensor."""

    def __init__(self, coordinator, entry_id, key, name, unit):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._key = key
        self._attr_name = f"Vilnius {name}"
        self._attr_native_unit_of_measurement = unit
        self._attr_unique_id = f"{entry_id}_{key}"
        self._attr_state_class = SensorStateClass.MEASUREMENT
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry_id)},
            "name": f"Vilnius Air Sensor {coordinator.sensor_index}",
            "manufacturer": "Vilnius City",
            "model": "Air Quality Monitor",
        }

    @property
    def native_value(self):
        """Return the state of the sensor."""
        if self.coordinator.data:
            return self.coordinator.data.get(self._key)
        return None

    @property
    def available(self):
        """Return if entity is available."""
        return self.coordinator.last_update_success and self.coordinator.data is not None

