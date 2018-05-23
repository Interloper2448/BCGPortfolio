def filterFloat(statement, low, high):
    while True:
        inp = float(input(statement))
        if inp <= low or inp > high:
            print("Entry must be greater than ", low, " and less than ", high)
        else:
            return inp

def filterInt(statement, low, high):
    while True:
        inp = int(input(statement))
        if inp <= low or inp > high:
            print("Entry must be greater than ",low," and less than ",high)
        else:
            return inp

