frappe.pages['dashboard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Dashboard',
		single_column: true
	});
	frappe.dashboard.make(page);
	frappe.dashboard.getStandardChartType(page);
	frappe.breadcrumbs.add("Dashboard");
}

frappe.dashboard = {
	start: 0,
	make: function(page) {
		var me = frappe.dashboard;
		me.page = page;
		me.body = $('<div></div>').appendTo(me.page.main);
		var data = "";
		$(frappe.render_template('dashboard', data)).appendTo(me.body);

                // add menu button
		this.page.add_menu_item(__("Change Dashboard Settings"), function() {
			window.location.href="#Form/Dashboard Settings";
		});
		this.page.add_menu_item(__("Reload"), function() {
			location.reload();
		});
		// attach button handlers
		this.page.main.find(".btn-bar").on('click', function() {
			frappe.dashboard.newChart(page, "bar");
		});
		this.page.main.find(".btn-line").on('click', function() {
			frappe.dashboard.newChart(page, "line");
		});
		this.page.main.find(".btn-scatter").on('click', function() {
			frappe.dashboard.newChart(page, "scatter");
		});
		this.page.main.find(".btn-pie").on('click', function() {
			frappe.dashboard.newChart(page, "pie");
		});
		this.page.main.find(".btn-percentage").on('click', function() {
			frappe.dashboard.newChart(page, "percentage");
		});
	},
	newChart: function(page, style) {
		var data = {
			labels: ["12am-3am", "3am-6am", "6am-9am", "9am-12pm",
					"12pm-3pm", "3pm-6pm", "6pm-9pm", "9pm-12am"],

			datasets: [
				{
					title: "Some Data",
					values: [25, 40, 30, 35, 8, 52, 17, -4]
				},
				{
					title: "Another Set",
					values: [25, 50, -10, 15, 18, 32, 27, 14]
				},
				{
					title: "Yet Another",
					values: [15, 20, -3, -15, 58, 12, -17, 37]
				}
			]
		};
		var chart = new Chart({
			parent: "#CustomerChart", // or a DOM element
			title: "Lead / Customer overview",
			data: data,
			type: style, // or 'line', 'scatter', 'pie', 'percentage'
			height: 250,

			colors: ['#7cd6fd', 'violet', 'blue'],
			// hex-codes or these preset colors;
			// defaults (in order):

			format_tooltip_x: d => (d + '').toUpperCase(),
			format_tooltip_y: d => d + ' pts'
		});
	},
	getStandardChartType: function(page) {
		frappe.model.get_value('Dashboard Settings', {'name': 'Dashboard Settings'}, 'chart_type', function(r) {
			//console.log(d.chart_type);
			if(r){
				frappe.dashboard.newChart(page, r.chart_type);
			}
		});
	}
}
