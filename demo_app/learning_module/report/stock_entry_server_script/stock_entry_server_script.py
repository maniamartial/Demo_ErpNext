# Copyright (c) 2023, Techmaniacc and contributors
# For license information, please see license.txt


import frappe
from frappe import _, msgprint

def execute(filters=None):
	if not filters: filters = {}

	data, columns = [], []

	columns = get_columns()
	cs_data = get_stock_entry_data(filters)

	if not cs_data:
		msgprint(_('No records found'))
		return columns, cs_data

	data = []
	for d in cs_data:
		row = frappe._dict({
				'naming_series': d.naming_series,
				'stock_entry_type': d.stock_entry_type,
				'posting_date': d.posting_date,
				'source_warehouse_address':d.source_warehouse_address,
				'target_warehouse_address':d.target_warehouse_address,
				
				
			})
		data.append(row)

	report_summary = display_stock_report_summary()
	return columns, data, None, None, report_summary

def get_columns():
		
	return [
			{
				'fieldname': 'naming_series',
				'label': _('Naming Series'),
				'fieldtype': 'Data',
				'width': '120'
			},
			{
				'fieldname': 'stock_entry_type',
				'label': _('Stock Entry Type'),
				'fieldtype': 'Data',
				'width': '120'
			},
			{
				'fieldname': 'posting_date',
				'label': _('Posting Date'),
				'fieldtype': 'Date',
				'width': '100'
			},
			{
				'fieldname': 'source_warehouse_address',
				'label': _('Source Warehouse'),
				'fieldtype': 'Data',
				'width': '120'
			},
			{
				'fieldname': 'source_warehouse_address',
				'label': _('Target Warehouse'),
				'fieldtype': 'Data',
				'width': '120'
			},
			
		]

def get_stock_entry_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype='Stock Entry',
		fields = ['naming_series', 'stock_entry_type', 'posting_date', 'source_warehouse_address', 'target_warehouse_address'],
		filters=conditions,
		order_by='naming_series desc'
	)	
	return data
	
def get_conditions(filters):
	conditions = {}
	for key, value in filters.items():
		if filters.get(key):
			conditions[key] = value

	return conditions

def get_stock_report_summary(data):
    if not data:
        return None

    total_dispatch = 0
    total_receipt = 0
    total_variance = 0
    variance_percentage = 0

    for entry in data:
        total_dispatch += entry['dispatch']
        total_receipt += entry['receipt']
        total_variance += entry['variance']

    if total_dispatch != 0:
        variance_percentage = (total_variance / total_dispatch) * 100

    return [
        {
            'value': total_dispatch,
            'indicator': 'Green',
            'label': 'Total Dispatch',
            'datatype': 'Float',
        },
        {
            'value': total_receipt,
            'indicator': 'Green',
            'label': 'Total Receipt',
            'datatype': 'Float',
        },
        {
            'value': total_variance,
            'indicator': 'Green',
            'label': 'Total Variance',
            'datatype': 'Float',
        },
        {
            'value': variance_percentage,
            'indicator': 'Green',
            'label': 'Variance %',
            'datatype': 'Float',
        }
    ]

def display_stock_report_summary():
    # Dummy data for the example
    dummy_data = [
        {'dispatch': 100, 'receipt': 120, 'variance': 20},
        {'dispatch': 150, 'receipt': 130, 'variance': -20},
        {'dispatch': 200, 'receipt': 220, 'variance': 20},
    ]

    return get_stock_report_summary(dummy_data)
