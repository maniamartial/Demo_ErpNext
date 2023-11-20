# Copyright (c) 2023, Techmaniacc and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDriver1(FrappeTestCase):
	def test_full_name_is_set_automatically(self):
		deriver1=frappe.get_doc({
			"doctype":"Driver1",
			"first_name":"Test",
			"last_name":"Driver1"
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
			"last_name": "Doe"  # Setting different first_name and last_name values
		}).insert()
		# Assert that saving this document does not raise a ValidationError
		self.assertRaises(frappe.exceptions.ValidationError)

  