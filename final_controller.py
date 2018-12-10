# @Author: HaoxuanLi  
# @Date 2018/12/9
# CWID: 10434197
from Utils.FileReader import FileReader
from domain.customer import Customer
from domain.inventory import Inventory
from domain.store import Store
from domain.transaction import Transaction
from domain.product import Product
import os
from prettytable import PrettyTable
from collections import defaultdict


class Final_controller:

    def __init__(self):
        self.transactions, self.stores, self.products, self.inventories, self.customers = [], {}, {}, {}, {}
        self.base_path = os.path.abspath("file_dir")
        self.read_customer(os.path.join(self.base_path, "customers.txt"), ",")
        self.read_product(os.path.join(self.base_path, "products.txt"), "|")
        self.read_store(os.path.join(self.base_path, "stores.txt"), "*")
        self.read_inventory(os.path.join(self.base_path, "inventory.txt"), "|")
        self.read_transaction(os.path.join(self.base_path, "transactions.txt"), "|")

    def read_customer(self, path: str, flag: str):
        header_list, attrs_list = FileReader.read_lines(path, flag, True)
        for attrs in attrs_list:
            customer = Customer(attrs[0], attrs[1])
            self.customers[customer.cust_id] = customer
        return header_list

    def read_inventory(self, path: str, flag: str):
        header_list, attrs_list = FileReader.read_lines(path, flag, True)
        for attrs in attrs_list:
            inventory = Inventory(attrs[0], attrs[1], attrs[2])
            self.inventories[inventory.store_id, inventory.product_id] = inventory
            self.products[inventory.product_id].num = inventory.quantity
        return header_list

    def read_product(self, path: str, flag: str):
        attrs_list = FileReader.read_lines(path, flag, False)
        for attrs in attrs_list:
            product = Product(attrs[0], attrs[1], attrs[2])
            self.products[product.product_id] = product

    def read_store(self, path: str, flag: str):
        header_list, attrs_list = FileReader.read_lines(path, flag, True)
        for attrs in attrs_list:
            store = Store(attrs[0], attrs[1])
            self.stores[store.id] = store
        return header_list

    def read_transaction(self, path: str, flag: str):
        header_list, attrs_list = FileReader.read_lines(path, flag, True)
        for attrs in attrs_list:
            transaction = Transaction(attrs[0], attrs[1], attrs[2], attrs[3])
            if int(self.products[transaction.product_id].num) - int(transaction.quantity) >= 0:
                self.products[transaction.product_id].num = str(
                    int(self.products[transaction.product_id].num) - int(transaction.quantity))
                self.transactions.append(transaction)
        return header_list

    def print_first_table(self):
        table1 = PrettyTable()
        table1.field_names = ["Store", "Product", "Customers", "Quantity"]

        for product in self.products.values():
            store = self.stores[product.store_id]
            transactions_temp = [transaction for transaction in self.transactions if
                                 transaction.product_id == product.product_id]
            customer_names = sorted([customer.name for customer in self.customers.values() if customer.cust_id in set(
                [transaction.cust_id for transaction in self.transactions if
                 transaction.product_id == product.product_id])])
            quant = 0
            for transaction in transactions_temp:
                quant += int(transaction.quantity)
            table1.add_row([store.name, product.description, customer_names, quant])
        print(table1.get_string())

    def print_second_table(self):
        table2 = PrettyTable()
        table2.field_names = ["Customer", "Product", "Quality Sold"]
        for customer in self.customers.values():
            num_dict = defaultdict(int)
            product_name = None
            for id in set([transaction.product_id for transaction in self.transactions if
                           customer.cust_id == transaction.cust_id]):
                count = 0
                for num in [transaction.quantity for transaction in self.transactions if
                            customer.cust_id == transaction.cust_id and transaction.product_id == id]:
                    count += int(num)

                table2.add_row([customer.name, self.products[id].description, count])

        print(table2.get_string())


f = Final_controller()
f.print_first_table()
f.print_second_table()
