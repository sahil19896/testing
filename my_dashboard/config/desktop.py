# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "My Dashboard",
			"color": "red",
			"icon": "fa fa-dashboard",
			"type": "module",
			"label": _("My Dashboard")
		}
	]
