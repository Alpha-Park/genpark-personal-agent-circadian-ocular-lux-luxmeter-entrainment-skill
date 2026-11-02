# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Circadian Ocular Luxmeter Entrainment Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentCircadianOcularLuxLuxmeterEntrainment

mcp = FastMCP("PersonalAgentCircadianOcularLuxLuxmeterEntrainment")
client = PersonalAgentCircadianOcularLuxLuxmeterEntrainment()

@mcp.tool()
def calculate_melanopic_edi_and_circadian_drive(
    photopic_lux: float = 12000.0,
    light_source_spectrum: str = "direct_sunlight",
    exposure_duration_minutes: float = 25.0,
    time_since_waking_hours: float = 0.5
) -> str:
    """Calculates Melanopic Equivalent Daylight Illuminance (melanopic EDI), PRC phase shift, and SCN drive."""
    import json
    return json.dumps(client.calculate_melanopic_edi_and_circadian_drive(
        photopic_lux, light_source_spectrum, exposure_duration_minutes, time_since_waking_hours
    ), indent=2)

@mcp.tool()
def prescribe_daily_solar_zeitgeber_schedule(
    wake_time_24h: float = 6.5,
    planned_sleep_time_24h: float = 22.5
) -> str:
    """Schedules morning solar anchoring, daytime working illumination, and evening low-lux cutoffs."""
    import json
    return json.dumps(client.prescribe_daily_solar_zeitgeber_schedule(
        wake_time_24h, planned_sleep_time_24h
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
