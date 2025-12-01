class ElectricityBillCalculator:
    def __init__(self, units):
        self.units = units
        self.slab1_rate = 3.50  
        self.slab2_rate = 4.50 
        self.slab3_rate = 6.00 

    def calculate_bill(self):
        units = self.units
        bill = 0.0
        if units <= 100:
            bill += units * self.slab1_rate
        else:
            bill += 100 * self.slab1_rate
            units -= 100
            if units <= 100:
                bill += units * self.slab2_rate
            else:
                bill += 100 * self.slab2_rate
                units -= 100
                bill += units * self.slab3_rate
        return bill


bill_1 = ElectricityBillCalculator(150)
print(f"Total bill: {bill_1.calculate_bill()}")

bill_2 = ElectricityBillCalculator(250)
print(f"Total bill: {bill_2.calculate_bill()}")

bill_3 = ElectricityBillCalculator(1050)
print(f"Total bill: {bill_3.calculate_bill()}")
