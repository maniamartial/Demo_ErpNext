import frappe
from frappe import qb
from frappe.tests.utils import FrappeTestCase

class TestGrossProfit(FrappeTestCase):
    def setUp(self):
        frappe.set_user('Administrator')
        self.item = frappe.get_doc({
            "doctype": "Item",
            "item_code": "EPSO TOP - 5Kg",
            "item_name": "EPSO TOP - 5Kg",
            "stock_uom": "Nos",
            "item_group": "EPSO TOP",
        }).insert()
        self.item.weight_per_unit = 10
        self.item.save()
        
    def tearDown(self):
        frappe.db.rollback()
        
    def test_calculate_qty_in_chosen_uom(self):
        self.assertEqual(self.item.stock_uom, 'Nos')
        self.assertEqual(self.item.weight_per_unit, 10)
        
    def test_conversion_factor_fetching_data(self):
        conversion_factor = frappe.db.get_value("UOM Conversion Detail", {"parent": self.item.name, "uom": "Nos"}, "conversion_factor")
        self.assertEqual(conversion_factor, 10)
