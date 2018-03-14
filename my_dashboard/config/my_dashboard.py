from __future__ import unicode_literals
from frappe import _

def get_data():
	return[
		{
			"label": _("Dashboards"),
			"icon": "fa fa-dashboard",
			"items": [
				{
					"type": "page",
					"name": "dashboard",
					"label": _("Dashboard"),
					"description": _("Admin Dashboard")
				},
				{
					"type": "page",
					"name": "my_dashboard",
					"label": _("My Dashboard"),
					"description": _("My Dashboard")
				},
				{
					"type": "page",
					"name": "new_dashboard",
					"label": _("New Dashboard"),
					"description": _("New Dashboard")
				}
			]
		},
		{
			"label": _("Setup"),
			"icon": "fa fa-dashboard",
			"items": [
				{
					"type": "doctype",
					"name": "Dashboard Settings",
					"label": _("Dashboard Settings"),
					"description": _("Setup for Dashboard")
				},
				{
					"type": "doctype",
					"name": "User Dashboard Settings",
					"label": _("User Dashboard Settings"),
					"description": _("User Dashboard Settings")
				},
				{
					"type": "doctype",
					"name": "Dashboard Standard Settings",
					"label": _("Dashboard Standard Settings"),
					"description": _("Dashboard Standard Settings")
				}
			]
		}
	]
