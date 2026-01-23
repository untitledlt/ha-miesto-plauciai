from datetime import timedelta
import aiohttp

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN

URL = (
    "https://opencity.idvilnius.lt/atviras/rest/services/"
    "Aplinka/Oro_tarsa/MapServer/4/query"
)

class VilniusAirCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, sensor_index):
        self.sensor_index = sensor_index
        super().__init__(
            hass,
            logger=None,
            name=DOMAIN,
            update_interval=timedelta(hours=1),
        )

    async def _async_update_data(self):
        params = {
            "where": f"1=1 AND sensor_index={self.sensor_index}",
            "outFields": "last_seen,pm1,pm2_5,pm10",
            "orderByFields": "last_seen DESC",
            "resultRecordCount": 1,
            "returnGeometry": "false",
            "f": "json",
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(URL, params=params) as resp:
                if resp.status != 200:
                    raise UpdateFailed("Failed to fetch data")
                data = await resp.json()

        try:
            return data["features"][0]["attributes"]
        except (KeyError, IndexError):
            raise UpdateFailed("No data returned")
