from enum import Enum
import sys
from PumpkinMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, NeedsCleaningException, OutOfStockException
from PumpkinMachineExceptions import InvalidPaymentException


class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity=10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost
        self.total_cost = 0

    def get_total_cost(self):
        return self.total_cost

    def use(self):
        self.quantity -= 1
        if (self.quantity < 0):
            raise OutOfStockException
        return self.quantity

    def in_stock(self):
        return self.quantity > 0

    def __repr__(self) -> str:
        return self.name


class Pumpkin(Usable):
    pass


class FaceStencil(Usable):
    pass


class Extra(Usable):
    pass


class STAGE(Enum):
    Pumpkin = 1
    FaceStencil = 2
    Extra = 3
    Pay = 4


class PumpkinMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 2
    MAX_STENCILS = 3
    MAX_EXTRAS = 3
    def __init__(self):
        self.pumpkins = [Pumpkin(name="Mini Pumpkin", cost=1),
                    Pumpkin(name="Small Pumpkin", cost=2),
                    Pumpkin(name="Medium Pumpkin", cost=2.5),
                    Pumpkin(name="Large Pumpkin", cost=3)]
        self.face_stencils = [FaceStencil(name="Happy Face", quantity=10, cost=1),
                        FaceStencil(name="Scream Face", quantity=10, cost=1),
                        FaceStencil(name="Toothy Face", quantity=10, cost=1),
                        FaceStencil(name="Spooky Face", quantity=1, cost=1)]
        self.extras = [Extra(name="Small Candle", quantity=10, cost=.25),
                Extra(name="LED Candle", quantity=1, cost=.25),
                Extra(name="Spooky Sound Effects", quantity=10, cost=1.25),
                Extra(name="Sticker Pack", quantity=10, cost=1.00),
                Extra(name="Paint Kit", quantity=10, cost=3),
                Extra(name="Dry Ice", quantity=10, cost=.25),
                Extra(name="Googly Eyes", quantity=10, cost=.25),
                Extra(name="Glitter", quantity=10, cost=.25)]

        # variables
        self.remaining_uses = PumpkinMachine.USES_UNTIL_CLEANING
        self.remaining_stencils = PumpkinMachine.MAX_STENCILS
        self.remaining_extras = PumpkinMachine.MAX_EXTRAS
        self.total_sales = 0
        self.total_products = 0
        self.sales = 0.0

        self.inprogress_pumpkin = []
        self.currently_selecting = STAGE.Pumpkin

    # rules
    # 1 - pumpkin must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - face stencils can't exceed max
    # 4 - extras can't exceed max
    # 5 - proper cost must be calculated and shown to the user
    # 6 - cleaning must be done after certain number of uses before any more things can be made
    # 7 - total sales should calculate properly based on cost calculation
    # 8 - total_products should increment properly after a payment

    def pick_pumpkin(self, choice):
        if self.currently_selecting != STAGE.Pumpkin:
            raise InvalidStageException
        for c in self.pumpkins:
            if c.name.lower() == choice.lower():
                c.use()
                self.inprogress_pumpkin.append(c)
                return
        raise InvalidChoiceException

    def pick_face_stencil(self, choice):
        if self.currently_selecting != STAGE.FaceStencil:
            raise InvalidStageException
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_stencils <= 0:
            raise ExceededRemainingChoicesException
        for f in self.face_stencils:
            if f.name.lower() == choice.lower():
                f.use()
                self.inprogress_pumpkin.append(f)
                self.remaining_stencils -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException

    def pick_extras(self, choice):
        if self.currently_selecting != STAGE.Extra:
            raise InvalidStageException
        if self.remaining_extras <= 0:
            raise ExceededRemainingChoicesException
        for t in self.extras:
            if t.name.lower() == choice.lower():
                t.use()
                self.inprogress_pumpkin.append(t)
                self.remaining_extras -= 1
                return
        raise InvalidChoiceException

    def reset(self):
        """Called when a pumpkin is complete"""
        self.remaining_stencils = self.MAX_STENCILS
        self.remaining_extras = self.MAX_EXTRAS
        self.inprogress_pumpkin = []
        self.currently_selecting = STAGE.Pumpkin

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING

    def handle_pumpkin_choice(self, _pumpkin):
        self.pick_pumpkin(_pumpkin)
        self.currently_selecting = STAGE.FaceStencil

    def handle_face_stencil_choice(self, _face_stencil):
        if _face_stencil == "next":
            self.currently_selecting = STAGE.Extra
        else:
            self.pick_face_stencil(_face_stencil)

    def handle_extra_choice(self, _extra):
        if _extra == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_extras(_extra)
    # UCID: tg335
    # Date : 23-10-2023
    # def handle_pay(self, expected, total):
    #     if self.currently_selecting != STAGE.Pay:
    #         raise InvalidStageException
    #
    #     # Removing the dollar sign and converting the user input to a float
    #     try:
    #         self.total_sales += self.inprogress_pumpkin[0].get_total_cost()
    #         total_as_float = float(str(total).replace("$", ""))
    #     except ValueError:
    #         raise InvalidPaymentException("Invalid payment format.")
    #
    #     # Using a threshold for float comparison
    #     threshold = 0.01  # 1 cent
    #     if abs(expected - total_as_float) < threshold:
    #         print("Thank you! Enjoy your Pumpkin and Happy Halloween!")
    #         self.total_products += 1
    #         #self.total_sales += expected
    #         self.reset()
    #     else:
    #         raise InvalidPaymentException("Incorrect payment! Please enter the exact value.")
    #
    def print_current_pumpkin(self):
        print(
            f"Current Pumpkin: {','.join([x.name for x in self.inprogress_pumpkin])}")
    def handle_pay(self, expected, total):
        if self.currently_selecting != STAGE.Pay:
            raise InvalidStageException

        # Removing the dollar sign and converting the user input to a float
        try:
            total_as_float = float(str(total).replace("$", ""))
        except ValueError:
            raise InvalidPaymentException("Invalid payment format.")

        # Using a threshold for float comparison
        threshold = 0.01  # 1 cent
        if abs(expected - total_as_float) < threshold:
            print("Thank you! Enjoy your Pumpkin and Happy Halloween!")
            self.total_products += 1
            self.total_sales += self.inprogress_pumpkin[0].get_total_cost()  # Adding the cost of the current pumpkin to the total sales
            self.reset()
        else:
            raise InvalidPaymentException("Incorrect payment! Please enter the exact value.")

    def calculate_cost(self):
        # Calculate the total cost
        total = sum([item.cost for item in self.inprogress_pumpkin])
        # Set the total cost for the in-progress pumpkin
        self.inprogress_pumpkin[0].total_cost = total
        return total
        # tg335 ---- 23-10-2023


    def run(self):
        try:
            if self.currently_selecting == STAGE.Pumpkin:
                pumpkin = input(
                    f"What type of pumpkin would you like {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.pumpkins))))}?\n")
                self.handle_pumpkin_choice(pumpkin)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.FaceStencil:
                stencil = input(
                    f"What type of face stencil would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.face_stencils))))}? Or type next.\n")
                self.handle_face_stencil_choice(stencil)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.Extra:
                extra = input(
                    f"What extras would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.extras))))}? Or type done.\n")
                self.handle_extra_choice(extra)
                self.print_current_pumpkin()
            elif self.currently_selecting == STAGE.Pay:
                expected = self.calculate_cost()
                # TODO show expected value as currency format
                # TODO require total to be entered as currency format
                total = input(f"Your total is ${expected:.2f}, please enter the exact value.\n")
                self.handle_pay(expected, float(total))

                choice = input("What would you like to do? (order or quit)\n")
                if choice == "quit":
                    # exit() in recursive functions creates stackoverflow
                    # use return 1 to exit
                    print("Quitting the pumpkin machine")
                    return 1
        except KeyboardInterrupt:
            # quit
            print("Quitting the pumpkin machine")
            sys.exit()
        # UCID: tg335
        # Date : 23-10-2023
        # TODO items below
        # Note: Stage/category refers to the enum towards the top. Make sure error messages are very clear to the user
        # handle OutOfStockException
        # show an appropriate message of what stage/category was out of stock
        except OutOfStockException:
            print("Sorry, one of the items you chose is out of stock. Please choose another.")
        # handle NeedsCleaningException
        # prompt user to type "clean" to trigger clean_machine()
        # any other input is ignored
        # print a message whether or not the machine was cleaned
        # UCID: bs643
        # Date : 21-10-2023
        except NeedsCleaningException:
            choice = input("The machine needs cleaning. Type 'clean' to proceed.")
            if choice.lower() == "clean":
                self.clean_machine()
                print("The machine is cleaned and ready!")
            else:
                print("Machine wasn't cleaned, proceeding can damage the machine!")
        # handle InvalidChoiceException
            # show an appropriate message of what stage/category was the invalid choice was in
        except InvalidChoiceException:         # UCID: bs643, Date : 21-10-2023
            print(f"Invalid choice in the {self.currently_selecting.name} category!")
        # handle ExceededRemainingChoicesException
            # show an appropriate message of which stage/category was exceeded
            # move to the next stage/category
        except ExceededRemainingChoicesException: # UCID: bs643, Date : 21-10-2023
            print(
                f"You have exceeded the max number of choices for {self.currently_selecting.name}. Moving to next stage!")
            # I'd recommend adding a condition to handle if you're already in the Pay stage, just for safety
            if self.currently_selecting == STAGE.FaceStencil:
                self.currently_selecting = STAGE.Extra
            elif self.currently_selecting == STAGE.Extra:
                self.currently_selecting = STAGE.Pay
            elif self.currently_selecting == STAGE.Pay:
                print("You have completed your order. Please restart if you want to order again.")
                return  # Exit the run function
        # UCID: tg335
        # Date : 23-10-2023
        # handle InvalidPaymentException
            # show an appropriate message
        except InvalidPaymentException:
            print("Incorrect payment! Please enter the exact value.")
        except Exception as e:
            # this is a default catch all, follow the steps above
            print(f"Something went wrong and I didn't handle it: {e}")

        self.run()

    def start(self):
        self.run()


if __name__ == "__main__":
    pm = PumpkinMachine()
    pm.start()