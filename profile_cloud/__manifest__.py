# Copyright (C) 2022 Trevi Software (https://trevi.et)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Cloud Profile",
    "summary": "Cloud features that avoid local storage of data",
    "version": "14.0.1.0.0",
    "author": "TREVI Software",
    "website": "https://github.com/trevi-software/odoo-profiles",
    "license": "AGPL-3",
    "category": "Generic Modules",
    "images": ["static/src/img/main_screenshot.png"],
    "depends": [
        "attachment_s3",
        "cloud_platform",
        "logging_json",
        "monitoring_log_requests",
        "monitoring_prometheus",
        "monitoring_status",
        "session_redis",
    ],
    "data": [],
    "installable": True,
    "application": True,
}
