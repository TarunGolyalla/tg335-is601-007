class MyCalc:
    ans = 0

    def _is_float(self, val):
        try:
            val = float(val)
            return True
        except:
            return False

    def _is_int(self, val):
        try:
            val = int(val)
            return True
        except:
            return False

    def _as_number(self, val):
        if self._is_int(val):
            return int(val)
        elif self._is_float(val):
            return float(val)
        else:
            raise Exception("Not a number")

    def addition(self, num1, num2):
        if num1 == "ans":
            return self.addition(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1 + num2
        print(f"addition={self.ans}")
        return self.ans

    # UCID:tg335; Date:10/15/23
    # addition() : addition method have two variables num1 and num2.
    # if condition checks num1 value, whether it is 'ans' or not, if num1=='ans',it returns ans and num2 as variables
    # if num1 is not 'ans' ,it takes run time values as num1 and num2
    # num1 = self._as_number(num1) ,_as_number function checks  and read as int or float , later
    # num1 + num2 value stores in ans and then returns the value ans
    # ans which is defined in class will update

    def subtraction(self, num1, num2):
        if num1 == "ans":
            return self.subtraction(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1 - num2
        print(f"subtraction={self.ans}")
        return self.ans

    # UCID:tg335; Date:10/15/23
    # subtraction : subtraction method have two variables num1 and num2.
    # if condition checks num1 value, whether it is 'ans' or not, if num1=='ans',it returns ans and num2 as variables
    # if num1 is not 'ans' ,it takes run time values as num1 and num2
    # num1 = self._as_number(num1) ,_as_number function checks  and read as int or float , later
    # num1 - num2 value stores in ans and then returns the value ans
    # ans which is defined in class will update

    def multiplication(self, num1, num2):
        if num1 == "ans":
            return self.multiplication(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1 * num2
        print(f"multiplication={self.ans}")
        return self.ans

    # UCID:tg335; Date:10/15/23
    # multiplication : multiplication method have two variables num1 and num2.
    # if condition checks num1 value, whether it is 'ans' or not, if num1=='ans',it returns ans and num2 as variables
    # if num1 is not 'ans' ,it takes run time values as num1 and num2
    # num1 = self._as_number(num1) ,_as_number function checks  and read as int or float , later
    # num1 * num2 value stores in ans and then returns the value ans
    # ans which is defined in class will update

    def division(self, num1, num2):
        if num1 == "ans":
            return self.division(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            if num2 == 0:
                print("Can't divide by zero, sorry")
            else:
                self.ans = num1 / num2
                print(f"division={self.ans}")
        return self.ans
    # UCID:tg335; Date:10/15/23
    # division : division method have two variables num1 and num2.
    # if condition checks num1 value, whether it is 'ans' or not, if num1=='ans',it returns ans and num2 as variables
    # if num1 is not 'ans' ,it takes run time values as num1 and num2
    # num1 = self._as_number(num1) ,_as_number function checks  and read as int or float , later
    # another if condition checkes whether num2 is 0 or not, if zero it will print can't divide by zero if not it divides num1 and num2
    # num1 / num2 value stores in ans and then returns the value ans
    # ans which is defined in class will update


if __name__ == '__main__':
    is_running = True
    iSTR = input("Are you ready:")
    res = 0
    Calc = MyCalc()
    if iSTR == "yes":
        while is_running:
            iSTR = input("What is your eq:")
            if iSTR == "quit" or iSTR == "q":
                is_running = False
            else:
                print("Your eq was " + str(iSTR))
                checks = ["+", "*", "//", "/", "", "x", "-", "%"]
                handled = False
                for check in checks:
                    if not handled and check in iSTR:
                        if "+" in check:
                            nums = iSTR.split("+")
                            res = Calc.addition(nums[0].strip(), nums[1].strip())
                        elif "/" in check:
                            nums = iSTR.split("/")
                            res = Calc.division(nums[0].strip(), nums[1].strip())
                        elif "*" in check:
                            nums = iSTR.split("*")
                            res = Calc.multiplication(nums[0].strip(), nums[1].strip())
                        elif "-" in check:
                            nums = iSTR.split("-")
                            res = Calc.subtraction(nums[0].strip(), nums[1].strip())

else:
    print("Good bye")
    is_running = False