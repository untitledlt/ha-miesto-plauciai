# Vilnius Air Quality - Home Assistant Custom Component

<p align="center">
  <img src="https://raw.githubusercontent.com/untitledlt/ha-miesto-plauciai/main/logo.png" alt="Vilnius Air Quality Logo" width="200">
</p>

[![GitHub Release](https://img.shields.io/github/v/release/untitledlt/ha-miesto-plauciai)](https://github.com/untitledlt/ha-miesto-plauciai/releases)
[![GitHub](https://img.shields.io/github/license/untitledlt/ha-miesto-plauciai)](https://github.com/untitledlt/ha-miesto-plauciai/blob/main/LICENSE)
[![Validate](https://github.com/untitledlt/ha-miesto-plauciai/actions/workflows/validate.yml/badge.svg)](https://github.com/untitledlt/ha-miesto-plauciai/actions/workflows/validate.yml)

A Home Assistant custom component that fetches air pollution sensor data from Vilnius city's air quality monitoring network at [miestoplauciai.vilnius.lt/orotarsa](https://miestoplauciai.vilnius.lt/orotarsa).

## Overview

This custom component integrates Vilnius city air quality sensors into Home Assistant, providing real-time particulate matter (PM) measurements from selected monitoring stations across the city.

## Features

- Fetches air pollution data from Vilnius city's official air quality monitoring API
- Supports selection of specific air quality sensor stations by sensor ID
- **Automatically detects and creates sensors for all available pollutants** at the selected station
- Measures various air quality parameters including:
  - Particulate matter (PM1, PM2.5, PM10)
  - Sulfur dioxide (SO2)
  - Carbon monoxide (CO)
  - Volatile organic compounds (VOC)
  - Ammonia (NH3)
  - Nitrogen oxides (NO2, NO)
  - Ozone (O3)
- Automatic updates every hour
- Cloud polling integration with Vilnius OpenCity API
- **Supports multiple sensor stations** - add the integration multiple times with different sensor IDs

## Installation

### Method 1: HACS Installation (Recommended)

1. Make sure you have [HACS](https://hacs.xyz/) installed in your Home Assistant instance
2. Open HACS in your Home Assistant instance
3. Click on **Integrations**
4. Click the **three dots** in the top right corner
5. Select **Custom repositories**
6. Add the repository URL: `https://github.com/untitledlt/ha-miesto-plauciai`
7. Select category: **Integration**
8. Click **Add**
9. Find "Vilnius Air Quality" in HACS and click **Download**
10. Restart Home Assistant
11. Go to **Settings** → **Devices & Services** → **Add Integration**
12. Search for "Vilnius Air Quality"
13. Enter the sensor index for your chosen monitoring station

### Method 2: Manual Download

1. Download the [latest release](https://github.com/untitledlt/ha-miesto-plauciai/releases) from GitHub
2. Extract the archive
3. Copy the `custom_components/vilnius_air` directory to your Home Assistant's `custom_components` folder
4. Restart Home Assistant
5. Go to **Settings** → **Devices & Services** → **Add Integration**
6. Search for "Vilnius Air Quality"
7. Enter the sensor index for your chosen monitoring station

### Method 3: Git Clone

1. Navigate to your Home Assistant configuration directory (where `configuration.yaml` is located)
2. If you don't have a `custom_components` directory, create it:
   ```bash
   mkdir custom_components
   cd custom_components
   ```
3. Clone this repository:
   ```bash
   git clone https://github.com/untitledlt/ha-miesto-plauciai.git
   cd ha-miesto-plauciai
   ```
4. Copy the integration to your custom_components folder:
   ```bash
   cp -r custom_components/vilnius_air ../vilnius_air
   ```
5. Restart Home Assistant
6. Go to **Settings** → **Devices & Services** → **Add Integration**
7. Search for "Vilnius Air Quality"
8. Enter the sensor index for your chosen monitoring station

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

#### Available Sensors

| Sensor Index | Name | Latitude | Longitude |
|--------------|------|----------|-----------|
| 87539 | Zujūnai | 54.72728 | 25.169634 |
| 97695 | Vilniaus Maironio progimnazija | 54.71449 | 25.237741 |
| 91147 | Vinco Kudirkos aikštė | 54.68735 | 25.279945 |
| 92611 | Vilniaus Taikos progimnazija | 54.715042 | 25.21283 |
| 97681 | Vilniaus Joachimo Lelevelio inžinerijos gimnazija | 54.70567 | 25.29908 |
| 97687 | Vilniaus Aleksandro Puškino gimnazija | 54.731033 | 25.222054 |
| 97731 | Vilniaus kunigaikščio Gedimino progimnazija | 54.692867 | 25.266613 |
| 97893 | Vilniaus Baltupių progimnazija | 54.730103 | 25.272648 |
| 97903 | Vilniaus Lazdynų vidurinė mokykla | 54.675785 | 25.212624 |
| 97905 | Vilniaus Martyno Mažvydo progimnazija | 54.70702 | 25.180683 |
| 97749 | Grigiškių Šviesos gimnazija | 54.667286 | 25.098402 |
| 97915 | Vilniaus Žaliakalnio darželis-mokykla | 54.686897 | 25.412926 |
| 90315 | Vilniaus Sietuvos progimnazija | 54.72162 | 25.227186 |
| 97919 | Vilniaus Ryto progimnazija | 54.694225 | 25.210457 |
| 97957 | Vilniaus Jono Basanavičiaus progimnazija | 54.679886 | 25.255571 |
| 97959 | Vilniaus Prano Mašioto pradinė mokykla | 54.715786 | 25.307705 |
| 97963 | Vilniaus Naujininkų progimnazija | 54.660263 | 25.268192 |
| 97967 | Vilniaus Naujamiesčio mokykla | 54.67775 | 25.267 |
| 97969 | Vilniaus Gerosios Vilties progimnazija | 54.671345 | 25.251398 |
| 97973 | Vilniaus Antano Vienuolio progimnazija | 54.673107 | 25.28931 |
| 97977 | Vilniaus Antakalnio progimnazija | 54.701992 | 25.310047 |
| 97979 | Vilniaus lopšelis-darželis "Eglutė" | 54.70372 | 25.248451 |
| 98015 | Vilniaus Fabijoniškių gimnazija | 54.732414 | 25.240326 |
| 30366 | Vėtrungių / S. Neries g. 7 (2 sensorius) | 54.733122 | 25.237299 |
| 30416 | Vėtrungių / S. Neries g. 7 (1 sensorius) | 54.73299 | 25.236736 |

## Sensors

Once configured, the integration creates sensor entities for all available pollutants from your selected monitoring station. Different stations may provide different measurements:

### Common Sensors (Available on most stations)

| Sensor | Description | Unit |
|--------|-------------|------|
| PM1 | PM1 particulate matter concentration | µg/m³ |
| PM2.5 | PM2.5 particulate matter concentration | µg/m³ |
| PM10 | PM10 particulate matter concentration | µg/m³ |

### Additional Sensors (Available on some stations)

| Sensor | Description | Unit |
|--------|-------------|------|
| SO2 | Sulfur dioxide concentration | µg/m³ |
| CO | Carbon monoxide concentration | mg/m³ |
| VOC | Volatile organic compounds | ppb |
| NH3 | Ammonia concentration | µg/m³ |
| NO2 | Nitrogen dioxide concentration | µg/m³ |
| NO | Nitrogen monoxide concentration | µg/m³ |
| O3 | Ozone concentration | µg/m³ |

**Note:** The integration automatically creates sensors only for pollutants that are measured by your selected monitoring station. Entity names include the sensor ID (e.g., `sensor.vilnius_air_30416_pm2_5`) to support multiple sensor stations.

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

Contributions are welcome! Please feel free to submit issues or pull requests on the [GitHub repository](https://github.com/untitledlt/ha-miesto-plauciai).

## License

This project is provided as-is for community use.

## Credits

- Air quality data provided by Vilnius City Municipality
- Data source: [miestoplauciai.vilnius.lt](https://miestoplauciai.vilnius.lt/orotarsa)
