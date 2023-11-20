# Copyright (c) 2023, Techmaniacc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MyExcept(Exception):
	def __init__(self, msg, error_code):
		super().__init__(msg)
		self.error_code=error_code
		
class Driver1(Document):
	def before_save(self):
		if self.last_name:
			self.full_name = self.first_name + " " + self.last_name
		else:
			self.full_name = self.first_name
   
	def validate(self):
		if self.first_name and self.last_name and self.first_name.lower() == self.last_name.lower():
			frappe.throw("First Name and Last Name cannot be the same")


   
   
