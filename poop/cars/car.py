class Car:
    wheels = 4 
    amount_of_cars=0
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year=year
        self.color=color
        self.for_sale=for_sale
        Car.amount_of_cars+=1

    def drive(self):
        print(f"You drive a {self.color} {self.model} from {self.year}")
