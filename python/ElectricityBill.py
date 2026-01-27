class consumers:
    def __init__(self,name,unit):
        self.name = name
        self.unit = unit
    bill = 0

consumer_list = []
unit_list = [2,3,5]
n_consumer = int(input("Enter the number of consumers: "))

for i in range(n_consumer):

    name = input("Enter the name: ")
    unit = int(input("Enter the unit: "))
    consumer = consumers(name,unit)

    if consumer.unit <= 100:

        consumer.bill = consumer.unit * unit_list[0]
        print(f"Bill :{consumer.bill}")
                                           
    elif consumer.unit >= 101 and consumer.unit <= 300:
        
        consumer.bill = consumer.unit * unit_list[1]
        print(f"Bill :{consumer.bill}")

    elif consumer.unit > 300:

        consumer.bill = consumer.unit * unit_list[2]
        print(f"Bill :{consumer.bill}")

    print()
    consumer_list.append(consumer)

for people in consumer_list:
    print(people.name)
    print(people.bill)
    print()
