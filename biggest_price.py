class Dealer:
    def __init__(self,company,model,price):
        self.company=company
        self.model=model
        self.price=price

class company(Dealer):
    def __init__(self,company,model,price):
        super().__init__(company,model,price)

    def massage(self):
        print('Good bye!')

car=company('Toyota','camery',120000)
T1=Dealer('Toyota','Hilux',800000)

H1=Dealer('hyundai','Azera',200000)
H2=Dealer('hyundai','Elantra',125000)

N1=Dealer('Nissan','Maxima',175000)
N2=Dealer('Nissan','Altima',300000)

T_All=T1.price+T2.price
H_All=H1.price+H2.price
N_All=N1.price+N2.price

print('--------------------------------------------------')
print('1st: ',T1.company)
print(f"{T1.model}:${T1.price}")
print(f"{T2.model}:${T2.price}")



