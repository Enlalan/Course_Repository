# learn print,variables,type


print("Hello Dunia")
print()  # --> display empty space antara barisan
print("Today i feel great")
print()
print("Because i learn Python")
print()

# calculate area & circumference of c circle
# using an approximation for pi

pi = 355/133
radius = 2.2
area = pi*(radius**2)
circumference = pi*(radius*2)
print("Area =", area)  # --> 12.918796
print(circumference)  # --> 11.74426
print("Circumference =", int(circumference))  # --> 11
print(type(circumference))  # --> "float"
print()
# calculate area & circumference for variable radius to 4.5
radius = radius+2
print(int(radius))  # 4 "display new radius value as int"
print("Area =", int(area))
# 12 "tidak berubah sbb tiada arahan kira area yg baru"
print("Circumference =", int(circumference))
# 11 "tidak berubah sbb tiada arahan kira area yg baru"
print()
# reassign value pada variable "area" melalui new arahan kiraan
area = pi*(radius**2)
circumference = pi*(radius*2)
print(radius)  # --> 4.2
print("Area =", int(area))  # 47 "new value sbb ada arahan kiraan yg baru"
print("Circumference =", int(circumference))
# answ: 22 "new value sbb ada arahan kiraan yg baru"
print()
# maka value assigned pd variable name (dlm memory) tidak akn brubah selagi
# tidak re-assign atau tiada arahan kiraan baru
print()
