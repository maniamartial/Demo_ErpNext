# Copyright (c) 2023, Techmaniacc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ServerSideScripting(Document):
	# def validate(self):
	# 	frappe.msgprint("Hello frappe")
	
	#def before_save(self)
	#def before_insert(self)
	#def on_update(self)
	#def on_submit(self)
	#def on_cancel(self)
	#def on_thrash(self)
	#def after_delete(self)

	# def before_submit(self):
	# 	frappe.msgprint("Hello frappe before submit")
	# def validate(self):
	# 	frappe.msgprint(("Hello my full name is '{0}' ").format(
	# 		self.first_name
	# 	))

	# def validate(self):
	# 	for row in self.get('family_members'):
	# 		frappe.msgprint(("{0}. The family members name is '{1}' and relationshi is '{2}'").format(
	# 			row.idx, row.name1, row.relation
			
	# 		))
	# frappe.get_doc(doctype, name)
	# def validate(self):
	# 	self.get_doc()
	
	# def get_doc(self):
	# 	doc=frappe.get_doc("Client Side Scripting", self.client_side_doc)
	# 	frappe.msgprint(("The First Name is '{0}' and Age is '{1}'").format(
	# 		doc.first_name, doc.age)
	# 	)
	pass

