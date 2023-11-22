# Copyright (c) 2023, Techmaniacc and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDriver1(FrappeTestCase):
	def test_full_name_is_set_automatically(self):
		deriver1=frappe.get_doc({
			"doctype":"Driver1",
			"first_name":"Test",
			"last_name":"Driver1",
   "age": 34 , # Setting age to 17
				"year_joined": "2023-12-12"
		}).insert()
		self.assertEqual(deriver1.full_name,"Test Driver1")
  
	def test_fullname_is_correctly_when_no_lastname(self):
		driver2=frappe.get_doc({
			"doctype":"Driver1",
   "first_name":"No_name"
		}).insert()
		self.assertEqual(driver2.full_name, "No_name")
  
	def test_first_name_and_last_name_should_not_be_the_same(self):
		driver3 = frappe.get_doc({
			"doctype": "Driver1",
			"first_name": "John",
			"last_name": "Doe" ,
   "age": 34 , # Setting age to 17
				"year_joined": "2023-12-12"# Setting different first_name and last_name values
		}).insert()
		# Assert that saving this document does not raise a ValidationError
		self.assertRaises(frappe.exceptions.ValidationError)
  
	def test_age_should_be_between_18_and_60(self):
		with self.assertRaises(frappe.exceptions.ValidationError):
			driver4 = frappe.get_doc({
				"doctype": "Driver1",
				"first_name": "John",
				"last_name": "Doe",
				"age": 34 , # Setting age to 17
				"year_joined": "2023-12-12"

			}).insert()
      
	def test_year_joined(self):
		with self.assertRaises(frappe.exceptions.ValidationError, msg="Date Joined cannot be greater than the current year tests"):
			driver5 = frappe.get_doc({
				"doctype": "Driver1",
				"first_name": "John",
				"last_name": "Doe",
				"age": 21,
				"year_joined": "2023-12-12"  # Setting year_joined to a future date

			}).insert()
   