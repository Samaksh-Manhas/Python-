#Program to create a class with name Hp_Gaming_Laptop
#Define common features like processor("I9"), screen_width("15")
#color(Dark Black)
#Define function of class with name
#configration with parameters RAM, ROM, MotherBoard, GPU, SSD
#Create 4 different objects of this class that represents 4 different 
# models of this laptop series with name G1, G2, G3, G4

class Hp_Gaming_Laptop:
    processor="i9"
    screen_width=15
    color="Dark Black"
    
    def spec(self, ram, rom, motherboard, gpu, ssd):
        self.ram=ram
        self.rom=rom
        self.motherboard=motherboard
        self.gpu=gpu
        self.ssd=ssd
        print(f"Specifications: RAM: {ram}, ROM: {rom}, Motherboard: {motherboard}, GPU: {gpu}, SSD: {ssd}")

G1=Hp_Gaming_Laptop()
G2=Hp_Gaming_Laptop()
G3=Hp_Gaming_Laptop()
G4=Hp_Gaming_Laptop()

print("G1:",G1.processor, G1.screen_width, G1.color)
G1.spec("4GB", "64GB", "Intel", "RTX 2050", "256 GB")

print("G2:",G2.processor, G2.screen_width, G2.color)
G2.spec("6GB", "128GB", "Intel", "RTX 3050", "512 GB")

print("G3:",G3.processor, G3.screen_width, G3.color)
G3.spec("16GB", "256GB", "Intel", "RTX 3090", "1 TB")

print("G4:",G4.processor, G4.screen_width, G4.color)
G4.spec("32GB", "512GB", "Intel", "RTX 4050", "2 TB")