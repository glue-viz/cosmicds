import requests

from echo import CallbackProperty
from glue.config import viewer_tool
from glue.viewers.common.tool import Tool

from cosmicds.utils import API_URL
from cosmicds.stories.hubbles_law.utils import HUBBLE_ROUTE_PATH

@viewer_tool
class SpectrumFlagTool(Tool):

    tool_id = "hubble:specflag"
    action_text = "Flag a spectrum as bad"
    tool_tip = "Flag a spectrum as bad"
    mdi_icon = "mdi-flag"

    flagged = CallbackProperty(False)

    def activate(self):
        data = { "galaxy_name": self.viewer.spectrum_name }
        requests.post(f"{API_URL}/{HUBBLE_ROUTE_PATH}/mark-spectrum-bad", json=data)
        self.flagged = True

