class Category:
    def __init__(self, category_name):
        self.name = category_name
        self.value = 0
        self.ledger = []

    def _add_to_ledger(self, amount, description):
        self.ledger.append({'amount': amount, 'description': description})

    def deposit(self, value, description=''):
        self.value += value
        self._add_to_ledger(value, description)

    def withdraw(self, value, description=''):
        if value > self.value:
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
    pass


if __name__ == '__main__':
    test = Category('Test')
    test.deposit(1000)
    test2 = Category('Test2')
    test.transfer(1000, test2)
    print(test.ledger)
    print(test2.ledger)
