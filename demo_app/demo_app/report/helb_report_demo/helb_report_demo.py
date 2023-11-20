# Copyright (c) 2022, Navari Limited and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, erpnext
from frappe import _

def execute(filters=None):

	company_currency = erpnext.get_company_currency(filters.get("company"))
	columns = get_columns()
	data = get_data(filters,company_currency)

	return columns, data

def get_columns():
	columns = [			
		{
		'label': _('Employee ID'),
		'fieldname': 'employee',
		'options': 'Employee',
		'width': 180
		},
		{
		'label': _('Employee Names'),
		'fieldname': 'employee_name',
		'fieldtype': 'Read Only',
		'width': 260
		},
		{
		'label': _('National ID'),
		'fieldname': 'national_id',
		'fieldtype': 'Data',
		'width': 180
		},
		{
		'label': _('Amount'),
		'fieldname': 'amount',
		'fieldtype': 'Currency',		
		'width': 200
		}
	]
		
	return columns

def get_data(filters,company_currency,conditions=""):
	# employee=frappe.qb.DocType("Employee")
	# salary_slip=frappe.qb.DocType("Salary Slip")
	# salary_detail=frappe.qb.DocType("Salary Detail")
	# query=frappe.qb.from_(employee)\
	# 	.inner_join(salary_slip)\
  	# 	.on(employee.name==salary_slip.employee)\
	# 	.inner_join(salary_detail)\
	# 	.on(salary_detail.parent==salary_slip.name)\
	# 	.select(employee.name,employee.employee_name,employee.national_id,salary_detail.amount)\
	# 	.where(salary_detail.amount!=0)
	# doc_status = {"Draft": 0, "Submitted": 1, "Cancelled": 2}
	# for filter in filters:
	# 	if filter=="from_date":
	# 		query=query.where(salary_slip.start_date==filters.from_date)
	# 	if filter=="to_date":
	# 		query=query.where(salary_slip.end_date==filters.to_date)
	# 	if filter=="company":
	# 		query=query.where(salary_slip.company==filters.company)
	# 	if filter=="salary_component":
	# 		query=query.where(salary_detail.salary_component==filters.salary_component)
	# 	if filter=="currency" and filters.get("currency") != company_currency:
	# 		query=query.where(salary_slip.currency==filters.currency)
	# 	if filter=="docstatus":
	# 		query=query.where(salary_slip.docstatus==doc_status[filters.get("docstatus")])
 
	conditions = get_conditions(filters,company_currency)

	if filters.from_date > filters.to_date:
		frappe.throw(_("To Date cannot be before From Date. {}").format(filters.to_date))

	data = frappe.db.sql("""
	SELECT  ss.employee, ss.employee_name,
			ss.start_date, ss.end_date, 
			e.national_id, sd.amount
	FROM `tabEmployee` e, `tabSalary Slip` ss, `tabSalary Detail` sd
	WHERE %s
		and e.name = ss.employee
		and sd.parent = ss.name		
		and sd.amount != 0	
	""" % conditions, filters, as_dict=1)
	return data

def get_conditions(filters,company_currency):
	conditions = ""
	doc_status = {"Draft": 0, "Submitted": 1, "Cancelled": 2}

	if filters.get("docstatus"):
		conditions += "ss.docstatus = {0}".format(doc_status[filters.get("docstatus")])

	if filters.get("from_date"): conditions += " and ss.start_date = %(from_date)s"
	if filters.get("to_date"): conditions += " and ss.end_date = %(to_date)s"
	if filters.get("company"): conditions += " and ss.company = %(company)s"
	if filters.get("salary_component"): conditions += " and sd.salary_component = %(salary_component)s"
	if filters.get("currency") and filters.get("currency") != company_currency:
		conditions += " and ss.currency = %(currency)s"

	return conditions