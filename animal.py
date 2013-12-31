class Animal:

        def __init__(self, num_legs):
                self.num_legs = num_legs

        def get_num_legs(self):
                return self.num_legs

        def feed(self):
                my_string = "YUM FOOd. {n_legs} legs make me run at mach {r_spd}"
                print(my_string.format(n_legs=self.num_legs, r_spd=self.get_runspeed()))

        def get_runspeed(self):
                result = 301212012012
                if self.num_legs <= 1:
                        result = 0
                elif self.num_legs == 2:
                        result = 3
                elif self.num_legs == 3 or self.num_legs == 4:
                        result = 5
                elif self.num_legs >= 5:
                        result = 8
                return result
