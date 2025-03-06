class Category:
    def __init__(self, category_name):
        self.name = category_name
        self.value = 0
        self.ledger = []

    def __str__(self):
        str = self.name.center(30, '*')

        for item in self.ledger:
            description = item['description']
            if len(description) > 23:
                description = description[:23]

            amount = f"{item['amount']:.2f}".rjust(30 - len(description))
            line = '\n' + description + amount
            str += line

        str += '\n' + f"Total: {self.get_balance():.2f}"
        return str

    def _add_to_ledger(self, amount, description):
        self.ledger.append({'amount': amount, 'description': description})

    def check_funds(self, value):
        return False if value > self.value else True

    def deposit(self, value, description=''):
        self.value += value
        self._add_to_ledger(value, description)

    def withdraw(self, value, description=''):
        if not self.check_funds(value):
            return False

        self.value -= value
        self._add_to_ledger(-value, description)
        return True

    def get_balance(self):
        return self.value

    def transfer(self, value, category):
        withdraw_success = self.withdraw(value, f'Transfer to {category.name}')
        if not withdraw_success:
            return False

        category.deposit(value, f'Transfer from {self.name}')
        return True


def create_spend_chart(categories):
    spent = []
    for category in categories:
        category_spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                category_spent += abs(item["amount"])
        spent.append(category_spent)

    total = sum(spent)
    percentages = [int((s / total) * 100) // 10 * 10 for s in spent]

    string = 'Percentage spent by category\n'
    for i in range(100, -10, -10):
        string += str(i).rjust(3) + "| "
        for percentage in percentages:
            string += 'o  ' if percentage >= i else '   '
        string += '\n'

    string += '    ' + '-' * (len(categories) * 3 + 1) + '\n'
    names = [category.name for category in categories]
    max_length = max(len(name) for name in names)

    for i in range(max_length):
        string += '     '
        for name in names:
            string += name[i] + '  ' if i < len(name) else '   '
        if i < max_length - 1:
            string += '\n'

    return string


if __name__ == '__main__':
    test = Category('Test')
    test.deposit(1000, 'testing!!!!')
    test2 = Category('Test2')
    test.transfer(1000, test2)
    print(test)
    print(create_spend_chart([test, test2]))
