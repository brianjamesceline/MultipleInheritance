from app import Resident

resident = Resident(name='Jennifer', age= '28', id=23)

resident.print_name()
resident.print_age()
resident.print_id()

resident.title()

# mro is method resolution order and this tells you the order of things getting called
# print(Resident.__mro__)
# This can also be called directly
print(Resident.mro())
