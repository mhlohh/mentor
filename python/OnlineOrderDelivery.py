n_orders = int(input("Enter the Orders: "))

delivery_status_dict = {
    'Fast delivery' : 0,
    'Normal delivery' : 0,
    'Delayed delivery' : 0
}
for i in range(n_orders):
    days = int(input("Enter the number of days: "))

    if days <= 2:
        delivery_status_dict['Fast delivery'] += 1
    elif days >= 3 and days <= 5:
        delivery_status_dict['Normal delivery'] += 1
    elif days > 5:
        delivery_status_dict['Delayed delivery'] += 1

print(delivery_status_dict)
    