# Copyright (c) 2023, Techmaniacc and contributors
# For license information, please see license.txt
from frappe.model.naming import getseries


import frappe
from datetime import datetime
from frappe.model.document import Document

class MyExcept(Exception):
	def __init__(self, msg, error_code):
		super().__init__(msg)
		self.error_code=error_code
		
class Driver1(Document):
    
	def before_save(self):
		# frappe.db.rename_table("Driver1", "Driver2")
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
		
  
	def autoname(self):
		if self.age>30 and self.age<40:
			prefix = f'{self.first_name[0:3]}-{self.last_name[0:3]}-{datetime.now().year}-30-'
		if self.age>40 and self.age<50:
			prefix = f'{self.first_name[0:3]}-{self.last_name[0:3]}-{datetime.now().year}-40-'
		if self.age>50:
			prefix = f'{self.first_name[0:3]}-{self.last_name[0:3]}-{datetime.now().year}-50-'
		self.name = prefix + getseries(prefix, 4)

     
	
   


   
   
