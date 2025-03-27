from car import Car

car1 = Car('BMW',2023,"BLACK",False)
car2 = Car('SKODA',2025,"SILVER",True)

print(car1.model)
car1.drive()
car2.drive()
print(Car.amount_of_cars)