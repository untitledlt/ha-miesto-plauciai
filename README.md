# Vilnius Air Quality - Home Assistant Custom Component

A Home Assistant custom component that fetches air pollution sensor data from Vilnius city's air quality monitoring network at [miestoplauciai.vilnius.lt/orotarsa](https://miestoplauciai.vilnius.lt/orotarsa).

## Overview

This custom component integrates Vilnius city air quality sensors into Home Assistant, providing real-time particulate matter (PM) measurements from selected monitoring stations across the city.

## Features

- Fetches air pollution data from Vilnius city's official air quality monitoring API
- Supports selection of specific air quality sensor stations by sensor ID
- Provides three sensor entities measuring different particulate matter sizes:
  - **PM1** - Particulate matter ≤ 1.0 μm
  - **PM2.5** - Particulate matter ≤ 2.5 μm  
  - **PM10** - Particulate matter ≤ 10 μm
- Automatic updates every hour
- Cloud polling integration with Vilnius OpenCity API

## Installation

### Manual Installation

1. Copy the `custom_components/vilnius_air` directory to your Home Assistant's `custom_components` folder
2. Restart Home Assistant
3. Go to **Settings** → **Devices & Services** → **Add Integration**
4. Search for "Vilnius Air Quality"
5. Enter the sensor index for your chosen monitoring station

### HACS Installation

_(Not yet available in HACS default repositories)_

## Configuration

The integration is configured through the Home Assistant UI:

1. Navigate to **Settings** → **Devices & Services**
2. Click **Add Integration**
3. Search for "Vilnius Air Quality"
4. Enter the **sensor_index** for your preferred air quality monitoring station

### Finding Sensor Index

To find the sensor index for a specific monitoring station:

1. Visit [miestoplauciai.vilnius.lt/orotarsa](https://miestoplauciai.vilnius.lt/orotarsa)
2. Select a sensor location on the map
3. Note the sensor index/ID for that location
4. Use this ID during integration setup

## Sensors

Once configured, the integration creates three sensor entities:

| Sensor | Description | Unit |
|--------|-------------|------|
| `sensor.vilnius_pm1` | PM1 particulate matter concentration | µg/m³ |
| `sensor.vilnius_pm2_5` | PM2.5 particulate matter concentration | µg/m³ |
| `sensor.vilnius_pm10` | PM10 particulate matter concentration | µg/m³ |

## Data Source

Data is fetched from the Vilnius OpenCity API:
```
https://opencity.idvilnius.lt/atviras/rest/services/Aplinka/Oro_tarsa/MapServer/4/query
```

The component queries the API every hour to retrieve the latest air quality measurements from your selected monitoring station.

## Health Guidelines

### PM2.5 Air Quality Index (WHO Guidelines)

- **0-10 µg/m³** - Good
- **10-25 µg/m³** - Moderate  
- **25-50 µg/m³** - Unhealthy for sensitive groups
- **50-75 µg/m³** - Unhealthy
- **75+ µg/m³** - Very unhealthy

### PM10 Air Quality Index (WHO Guidelines)

- **0-20 µg/m³** - Good
- **20-50 µg/m³** - Moderate
- **50-100 µg/m³** - Unhealthy for sensitive groups
- **100-200 µg/m³** - Unhealthy
- **200+ µg/m³** - Very unhealthy

## Use in Automations

Example automation to send notification when air quality is poor:

```yaml
automation:
  - alias: "Alert on Poor Air Quality"
    trigger:
      - platform: numeric_state
        entity_id: sensor.vilnius_pm2_5
        above: 50
    action:
      - service: notify.mobile_app
        data:
          title: "Poor Air Quality Alert"
          message: "PM2.5 levels are unhealthy. Consider staying indoors."
```

## Troubleshooting

### Integration not loading
- Ensure the custom component folder is correctly placed in `config/custom_components/vilnius_air`
- Check Home Assistant logs for any error messages
- Verify your sensor_index is valid

### No data available
- Verify the sensor_index corresponds to an active monitoring station
- Check if the Vilnius OpenCity API is accessible
- The API may occasionally be down for maintenance

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is provided as-is for community use.

## Credits

- Air quality data provided by Vilnius City Municipality
- Data source: [miestoplauciai.vilnius.lt](https://miestoplauciai.vilnius.lt/orotarsa)
