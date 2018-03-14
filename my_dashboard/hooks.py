# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "my_dashboard"
app_title = "My Dashboard"
app_publisher = "sahil"
app_description = "Dashboard"
app_icon = "fa fa-dashboard"
app_color = "red"
app_email = "sahil19896@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/my_dashboard/css/my_dashboard.css"
# app_include_js = "/assets/my_dashboard/js/my_dashboard.js"

# include js, css files in header of web template
# web_include_css = "/assets/my_dashboard/css/my_dashboard.css"
# web_include_js = "/assets/my_dashboard/js/my_dashboard.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "my_dashboard.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "my_dashboard.install.before_install"
# after_install = "my_dashboard.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "my_dashboard.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"my_dashboard.tasks.all"
# 	],
# 	"daily": [
# 		"my_dashboard.tasks.daily"
# 	],
# 	"hourly": [
# 		"my_dashboard.tasks.hourly"
# 	],
# 	"weekly": [
# 		"my_dashboard.tasks.weekly"
# 	]
# 	"monthly": [
# 		"my_dashboard.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "my_dashboard.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "my_dashboard.event.get_events"
# }

