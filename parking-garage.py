class Pgarage():

    def __init__(self):
        self.amount_of_tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Ashley
        self. parking_spaces = [False, False, False, False,
                                False, False, False, False, False, False]  # Ashley
        self.ticket_in_use = []
        self.currentTicket = {'paid': False}
        self.ticket_Taken = {'parked': False}
        self.ticket = 0

    def takeTicket(self):  # Ashley
        try:
            self.ticket_in_use.insert(0, self.amount_of_tickets.pop())
            # self.ticket_in_use.sort()
            self.parking_spaces[self.ticket_in_use[0] - 1] = True
            self.ticket_Taken['parked'] = True
            self.currentTicket['paid'] = False
            print(f'You have ticket number {self.ticket_in_use[0]}.')
        except:
            print('Sorry, there are no more parking spots available.')

    def payforParking(self):
        self.ticket = input('What ticket would you like to pay for?\n')
        if int(self.ticket) in self.ticket_in_use:
    
            
            payment = int(input(f"The cost for parking is $20 dollars.\n"))
            if payment >= 20 :


                print(f'Ticket number {self.ticket} has been paid!')

                self.amount_of_tickets.append(int(self.ticket))
                self.amount_of_tickets.sort()

                self.currentTicket['paid'] = True

            else:
                print(f'I am sorry that is not enough or not valid')
                self.currentTicket['paid'] = False
        else:
            print(f'I am sorry that is not a valid ticket number')

    def leaveGarage(self):  # Nick
        if self.currentTicket['paid'] == True:

            self.parking_spaces[int(self.ticket) - 1] = False

            self.currentTicket['paid'] = False
            print('Thank you, have nice day!')

        elif self.currentTicket['paid'] == False:
            print('You have to pay first!')
            self.payforParking()
            self.currentTicket['paid'] = False

        
            print('Thank you, have nice day!')
            self.parking_spaces[int(self.ticket) - 1] = False

    def runner(self):  # Ashley

        while True:
            user_ = input(
                'Welcome to my garage. T for ticket, P to pay, L to leave, and Q to quit.\n').lower()
            if user_.upper() != 'Q':
                if user_ == 't':
                    self.takeTicket()
                elif user_ == 'p' and self.ticket_Taken['parked'] == True:

                    self.payforParking()
                elif user_ == 'l' and self.ticket_Taken['parked'] == True:
                    self.leaveGarage()
                else:
                    print('I\'m sorry that is an invalid input. Please try again.')
            else:
                break


test = Pgarage()

test.runner()
