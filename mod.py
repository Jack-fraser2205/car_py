import time
import random


class Car:
    faster_ascii = """
            _-_-  _/\\______\\__
         _-_-__  /,-. -|-,-.`-.
            _-_- `( o )----( o )-'
                   `-'      `-' 
                   """

    slower_ascii = """
            _-_-  _/\\______\\__
                 /,-. -|-,-.`-.
            _-_- `( o )----( o )-'
                   `-'      `-'
                   """
    speed = 0
    gear = 1
    rand_int = 0
    play = True

    def random_num(self):
        self.rand_int = random.randint(0, 10)
        if self.rand_int > random.randint(0, 15):
            self.red_light()

    def delay(self):
        time.sleep(1)

    def red_light(self):
        print("RED LIGHT!")
        print("3...")
        self.delay()
        print("2...")
        self.delay()
        print("1...")
        self.delay()
        print("GO")
        self.accelerate()

    def check_speed(self):
        if self.speed == 0:
            return 0

    def check_gear_down(self):
        if self.gear <= 1:
            return 0

    def check_gear_up(self):
        if self.gear == 6:
            return 0

    def gear_up(self):
        if self.check_gear_up() == 0:
            print("You can't go further !")
        else:
            self.gear = self.gear + 1
            print(f"Gear : {self.gear}")
            self.random_num()

    def gear_down(self):
        if self.check_gear_down() == 0:
            print("You can't decrease further!")
        else:
            self.gear = self.gear - 1
            print(f"Gear : {self.gear}")
            self.random_num()

    def park(self):
        self.gear = 1
        self.speed = 0
        print("You succesfuly parked")
        self.play = False

    def accelerate(self):
        self.speed = self.speed + 10 * self.gear
        print(self.speed)
        print(self.faster_ascii)
        self.random_num()
        return self.speed

    def brake(self):
        if self.check_speed() == 0:
            print("You cant go slower! \n")
        else:
            self.speed = self.speed - 10
            print(self.speed)
            print(self.slower_ascii)
            self.random_num()
            return self.speed
