from dealer_classes import Motorcycle, Truck

vehicles_to_compare = list()

moto1 = Motorcycle("Honda CRF150R", 346.0, 5599.0, 100.0)
moto2 = Motorcycle("Harley-Davidson Touring", 63463.3, 10998.95, 120.0)
moto3 = Motorcycle("Suzuki Hayabusa", 27700.0, 8500, 110.0)

truck1 = Truck("Ford Maverick", 4559.2, 28500)
truck2 = Truck("Ford Ranger", 15839.9, 30590)
truck3 = Truck("Toyota Tacoma", 38930.5, 40990)

motorcycles = [moto1, moto2, moto3]
trucks = [truck1, truck2, truck3]
selected_list = ''

while True:
    while True:
        vehicle_choice = input("Choose a vehicle category (truck/motorcycle) >> ").lower()
        if 'moto' in vehicle_choice:
            vehicle_choice = 'motorcycle'
            break
        elif vehicle_choice == 'truck':
            break
        else:
            print("Please pick a valid vehicle category")

    if vehicle_choice == 'motorcycle':
        selected_list = 'moto'
        moto_number = 1
        for moto in motorcycles:
            print(f"{moto_number}. {Motorcycle.get_info(moto)}")
            moto_number += 1

    elif vehicle_choice == 'truck':
        selected_list = 'truck'
        truck_number = 1
        for truck in trucks:
            print(f"{truck_number}. {Truck.get_info(truck)}")
            truck_number += 1

    while True:
        add_vehicle = input("Would you like to add a vehicle to compare? (y/n) >> ")
        if add_vehicle != 'y':
            break
        print()
        vehicle_pick = int(input("Which vehicle would you like to add? >> ")) - 1
        print()
        if selected_list == 'moto' and 0 <= vehicle_pick <= len(motorcycles):
            vehicles_to_compare.append(motorcycles[vehicle_pick])
            print(f"{motorcycles[vehicle_pick].make} added!")
            motorcycles.pop(vehicle_pick)
            print()
            break
        elif selected_list == 'truck' and 0 <= vehicle_pick <= len(trucks):
            vehicles_to_compare.append(trucks[vehicle_pick])
            print(f"{trucks[vehicle_pick].make} added!")
            trucks.pop(vehicle_pick)
            print()
            break
        else:
            print("Please select a valid vehicle.")

    continue_pick = input("Would you like to look at more vehicles? (y/n) >> ")
    if continue_pick != 'y':
        break


print()
i_number = 1
for i in vehicles_to_compare:
    print(f"{i_number}. {i.get_info()}")
    i.make_noise()
    i_number += 1

print()
user_purchase = input("Would you like to purchase a vehicle? (y/n) >> ")
if user_purchase != 'y':
    print()
    print("Thank you! Goodbye.")
else:
    user_purchase = int(input("Please enter the vehicle number >> ")) - 1
    print()
    print(f"You chose the {vehicles_to_compare[user_purchase].make} at ${vehicles_to_compare[user_purchase].price}")
