products = [
    {
        "id": 1,
        "name": "s22",
        "price": 450,
        "quantity": 3,
    },
    {
        "id": 2,
        "name": "s23",
        "price": 550,
        "quantity": 2,
    },
    {
        "id": 3,
        "name": "s24",
        "price": 650,
        "quantity": 8,
    }
]


          
# 1. Jami qiymat
def total_amount(products: list[dict[str, int | str]]) -> float | int:
    total = 0
    for product in products:
        total += product['price'] * product['quantity']

    return total

# 2. Eng qimmat product
def get_max_product(products: list[dict[str, int | str]]) -> dict[str, int | str] | None:
    if not products:
        return None
    
    max_product = products[0]
    for product in products:
        if product['price'] > max_product['price']:
            max_product = product

    return max_product

# 3. O'rtacha narx
def get_avg_price(products: list[dict[str, int | str]]) -> float | int:
    total = 0
    for product in products:
        total += product['price']

    avg = total / len(products)
    return avg

avg = get_avg_price(products)
print(avg)