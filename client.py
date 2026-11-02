# -*- coding: utf-8 -*-
"""Personal Agent Circadian Ocular Luxmeter Entrainment Skill.

Zero-dependency CIE S 026 melanopic equivalent daylight illuminance (melanopic EDI) quantifier,
intrinsically photosensitive retinal ganglion cell (ipRGC) modeler, and solar zeitgeber scheduler.
"""

import math
from typing import Dict, Any, Optional

class PersonalAgentCircadianOcularLuxLuxmeterEntrainment:
    """Quantitative circadian photobiology and ocular light hygiene engine based on
    Lucas et al. and the CIE S 026:2018 international standard for ipRGC-influenced light responses."""

    # Melanopic Action Factors (MAF) for common light spectra
    MELANOPIC_ACTION_FACTORS = {
        "direct_sunlight": 1.00,
        "overcast_daylight": 1.10,
        "cool_white_led": 0.72,
        "standard_office_fluorescent": 0.68,
        "computer_monitor_srgb": 0.65,
        "warm_white_led": 0.45,
        "candlelight_amber": 0.20,
        "blue_blocker_filtered": 0.08
    }

    def calculate_melanopic_edi_and_circadian_drive(
        self,
        photopic_lux: float = 12000.0,
        light_source_spectrum: str = "direct_sunlight",
        exposure_duration_minutes: float = 25.0,
        time_since_waking_hours: float = 0.5
    ) -> Dict[str, Any]:
        """Calculates Melanopic Equivalent Daylight Illuminance (melanopic EDI in lux),
        suprachiasmatic nucleus (SCN) circadian phase reset drive, and melatonin suppression risk."""
        lux = max(0.0, float(photopic_lux))
        dur = max(1.0, float(exposure_duration_minutes))
        src_key = light_source_spectrum.lower().replace(" ", "_")
        maf = self.MELANOPIC_ACTION_FACTORS.get(src_key, 0.65)
        waking_h = max(0.0, float(time_since_waking_hours))

        # Melanopic EDI = Photopic Lux * Melanopic Action Factor
        melanopic_edi = round(lux * maf, 1)

        # Photon Dose = Melanopic EDI * (Duration in minutes / 60)
        melanopic_photon_dose = round(melanopic_edi * (dur / 60.0), 1)

        # Circadian Phase Response Curve (PRC) Phase Shift Direction:
        # Light in early morning (0-2 hours after waking): Phase Advance (+0.3 to +1.8 hrs)
        # Light in mid-day (3-9 hours after waking): Stable Entrainment (0.0 hrs shift)
        # Light late evening / night (> 14 hours after waking): Phase Delay (-0.5 to -2.5 hrs)
        if waking_h <= 2.5:
            shift_direction = "Phase Advance (Shifts Circadian Clock Earlier)"
            shift_magnitude_hours = round(min(1.8, (melanopic_edi / 2000.0) * 0.9 * math.sqrt(dur / 20.0)), 2)
            timing_appropriateness = "Optimal Morning Solar Zeitgeber Window"
        elif waking_h <= 12.0:
            shift_direction = "Entrainment Maintenance (Stabilizes Master Pacemaker)"
            shift_magnitude_hours = 0.0
            timing_appropriateness = "Adequate Daytime Alertness Reinforcement"
        else:
            shift_direction = "Phase Delay (Undesirably Delays Sleep Gate and DLMO)"
            shift_magnitude_hours = -round(min(2.5, (melanopic_edi / 150.0) * 0.8 * math.sqrt(dur / 30.0)), 2)
            timing_appropriateness = "Adverse Circadian Disruption / Melatonin Suppression Warning"

        # International CIE Consensus Benchmark:
        # Daytime target: >= 250 melanopic EDI continuously
        # Morning pulse target: >= 1000 melanopic EDI for >= 20 mins
        # Pre-bed target: < 10 melanopic EDI in 3 hours prior to sleep
        if waking_h <= 2.5:
            adequacy = "High Morning Reset Pulse" if melanopic_edi >= 1000.0 else "Sub-Optimal Morning Photon Flux"
        elif waking_h <= 12.0:
            adequacy = "Sufficient Alertness Flux" if melanopic_edi >= 250.0 else "Sub-Threshold Indoor Dim Light (< 250 EDI)"
        else:
            adequacy = "Circadian Safe (< 10 EDI)" if melanopic_edi < 10.0 else "Circadian Toxic Evening Light (> 10 EDI)"

        return {
            "photopic_illuminance_lux": lux,
            "light_source": light_source_spectrum,
            "melanopic_action_factor_maf": maf,
            "melanopic_equivalent_daylight_illuminance_edi": melanopic_edi,
            "melanopic_photon_dose_lux_hours": melanopic_photon_dose,
            "time_since_waking_hours": waking_h,
            "circadian_phase_shift_trajectory": shift_direction,
            "projected_phase_shift_hours": f"{'+' if shift_magnitude_hours > 0 else ''}{shift_magnitude_hours} hrs",
            "photobiological_adequacy_evaluation": adequacy,
            "timing_appropriateness": timing_appropriateness
        }

    def prescribe_daily_solar_zeitgeber_schedule(
        self,
        wake_time_24h: float = 6.5,
        planned_sleep_time_24h: float = 22.5
    ) -> Dict[str, Any]:
        """Schedules exact chronological clock times for morning photon viewing,
        daytime illumination thresholds, and evening low-lux melatonergic cutoffs."""
        wake = wake_time_24h % 24.0
        sleep = planned_sleep_time_24h % 24.0

        def _fmt(h_float: float) -> str:
            h = int(h_float) % 24
            m = int(round((h_float - int(h_float)) * 60))
            if m >= 60:
                h = (h + 1) % 24
                m = 0
            return f"{h:02d}:{m:02d}"

        morning_start = wake
        morning_end = (wake + 1.0) % 24.0
        dusk_viewing = (sleep - 3.5) % 24.0
        evening_cutoff = (sleep - 2.5) % 24.0

        return {
            "target_wake_time": _fmt(wake),
            "target_sleep_time": _fmt(sleep),
            "morning_solar_anchoring_window": f"{_fmt(morning_start)} - {_fmt(morning_end)} (Target: >= 10,000 lux outdoor / >= 1,000 melanopic EDI for 15-30 min)",
            "daytime_indoor_work_benchmark": "Maintain >= 250 melanopic EDI continuously at eye level",
            "dusk_solar_transition_window": f"{_fmt(dusk_viewing)} (5-10 min outdoor viewing of low solar angle light to buffer evening sensitivity)",
            "evening_melatonin_preservation_cutoff": f"{_fmt(evening_cutoff)} (Drop all ambient lighting to < 10 melanopic lux; red/amber warm spectrum only)",
            "photobiological_mandate": "Direct photon absorption via melanopsin ganglion cells anchors the suprachiasmatic nucleus (SCN) circadian period."
        }
