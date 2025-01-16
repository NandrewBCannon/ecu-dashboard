# config.py

DASHBOARD_CLASSES = {
    "CombinedDashboard": lambda parent: __import__('dashboards.combined_dashboard', fromlist=['CombinedDashboard']).CombinedDashboard(parent),
    "SpeedGaugeDashboard": lambda parent: __import__('dashboards.speed_gauge_dashboard', fromlist=['SpeedGaugeDashboard']).SpeedGaugeDashboard(parent),
    "RpmDashboard": lambda parent: __import__('dashboards.rpm_dashboard', fromlist=['RpmDashboard']).RpmDashboard(parent),
    "BatteryVoltageDashboard": lambda parent: __import__('dashboards.battery_voltage_dashboard', fromlist=['BatteryVoltageDashboard']).BatteryVoltageDashboard(parent),
    "InjectorDutyDashboard": lambda parent: __import__('dashboards.injector_duty_dashboard', fromlist=['InjectorDutyDashboard']).InjectorDutyDashboard(parent),
    "IgnitionTimingDashboard": lambda parent: __import__('dashboards.ignition_timing_dashboard', fromlist=['IgnitionTimingDashboard']).IgnitionTimingDashboard(parent),
    "AACDashboard": lambda parent: __import__('dashboards.aac_dashboard', fromlist=['AACDashboard']).AACDashboard(parent),
    "O2VoltageDashboard": lambda parent: __import__('dashboards.o2_voltage_dashboard', fromlist=['O2VoltageDashboard']).O2VoltageDashboard(parent),
    "WaterTempDashboard": lambda parent: __import__('dashboards.water_temp_dashboard', fromlist=['WaterTempDashboard']).WaterTempDashboard(parent),
    "AFMVoltageDashboard": lambda parent: __import__('dashboards.afm_voltage_dashboard', fromlist=['AFMVoltageDashboard']).AFMVoltageDashboard(parent),
    "TPSDashboard": lambda parent: __import__('dashboards.tps_dashboard', fromlist=['TPSDashboard']).TPSDashboard(parent),
}
