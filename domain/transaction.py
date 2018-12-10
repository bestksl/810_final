# @Author: HaoxuanLi  
# @Date 2018/12/9
# CWID: 10434197


class Transaction:
    def __init__(self, cust_id, quantity, product_id, store_id):
        self.cust_id = cust_id
        self.quantity = quantity
        self.product_id = product_id
        self.store_id = store_id
