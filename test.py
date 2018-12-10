# @Author: HaoxuanLi  
# @Date 2018/12/9
# CWID: 10434197
import unittest

from Utils.FileReader import FileReader
from domain.store import Store
from final_controller import Final_controller
import os


class TestFinalController(unittest.TestCase):
    c = Final_controller()
    base_path = os.path.abspath("file_dir")

    def test_store(self):
        stores_file = open(os.path.join(self.base_path, "stores.txt"))
        self.assertEqual(len([l for l in stores_file]), len(self.c.stores) + 1)
        stores_file.close()

    def test_transaction(self):
        tran_file = open(os.path.join(self.base_path, "transactions.txt"))
        self.assertNotEqual(len([l for l in tran_file]), len(self.c.transactions) + 1)
        tran_file.close()

    def test_products(self):
        products_file = open(os.path.join(self.base_path, "products.txt"))
        self.assertEqual(len([l for l in products_file]), len(self.c.products))
        products_file.close()

    def test_customers(self):
        customers_file = open(os.path.join(self.base_path, "customers.txt"))
        self.assertEqual(len([l for l in customers_file]), len(self.c.customers) + 1)
        customers_file.close()
