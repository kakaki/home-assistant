"""Constants for Neato integration."""

NEATO_DOMAIN = "neato"

CONF_VENDOR = "vendor"
NEATO_ROBOTS = "neato_robots"
NEATO_LOGIN = "neato_login"
NEATO_CONFIG = "neato_config"
NEATO_MAP_DATA = "neato_map_data"
NEATO_PERSISTENT_MAPS = "neato_persistent_maps"

VALID_VENDORS = ["neato", "vorwerk"]

MODE = {1: "Eco", 2: "Turbo"}

ACTION = {
    0: "Invalid",
    1: "House Cleaning",
    2: "Spot Cleaning",
    3: "Manual Cleaning",
    4: "Docking",
    5: "User Menu Active",
    6: "Suspended Cleaning",
    7: "Updating",
    8: "Copying logs",
    9: "Recovering Location",
    10: "IEC test",
    11: "Map cleaning",
    12: "Exploring map (creating a persistent map)",
    13: "Acquiring Persistent Map IDs",
    14: "Creating & Uploading Map",
    15: "Suspended Exploration",
}

ERRORS = {
    "ui_error_battery_battundervoltlithiumsafety": "Replace battery",
    "ui_error_battery_critical": "Replace battery",
    "ui_error_battery_invalidsensor": "Replace battery",
    "ui_error_battery_lithiumadapterfailure": "Replace battery",
    "ui_error_battery_mismatch": "Replace battery",
    "ui_error_battery_nothermistor": "Replace battery",
    "ui_error_battery_overtemp": "Replace battery",
    "ui_error_battery_overvolt": "Replace battery",
    "ui_error_battery_undercurrent": "Replace battery",
    "ui_error_battery_undertemp": "Replace battery",
    "ui_error_battery_undervolt": "Replace battery",
    "ui_error_battery_unplugged": "Replace battery",
    "ui_error_brush_stuck": "Brush stuck",
    "ui_error_brush_overloaded": "Brush overloaded",
    "ui_error_bumper_stuck": "Bumper stuck",
    "ui_error_check_battery_switch": "Check battery",
    "ui_error_corrupt_scb": "Call customer service corrupt board",
    "ui_error_deck_debris": "Deck debris",
    "ui_error_dflt_app": "Check Neato app",
    "ui_error_disconnect_chrg_cable": "Disconnected charge cable",
    "ui_error_disconnect_usb_cable": "Disconnected USB cable",
    "ui_error_dust_bin_missing": "Dust bin missing",
    "ui_error_dust_bin_full": "Dust bin full",
    "ui_error_dust_bin_emptied": "Dust bin emptied",
    "ui_error_hardware_failure": "Hardware failure",
    "ui_error_ldrop_stuck": "Clear my path",
    "ui_error_lds_jammed": "Clear my path",
    "ui_error_lds_bad_packets": "Check Neato app",
    "ui_error_lds_disconnected": "Check Neato app",
    "ui_error_lds_missed_packets": "Check Neato app",
    "ui_error_lwheel_stuck": "Clear my path",
    "ui_error_navigation_backdrop_frontbump": "Clear my path",
    "ui_error_navigation_backdrop_leftbump": "Clear my path",
    "ui_error_navigation_backdrop_wheelextended": "Clear my path",
    "ui_error_navigation_noprogress": "Clear my path",
    "ui_error_navigation_origin_unclean": "Clear my path",
    "ui_error_navigation_pathproblems": "Cannot return to base",
    "ui_error_navigation_pinkycommsfail": "Clear my path",
    "ui_error_navigation_falling": "Clear my path",
    "ui_error_navigation_noexitstogo": "Clear my path",
    "ui_error_navigation_nomotioncommands": "Clear my path",
    "ui_error_navigation_rightdrop_leftbump": "Clear my path",
    "ui_error_navigation_undockingfailed": "Clear my path",
    "ui_error_picked_up": "Picked up",
    "ui_error_qa_fail": "Check Neato app",
    "ui_error_rdrop_stuck": "Clear my path",
    "ui_error_reconnect_failed": "Reconnect failed",
    "ui_error_rwheel_stuck": "Clear my path",
    "ui_error_stuck": "Stuck!",
    "ui_error_unable_to_return_to_base": "Unable to return to base",
    "ui_error_unable_to_see": "Clean vacuum sensors",
    "ui_error_vacuum_slip": "Clear my path",
    "ui_error_vacuum_stuck": "Clear my path",
    "ui_error_warning": "Error check app",
    "batt_base_connect_fail": "Battery failed to connect to base",
    "batt_base_no_power": "Battery base has no power",
    "batt_low": "Battery low",
    "batt_on_base": "Battery on base",
    "clean_tilt_on_start": "Clean the tilt on start",
    "dustbin_full": "Dust bin full",
    "dustbin_missing": "Dust bin missing",
    "gen_picked_up": "Picked up",
    "hw_fail": "Hardware failure",
    "hw_tof_sensor_sensor": "Hardware sensor disconnected",
    "lds_bad_packets": "Bad packets",
    "lds_deck_debris": "Debris on deck",
    "lds_disconnected": "Disconnected",
    "lds_jammed": "Jammed",
    "lds_missed_packets": "Missed packets",
    "maint_brush_stuck": "Brush stuck",
    "maint_brush_overload": "Brush overloaded",
    "maint_bumper_stuck": "Bumper stuck",
    "maint_customer_support_qa": "Contact customer support",
    "maint_vacuum_stuck": "Vacuum is stuck",
    "maint_vacuum_slip": "Vacuum is stuck",
    "maint_left_drop_stuck": "Vacuum is stuck",
    "maint_left_wheel_stuck": "Vacuum is stuck",
    "maint_right_drop_stuck": "Vacuum is stuck",
    "maint_right_wheel_stuck": "Vacuum is stuck",
    "not_on_charge_base": "Not on the charge base",
    "nav_robot_falling": "Clear my path",
    "nav_no_path": "Clear my path",
    "nav_path_problem": "Clear my path",
    "nav_backdrop_frontbump": "Clear my path",
    "nav_backdrop_leftbump": "Clear my path",
    "nav_backdrop_wheelextended": "Clear my path",
    "nav_mag_sensor": "Clear my path",
    "nav_no_exit": "Clear my path",
    "nav_no_movement": "Clear my path",
    "nav_rightdrop_leftbump": "Clear my path",
    "nav_undocking_failed": "Clear my path",
}

ALERTS = {
    "ui_alert_dust_bin_full": "Please empty dust bin",
    "ui_alert_recovering_location": "Returning to start",
    "ui_alert_battery_chargebasecommerr": "Battery error",
    "ui_alert_busy_charging": "Busy charging",
    "ui_alert_charging_base": "Base charging",
    "ui_alert_charging_power": "Charging power",
    "ui_alert_connect_chrg_cable": "Connect charge cable",
    "ui_alert_info_thank_you": "Thank you",
    "ui_alert_invalid": "Invalid check app",
    "ui_alert_old_error": "Old error",
    "ui_alert_swupdate_fail": "Update failed",
    "dustbin_full": "Please empty dust bin",
    "maint_brush_change": "Change the brush",
    "maint_filter_change": "Change the filter",
    "clean_completed_to_start": "Cleaning completed",
    "nav_floorplan_not_created": "No floorplan found",
    "nav_floorplan_load_fail": "Failed to load floorplan",
    "nav_floorplan_localization_fail": "Failed to load floorplan",
    "clean_incomplete_to_start": "Cleaning incomplete",
    "log_upload_failed": "Logs failed to upload",
}
