"""Vilnius Air Quality sensors."""
from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, CONF_SENSOR_INDEX

# All possible sensors with their display names and units
ALL_SENSORS = {
    "pm1": ("PM1", "µg/m³", "mdi:blur"),
    "pm2_5": ("PM2.5", "µg/m³", "mdi:blur"),
    "pm10": ("PM10", "µg/m³", "mdi:blur"),
    "so2_ug_m3": ("SO2", "µg/m³", "mdi:molecule"),
    "co_mg_m3": ("CO", "mg/m³", "mdi:molecule-co"),
    "voc": ("VOC", "ppb", "mdi:air-filter"),
    "nh3_ug_m3": ("NH3", "µg/m³", "mdi:molecule"),
    "no2_ug_m3": ("NO2", "µg/m³", "mdi:molecule"),
    "no_ug_m3": ("NO", "µg/m³", "mdi:molecule"),
    "o3_ug_m3": ("O3", "µg/m³", "mdi:molecule"),
}


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up Vilnius Air Quality sensors."""
    from .coordinator import VilniusAirCoordinator

    sensor_index = entry.data[CONF_SENSOR_INDEX]
    coordinator = VilniusAirCoordinator(hass, sensor_index)

    await coordinator.async_config_entry_first_refresh()

    # Create sensors for all fields that exist in the API response
    # (even if they're None initially, they might have data later)
    entities = []
    if coordinator.data:
        for key, (name, unit, icon) in ALL_SENSORS.items():
            # Create sensor if the key exists in the response (even if value is None)
            if key in coordinator.data:
                entities.append(
                    VilniusAirSensor(coordinator, entry.entry_id, sensor_index, key, name, unit, icon)
                )
    
    async_add_entities(entities)


class VilniusAirSensor(CoordinatorEntity, SensorEntity):
    """Vilnius Air Quality sensor."""

    def __init__(self, coordinator, entry_id, sensor_index, key, name, unit, icon):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._key = key
        self._sensor_index = sensor_index
        self._attr_name = f"Vilnius Air {sensor_index} {name}"
        self._attr_native_unit_of_measurement = unit
        self._attr_unique_id = f"{entry_id}_{key}"
        self._attr_state_class = SensorStateClass.MEASUREMENT
        self._attr_icon = icon
        # Set a custom entity_id suggestion that includes sensor index
        self.entity_id = f"sensor.vilnius_air_{sensor_index}_{key}"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry_id)},
            "name": f"Vilnius Air Sensor {sensor_index}",
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

