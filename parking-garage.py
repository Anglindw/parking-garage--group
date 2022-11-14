class Pgarage():

    def __init__(self):
        self.amount_of_tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Ashley
        self. parking_spaces = [False, False, False, False,
                                False, False, False, False, False, False]  # Ashley
        self.ticket_in_use = []
        self.currentTicket = {'paid': False}
        self.ticket_Taken = {'parked': False}

    def takeTicket(self):  # Ashley
        self.ticket_in_use.insert(0, self.amount_of_tickets.pop())
        self.ticket_in_use.sort()
        self.parking_spaces[self.ticket_in_use[0] - 1] = True
        self.ticket_Taken['parked'] = True
        self.currentTicket['paid'] = False
        print(f'You have ticket number {self.ticket_in_use[0]}.')

    def payforParking(self):
        ticket = input('What ticket would you like to pay for?')
        if ticket in self.ticket_in_use:

            payment = int(input(f"Hello the cost for parking is $20 dollars"))
            if payment >= 20:

                print(f'Ticket number {self.ticket_in_use[-1]} has been paid!')

                self.amount_of_tickets.append(self.ticket_in_use.pop())
                self.amount_of_tickets.sort()

                self.currentTicket['paid'] = True

        else:
            print(f'I am sorry that is not enough or not valid')
            self.currentTicket['paid'] = False

    def leaveGarage(self):  # Nick
        if self.currentTicket['paid'] == True:

            self.parking_spaces[self.ticket_in_use - 1] = False

            print('Thank you, have nice day!')
        elif self.currentTicket['paid'] == False:
            self.payforParking()
            self.parking_spaces[self.ticket_in_use - 1] = False
            print('Thank you, have nice day!')

    def runner(self):  # Ashley

        while True:
            user_ = input(
                'Welcome to my garage. Please start by taking a ticket. (take a ticket) ').lower()
            if user_ == 'take':
                self.takeTicket()
            elif user_ == 'pay' and self.ticket_Taken['parked'] == True:

                self.payforParking()
            elif user_ == 'leave' and self.ticket_Taken['parked'] == True:
                self.leaveGarage()
            else:
                print('I\'m sorry that is an invalid input. Please try again.')