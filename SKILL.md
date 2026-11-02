---
name: genpark-personal-agent-circadian-ocular-lux-luxmeter-entrainment-skill
version: "1.0.0"
description: "Zero-dependency CIE S 026 melanopic equivalent daylight illuminance (melanopic EDI) quantifier, intrinsically photosensitive retinal ganglion cell (ipRGC) modeler, and solar zeitgeber scheduler."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Circadian Ocular Luxmeter Entrainment Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI health companions to model circadian photobiology, calculate Melanopic Equivalent Daylight Illuminance (melanopic EDI in lux) according to the CIE S 026 standard, quantify intrinsically photosensitive retinal ganglion cell (ipRGC) melanopsin activation, determine Phase Response Curve (PRC) phase advances and delays, and schedule 24-hour solar zeitgeber protocols.

## Agent In-Context Capabilities

- **Melanopic EDI Calculation**: Converts standard photopic lux across diverse spectral light sources (sunlight, overcast sky, cool white LED, sRGB monitor, warm LED) into true melanopsin-activating illuminance.
- **Phase Response Curve (PRC) Modeling**: Accurately projects circadian clock phase advances (morning photon pulse) and phase delays (evening blue light contamination).
- **International Photobiology Standards**: Enforces international consensus thresholds ($\ge 1000$ melanopic EDI for morning reset, $\ge 250$ for daytime alertness, $< 10$ for pre-sleep melatonin protection).

## Tools Summary

1. `calculate_melanopic_edi_and_circadian_drive`: Computes melanopic EDI, photon dose, and projected phase shift trajectory in hours.
2. `prescribe_daily_solar_zeitgeber_schedule`: Schedules morning, daytime, dusk, and evening photobiological milestones.
