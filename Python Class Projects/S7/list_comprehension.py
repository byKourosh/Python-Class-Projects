order_list = ['mobile', 'mobile', 'speaker', 'speaker', 'monitor', 'monitor', 'monitor', 'mouse']

[print(product, order_list.count(product) * "*") for product in set(order_list)]