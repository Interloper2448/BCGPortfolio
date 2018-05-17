#!/usr/bin/env python3

from datetime import datetime, timedelta, date

def get_invoice_date():
    while True:
        try:
            invoice_date_str = input("Enter the invoice date (MM/DD/YYYY): ")    
            invoice_date = datetime.strptime(invoice_date_str, "%m/%d/%Y")
            if invoice_date >= datetime.now():
                raise ValueError
            return invoice_date
        except ValueError:
            print("You must enter a valid date")
            continue

def main():
    print("The Invoice Due Date program")
    print()

    while True:
        invoice_date = get_invoice_date()
        print()

        # calculate due date and days overdue
        holder = invoice_date + timedelta(days=30)
        due_date = date(holder.year,holder.month,holder.day)
        holder = datetime.now()
        current_date = date(holder.year,holder.month,holder.day)
        days_overdue = (current_date - due_date).days
        # days_overdue = date(holder.year, holder.month, holder.day)

        # display results
        print("Invoice Date: " + invoice_date.strftime("%B %d, %Y"))
        print("Due Date:     " + due_date.strftime("%B %d, %Y"))
        print("Current Date: " + current_date.strftime("%B %d, %Y"))
        if days_overdue > 0:
            print("This invoice is", days_overdue, "day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print("This invoice is due in", days_due, "day(s).")
        print()

        # ask if user wants to continue
        result = input("Continue? (y/n): ")
        print()
        if result.lower() != "y":
            print("Bye!")
            break      

if __name__ == "__main__":
    main()
