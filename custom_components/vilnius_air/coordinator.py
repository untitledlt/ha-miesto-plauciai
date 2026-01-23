"""Vilnius Air Quality data coordinator."""
from datetime import timedelta
import logging
import aiohttp

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

URL = (
    "https://opencity.idvilnius.lt/atviras/rest/services/"
    "Aplinka/Oro_tarsa/MapServer/4/query"
)


class VilniusAirCoordinator(DataUpdateCoordinator):
    """Vilnius Air Quality data update coordinator."""

    def __init__(self, hass, sensor_index):
        """Initialize the coordinator."""
        self.sensor_index = sensor_index
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(hours=1),
        )

    async def _async_update_data(self):
        """Fetch data from API."""
        params = {
            "where": f"1=1 AND sensor_index={self.sensor_index}",
            "outFields": "last_seen,pm1,pm2_5,pm10,so2_ug_m3,co_mg_m3,voc,nh3_ug_m3,no2_ug_m3,no_ug_m3,o3_ug_m3",
            "orderByFields": "last_seen DESC",
            "resultRecordCount": 1,
            "returnGeometry": "false",
            "f": "json",
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(URL, params=params) as resp:
                    if resp.status != 200:
                        raise UpdateFailed(f"Failed to fetch data: HTTP {resp.status}")
                    data = await resp.json()

            if not data.get("features"):
                raise UpdateFailed(f"No data returned for sensor_index {self.sensor_index}")
            
            attributes = data["features"][0]["attributes"]
            _LOGGER.debug("Fetched data: %s", attributes)
            return attributes
        except aiohttp.ClientError as err:
            raise UpdateFailed(f"Error communicating with API: {err}") from err
        except (KeyError, IndexError) as err:
            raise UpdateFailed(f"Invalid data format: {err}") from err

