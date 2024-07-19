products = {
    'Milk': 1.9,
    'Bread': 2.5,
    'Eggs': 4.9,
    'Cheese': 14.4
}

TAX_RATE = 0.17

products_with_tax = {product: price * (1 + TAX_RATE) for product, price in products.items()}

print(products_with_tax)
