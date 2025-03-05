class Category:
    def __init__(self, category_name):
        self.name = category_name
        self.value = 0
        self.ledger = []

    def _add_to_ledger(self, amount, description):
        self.ledger.append({'amount': amount, 'description': description})
        print(self.ledger)

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


def create_spend_chart(categories):
    pass


if __name__ == '__main__':
    test = Category('Test')
    test.deposit(1000)
    test.withdraw(500, 'withdraw')
    print(test.get_balance())
