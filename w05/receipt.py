import csv
from datetime import datetime

def read_dictionary(file_path):
    dictionary = {}
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                product_id = row[0]
                product_info = row[1:]
                dictionary[product_id] = product_info
    except FileNotFoundError:
        print("Error: missing file")
    return dictionary

def process_order(products_dict, order_file):
    items = []
    total_items = 0
    subtotal = 0.0

    try:
        with open(order_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                product_id = row[0]
                quantity = int(row[1])

                try:
                    product_info = products_dict[product_id]
                    product_name = product_info[0]
                    product_price = float(product_info[1])

                    # Get the current day of the week
                    current_day = datetime.now().weekday()

                    # Check if today is Tuesday (1) or Wednesday (2)
                    if current_day == 1 or current_day == 2:
                        # Apply a 10% discount
                        product_price *= 0.9

                    item_total = product_price * quantity

                    items.append(f"{quantity} {product_name}: {quantity} @ {product_price:.2f}")
                    total_items += quantity
                    subtotal += item_total
                except KeyError:
                    print(f"Error: unknown product ID in the {order_file} file")
                    print(f"'{product_id}'")
    except FileNotFoundError:
        print("Error: missing file")

    return items, total_items, subtotal

def print_receipt(store_name, items, total_items, subtotal):
    sales_tax_rate = 0.06
    sales_tax = subtotal * sales_tax_rate
    total = subtotal + sales_tax

    print()
    print(store_name)
    print()
    for item in items:
        print(item)
    print()
    print(f"Number of Items: {total_items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")
    print()
    print("Thank you for shopping at the Inkom Emporium")
    print(datetime.now().strftime("%a %b %d %H:%M:%S %Y"))
    print()

def main():
    store_name = "Inkom Emporium"
    products_file = r"C:\Users\DANIEL ESPITIA\Documents\cse111\w05\products.csv"
    order_file = r"C:\Users\DANIEL ESPITIA\Documents\cse111\w05\request.csv"

    products_dict = read_dictionary(products_file)
    items, total_items, subtotal = process_order(products_dict, order_file)
    print_receipt(store_name, items, total_items, subtotal)

if __name__ == "__main__":
    main()