product_object1 = {
    "id": 1,
    "name": "Laptop",
    "category": "Electronics",
    "price": 750,
    "stock": 50,
    "supplier_email": "supplier1@gmail.com"
}

product_object2 = {
    "id": 2,
    "name": "Desk Chair",
    "category": "Furniture",
    "price": 100,
    "stock": 200,
    "supplier_email": "supplier2@gmail.com"
}

product_object3 = {
    "id": 3,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 200,
    "stock": 150,
    "supplier_email": "supplier3@gmail.com"
}

product_object4 = {
    "id": 4,
    "name": "Notebook",
    "category": "Stationery",
    "price": 5,
    "stock": 500,
    "supplier_email": "supplier4@gmail.com"
}

product_object5 = {
    "id": 5,
    "name": "Running Shoes",
    "category": "Apparel",
    "price": 80,
    "stock": 100,
    "supplier_email": "supplier5@gmail.com"
}

product_objects = [product_object1, product_object2, product_object3, product_object4, product_object5]

for product in product_objects:
    print(f"ID: {product.get('id')}, Name: {product.get('name')}, Category: {product.get('category')}, Price: {product.get('price')}, Stock: {product.get('stock')}, Email: {product.get('supplier_email')}")