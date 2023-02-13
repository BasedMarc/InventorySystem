print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

print("Select first service:")
service1 = input()
print("Select second service:\n")
service2 = input()

print("Davy's auto shop invoice\n")

if service1 == "Oil change":
    print("Service 1: Oil change, $35")
    service1 = 35
elif service1 == "Tire rotation":
    print("Service 1: Tire rotation, $19")
    service1 = 19
elif service1 == "Car wash":
    print("Service 1: Car wash, $7")
    service1 = 7
elif service1 == "Car wax":
    print("Service 1: Car wax, $12")
    service1 = 12
elif service1 == "-":
    print("Service 1: No service")
    service1 = 0

if service2 == "Oil change":
    print("Service 2: Oil change, $35\n")
    service2 = 35
elif service2 == "Tire rotation":
    print("Service 2: Tire rotation, $19\n")
    service2 = 19
elif service2 == "Car wash":
    print("Service 2: Car wash, $7\n")
    service2 = 7
elif service2 == "Car wax":
    print("Service 2: Car wax, $12\n")
    service2 = 12
elif service2 == "-":
    print("Service 2: No service\n")
    service2 = 0

print("Total: ${}".format(service1 + service2))
