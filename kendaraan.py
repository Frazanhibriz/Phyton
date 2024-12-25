class Kendaraan:
    def __init__(self, owner, noPlat, tahun):
        self.owner = owner
        self.noPlat = noPlat
        self.tahun = tahun
    
    def hitungServiceCost(self):
        raise NotImplementedError("Harus di implementasikan pada subclassnya")
    
    def printInfo(self):
        print(f"Owner: {self.owner}, No. Kendaraan: {self.noPlat}, Tahun Rilis: {self.tahun}")
        
                
class Car(Kendaraan):
    def __init__(self, owner, noPlat, tahun, jumlahPintu):
        super().__init__(owner, noPlat, tahun)
        self.jumlahPintu = jumlahPintu
        
    def hitungServiceCost(self):
        return (((self.tahun % 10) + self.jumlahPintu) * 100000)
    
   
class Motorcycle(Kendaraan):
    def __init__(self, owner, noPlat, tahun, kapasitasMesin):
        super().__init__(owner, noPlat, tahun)
        self.kapasitasMesin = kapasitasMesin
    
    def hitungServiceCost(self):
        return ((self.kapasitasMesin // 100) * 50000)
  
      
class Truck(Kendaraan): 
    def __init__(self, owner, noPlat, tahun, kapasitasMuatan):
        super().__init__(owner, noPlat, tahun)
        self.kapasitasMuatan = kapasitasMuatan
    
    def hitungServiceCost(self):
        return (self.kapasitasMuatan * 300000)
    
 
def  printServiceDetails(Vehicles: list[Kendaraan]):
    for vehicle in Vehicles:
        vehicle.printInfo()
        print(f"Service Cost: Rp. {vehicle.hitungServiceCost()}")
        print("---------------------------------------------------------------------------------------")


car = Car("John Doe", "B1234XYZ", 2015, 4)
motorcycle = Motorcycle("Jane Smith", "D5678ABC", 2020, 150)
truck = Truck("James Brown", "F91011JKL", 2018, 5)

Vehicles = [car, motorcycle, truck]

printServiceDetails(Vehicles)
