###############################################################################
#
#   Module for OpenERP
#   Copyright (C) 2019,2021-2023 Trevi Software (http://trevi.et).
#   Copyright (C) 2014 Akretion (http://www.akretion.com).
#   @author Sébastien BEAU <sebastien.beau@akretion.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    "name": "Purchase Management Profile",
    "version": "14.0.1.0.0",
    "author": "TREVI Software, trevi-software",
    "website": "https://github.com/trevi-software/odoo-profiles",
    "license": "AGPL-3",
    "category": "Generic Modules",
    "images": ["static/src/img/main_screenshot.png"],
    "depends": [
        # https://github.com/OCA/server-ux
        "base_tier_validation",
        "base_tier_validation_correction",
        "base_tier_validation_report",
        "base_tier_validation_server_action",
        "base_tier_validation_waiting",
        # https://github.com/OCA/purchase-workflow
        "purchase_advance_payment",
        "purchase_delivery_split_date",
        "purchase_last_price_info",
        "purchase_location_by_line",
        "purchase_order_line_price_history",
        "purchase_reception_status",
        "purchase_request",
        "purchase_request_tier_validation",
        "purchase_request_to_requisition",
        "purchase_requisition_auto_rfq",
        "purchase_requisition_tier_validation",
        "purchase_rfq_number",
        "purchase_substate",
        "purchase_tags",
        "purchase_tier_validation",
        "subcontracted_service",
    ],
    "data": [],
    "installable": True,
    "auto_install": False,
    "application": True,
}
