from mod import *

car = Car()

while car.play:
    ans = input("Touch something! : ")
    ans = ans.lower()

    match ans:
        case "z":
            car.accelerate()
        case "s":
            car.brake()
        case "gu":
            car.gear_up()
        case "gd":
            car.gear_down()
        case "p":
            car.park()
