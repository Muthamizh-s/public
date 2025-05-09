import json

# Add customer details
def add_customer():
    try:
        file = open("customers.json", "r")
        customers = json.load(file)
        file.close()
    except:
        customers = []

    while True:
        name = input("Enter customer name: ")
        phone = input("Enter phone number: ")
        address = input("Enter address: ")
        customer = {"name": name, "phone": phone, "address": address}
        customers.append(customer)

        again = input("Do you want to add another customer? (yes or no): ")
        if again.lower() != "yes":
            break

    file = open("customers.json", "w")
    json.dump(customers, file, indent=4)
    file.close()
    print("Customer details saved.")

# Most common address
def most_common_address():
    try:
        file = open("customers.json", "r")
        customers = json.load(file)
        file.close()
    except:
        print("Customer file not found.")
        return

    addresses = []
    for customer in customers:
        addresses.append(customer["address"])

    if len(addresses) == 0:
        print("No addresses found.")
        return

    most = ""
    most_count = 0
    for i in addresses:
        count = 0
        for j in addresses:
            if i == j:
                count = count + 1
        if count > most_count:
            most_count = count
            most = i

    print("Most common address is:", most)
    print("Used", most_count, "times")

add_customer()
most_common_address()
