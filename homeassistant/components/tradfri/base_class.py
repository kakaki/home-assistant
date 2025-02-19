"""Base class for IKEA TRADFRI."""
import logging

from pytradfri.error import PytradfriError

from homeassistant.core import callback
from homeassistant.helpers.entity import Entity
from . import DOMAIN as TRADFRI_DOMAIN

_LOGGER = logging.getLogger(__name__)


class TradfriBaseDevice(Entity):
    """Base class for a TRADFRI device."""

    def __init__(self, device, api, gateway_id):
        """Initialize a device."""
        self._available = True
        self._api = api
        self._device = None
        self._device_control = None
        self._device_data = None
        self._gateway_id = gateway_id
        self._name = None
        self._unique_id = None

        self._refresh(device)

    @callback
    def _async_start_observe(self, exc=None):
        """Start observation of device."""
        if exc:
            self._available = False
            self.async_schedule_update_ha_state()
            _LOGGER.warning("Observation failed for %s", self._name, exc_info=exc)

        try:
            cmd = self._device.observe(
                callback=self._observe_update,
                err_callback=self._async_start_observe,
                duration=0,
            )
            self.hass.async_create_task(self._api(cmd))
        except PytradfriError as err:
            _LOGGER.warning("Observation failed, trying again", exc_info=err)
            self._async_start_observe()

    async def async_added_to_hass(self):
        """Start thread when added to hass."""
        self._async_start_observe()

    @property
    def available(self):
        """Return True if entity is available."""
        return self._available

    @property
    def device_info(self):
        """Return the device info."""
        info = self._device.device_info

        return {
            "identifiers": {(TRADFRI_DOMAIN, self._device.id)},
            "name": self._name,
            "manufacturer": info.manufacturer,
            "model": info.model_number,
            "sw_version": info.firmware_version,
            "via_device": (TRADFRI_DOMAIN, self._gateway_id),
        }

    @property
    def name(self):
        """Return the display name of this device."""
        return self._name

    @property
    def should_poll(self):
        """No polling needed for tradfri device."""
        return False

    @property
    def unique_id(self):
        """Return unique ID for device."""
        return self._unique_id

    @callback
    def _observe_update(self, device):
        """Receive new state data for this device."""
        self._refresh(device)
        self.async_schedule_update_ha_state()

    def _refresh(self, device):
        """Refresh the device data."""
        self._device = device
        self._name = device.name
        self._available = device.reachable
