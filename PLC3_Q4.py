from collections import OrderedDict
import pickle
class Vehicle:
def __init__(self, reg_no, eng_no, model, type, mileage, vendor, owner_name):
self.reg_no = reg_no
self.eng_no = eng_no
self.model = model
self.type = type
self.mileage = mileage
self.vendor = vendor
self.owner_name = owner_name
@property
def details(self):
return f"REG NO: {self.reg_no}:\n\tENGINE NO: {self.eng_no}\n\tOWNER: {self.
21-805-0106: Python Programming Lab
class VehicleCollection:
def __init__(self):
self.vehicles = OrderedDict()
def add(self, vehicle):
self.vehicles[vehicle.reg_no] = vehicle
def delete(self, reg_no):
del self.vehicles[reg_no]
def modify(self, reg_no, attr, val):
setattr(self.vehicles[reg_no], attr, val)
def sort_by_mileage(self):
self.vehicles = OrderedDict(
sorted(self.vehicles.items(), key=lambda x: float(x[1].mileage))
)
def filter_by_attr(self, attr, val):
return [
vehicle.details
for vehicle in self.vehicles.values()
if getattr(vehicle, attr) == val
]
def display(self):
for reg_no in self.vehicles:
print(self.vehicles[reg_no].details)
print("****************************************
*************************")
if __name__ == "__main__":
vehicle_collection = VehicleCollection()
available_attrs = ["eng_no", "model", "type", "mileage", "vendor", "owner_name"]
21-805-0106: Python Programming Lab
while True:
ch = int(
input(
"1. Add vehicle\t2. Delete vehicle\t
3. Modify vehicle\t4.Filter vehicles\t
5. Display details\t6. Save collection\t
7.Load collection\t8. Sort vehicles by mileage
\t9. END\n>>> "
)
)
if ch == 1:
print("***************____ADD_VEHICLE____***************")
reg_no = input("Enter register no: ")
eng_no = input("Enter engine no: ")
model = input("Enter model: ")
type_ = input("Enter type: ")
mileage = input("Enter mileage: ")
vendor = input("Enter vendor name: ")
owner_name = input("Enter owner name: ")
vehicle_collection.add(
Vehicle(reg_no, eng_no, model, type_, mileage, vendor, owner_name)
)
elif ch == 2:
print("***************____DELETE_VEHICLE____***************")
reg_no = input("Enter register no: ")
vehicle_collection.delete(reg_no)
elif ch == 3:
print("***************____MODIFY_VEHICLE____***************")
while True:
reg_no = input("Enter register no: ")
if not vehicle_collection.vehicles.get(reg_no):
print("NO SUCH VEHICLE!")
continue
print("Available attributes:", available_attrs)
attr = input("Enter attribute to modify: ")
if attr not in available_attrs:
print("Invalid attribute!")
continue
21-805-0106: Python Programming Lab
val = input("Enter value of attribute: ")
vehicle_collection.modify(reg_no, attr, val)
break
elif ch == 4:
print("***************____FILTER_VEHICLES____***************")
while True:
print("Available attributes:", available_attrs)
attr = input("Enter attribute: ")
if attr not in available_attrs:
print("Invalid attribute!")
continue
val = input("Enter value of attribute: ")
res = vehicle_collection.filter_by_attr(attr, val)
for string in res:
print(string)
print(
"*******************************
**********************************"
)
break
elif ch == 5:
print("*************************____DETAILS____************
*************")
vehicle_collection.display()
elif ch == 6:
file_name = input("Enter pickle file name:")
with open(file_name, "wb") as f:
pickle.dump(vehicle_collection, f)
print(f"COLLECTION STORED IN {file_name}")
elif ch == 7:
file_name = input("Enter name of pickle file: ")
with open(file_name, "rb") as f:
vehicle_collection = pickle.load(f)
elif ch == 8:
vehicle_collection.sort_by_mileage()
vehicle_collection.display()
else:
	break