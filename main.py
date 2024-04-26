from mod import *

car = Car()

while True:
    ans = input("Touch something! (Z/S) : ")
    ans.lower()

    # if ans == "z":
    #     car.accelerate()
    # elif ans == "s":
    #     car.brake()
    # elif ans == "gu":
    #     car.gear_up()
    # elif ans == "gd":
    #     car.gear_down()

    match ans:
        case "z":
            car.accelerate()
        case "s":
            car.brake()
        case "gu":
            car.gear_up()
        case "gd":
            car.gear_down()
