class Pgarage():

    def __init__(self):
       self.amount_of_tickets = [10] # Ashley
       self. parking_spaces = [10] # Ashley

    def takeTicket(self): # Ashley
        return ('Here is your ticket. Have a nice day!')   
        self.amount_of_tickets -= 1 
        self.parking_spaces -= 1 

    def payforParking(self): 
        pass

    def leaveGgarage(self):
        pass

    def runner(self): # Ashley
        user_ = input('Welcome to my garage. Please start by taking a ticket. (take a ticket) ').lower() 
        if user_ == 'take a ticket': 
            self.takeTicket() 
            self.payforParking()
            self.leaveGgarage()
        else: 
            print('I\'m sorry that is an invalid input. Please try again.') 

    