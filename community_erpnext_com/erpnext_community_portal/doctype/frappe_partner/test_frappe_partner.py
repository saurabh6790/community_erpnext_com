# Copyright (c) 2015, Frappe Technologies Pvt Ltd and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Frappe Partner')

class TestFrappePartner(unittest.TestCase):
	pass