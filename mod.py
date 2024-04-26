class Car:
    speed = 0
    gear = 1

    def check_speed(self):
        if self.speed == 0:
            return 0

    def gear_up(self):
        self.gear = self.gear + 1

    def gear_down(self):
        if self.gear == 0:
            print("You cant decrease")
        else:
            self.gear = self.gear - 1

    def accelerate(self):
        self.speed = self.speed + 10 * self.gear
        print(self.speed)
        return self.speed

    def brake(self):
        if self.check_speed() == 0:
            print("You cant go slower ! \n")
        else:
            self.speed = self.speed - 10
            print(self.speed)
            return self.speed
