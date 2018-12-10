# @Author: HaoxuanLi  
# @Date 2018/12/9
# CWID: 10434197

# product_id, the store_id where the product is sold, and a description of the item sold.


class Product:
    def __init__(self, product_id: str, store_id: str, description: str):
        self.product_id = product_id
        self.store_id = store_id
        self.description = description
        self.num = 0
