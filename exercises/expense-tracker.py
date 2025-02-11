def main():
    expenses = []

    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        choice = float(input('Enter your choice: '))

        match choice:
            case 1:
                amount = float(input('Enter amount: '))
                category = input('Enter category: ')
                addExpense(expenses, amount, category)
            case 2:
                print('\nAll Expenses:')
                print_expenses(expenses)
            case 3:
                pass
            case 4:
                pass
            case 5:
                print('Exiting the Expense Tracker...')
                break


def addExpense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})


def print_expenses(expenses):
    for expense in expenses:
        print('Amount: ', expense["amount"], ', Category: ', expense["category"])


main()
