# Copyright (c) 2023, Techmaniacc and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime
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
		if self.age and isinstance(self.age, int):
			
			if self.age < 18:
				frappe.throw("Age cannot be less than 18")
			elif self.age > 60:
				frappe.throw("Age cannot be greater than 60")
		else:
			frappe.throw("Age is not set or has an invalid value")
		if self.year_joined and isinstance(self.year_joined, str):
			try:
				year_joined_date = datetime.strptime(self.year_joined, '%Y-%m-%d').date()
				current_date = datetime.strptime(frappe.utils.nowdate(), '%Y-%m-%d').date()
				
				if year_joined_date > current_date:
					frappe.throw("Year Joined cannot be greater than the current year")
			except ValueError:
				frappe.throw("Invalid date format for year_joined")
		else:
			frappe.throw("Year Joined is not set or has an invalid value")
	
   


   
   
