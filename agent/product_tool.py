
PRODUCTS = [
    {
        "product_name": "Aspire Student 14",
        "category": "Laptop",
        "price": 42999,
        "ram": "8GB",
        "storage": "512GB SSD",
        "purpose": "Students and everyday productivity"
    },
    {
        "product_name": "ValueBook 15",
        "category": "Laptop",
        "price": 34999,
        "ram": "8GB",
        "storage": "256GB SSD",
        "purpose": "Basic home and student use"
    },
    {
        "product_name": "ProBook Business 14",
        "category": "Laptop",
        "price": 58999,
        "ram": "16GB",
        "storage": "512GB SSD",
        "purpose": "Business and office work"
    },
    {
        "product_name": "Creator 15",
        "category": "Laptop",
        "price": 74999,
        "ram": "16GB",
        "storage": "1TB SSD",
        "purpose": "Content creation and development"
    }
]


def get_product_details(max_price=50000, purpose="student"):
    """Return retail products within a price limit and matching a purpose."""
    purpose = purpose.lower()

    matching_products = [
        product for product in PRODUCTS
        if product["price"] <= max_price
        and (
            purpose in product["purpose"].lower()
            or purpose in product["product_name"].lower()
            or purpose == "all"
        )
    ]

    return matching_products
