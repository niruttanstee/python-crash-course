from lottery import Lottery
# You can use a loop to see how hard it might be to win the kind of lottery
# we just made. 

# Make a list or tuple called my_ticket. 
my_ticket = ['a', 4, 10, 'c', 2, 3]

# Write a loop that keeps pulling
# numbers until your ticket wins. Print a message reporting how many times the
# loop had to run to give you a winning ticket.

def pull_tickets(ticket):
    """
    Draws lottery ticket until the defined ticket is the winning ticket.
    When it is the winning ticket, prints message with the number of draws.
    """
    lottery = Lottery()
    count = 0
    win = False
    
    while not win:
        lottery_result = lottery.draw()
        print(lottery_result)
        if ticket == lottery_result:
            win = True
        else:
            count+= 1
    
    print("--- Winning ticket! ----")
    print(f"{lottery_result} == {ticket}")
    print(f"It took {count} draws to get the winning ticket.")

pull_tickets(my_ticket)



