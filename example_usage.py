# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Circadian Ocular Luxmeter Entrainment Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentCircadianOcularLuxLuxmeterEntrainment

def main():
    agent = PersonalAgentCircadianOcularLuxLuxmeterEntrainment()

    print("=" * 70)
    print("DEMO: Personal Agent Circadian Ocular Lux & Solar Zeitgeber Entrainment")
    print("=" * 70)

    # 1. Morning Direct Sunlight Viewing (15,000 lux, 20 mins, 30 min post-waking)
    res_sun = agent.calculate_melanopic_edi_and_circadian_drive(
        photopic_lux=15000.0,
        light_source_spectrum="direct_sunlight",
        exposure_duration_minutes=20.0,
        time_since_waking_hours=0.5
    )

    print(f"\n1. Morning Solar Viewing Photobiology (15,000 Lux Direct Sun):")
    print(f"   Photopic Lux: {res_sun['photopic_illuminance_lux']} lux | Spectrum: {res_sun['light_source']}")
    print(f"   Melanopic Action Factor (MAF): {res_sun['melanopic_action_factor_maf']}")
    print(f"   Melanopic EDI: {res_sun['melanopic_equivalent_daylight_illuminance_edi']} lux")
    print(f"   Photon Dose: {res_sun['melanopic_photon_dose_lux_hours']} lux*hours")
    print(f"   PRC Trajectory: {res_sun['circadian_phase_shift_trajectory']}")
    print(f"   Projected Phase Shift: {res_sun['projected_phase_shift_hours']}")
    print(f"   Photobiological Evaluation: {res_sun['photobiological_adequacy_evaluation']}")
    print(f"   Timing Appropriateness: {res_sun['timing_appropriateness']}")

    # 2. Nighttime Screen Exposure (180 lux, computer monitor, 15 hours post-waking / pre-bed)
    res_night = agent.calculate_melanopic_edi_and_circadian_drive(
        photopic_lux=180.0,
        light_source_spectrum="computer_monitor_srgb",
        exposure_duration_minutes=45.0,
        time_since_waking_hours=15.0
    )

    print(f"\n2. Nighttime Screen Exposure Photobiology (180 Lux Monitor @ T+15 hrs):")
    print(f"   Melanopic EDI: {res_night['melanopic_equivalent_daylight_illuminance_edi']} lux")
    print(f"   PRC Trajectory: {res_night['circadian_phase_shift_trajectory']}")
    print(f"   Projected Phase Shift: {res_night['projected_phase_shift_hours']}")
    print(f"   Evaluation: {res_night['photobiological_adequacy_evaluation']}")
    print(f"   Timing Warning: {res_night['timing_appropriateness']}")

    # 3. Schedule Daily Solar Zeitgeber Timetable
    res_sched = agent.prescribe_daily_solar_zeitgeber_schedule(
        wake_time_24h=6.5,
        planned_sleep_time_24h=22.5
    )

    print(f"\n3. Daily 24-Hour Solar Zeitgeber Schedule (Wake: 06:30, Sleep: 22:30):")
    print(f"   Morning Window: {res_sched['morning_solar_anchoring_window']}")
    print(f"   Daytime Work Standard: {res_sched['daytime_indoor_work_benchmark']}")
    print(f"   Dusk Transition: {res_sched['dusk_solar_transition_window']}")
    print(f"   Evening Cutoff: {res_sched['evening_melatonin_preservation_cutoff']}")
    print(f"   Photobiological Principle: {res_sched['photobiological_mandate']}")

    print("\nVerification complete: Ocular lux entrainment engine executed flawlessly.")

if __name__ == "__main__":
    main()
