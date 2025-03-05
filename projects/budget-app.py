class Category:
    def __init__(self, category_name):
        self.name = category_name
        self.value = 0
        self.ledger = []

    def _add_to_ledger(self, amount, description):
        self.ledger.append({'amount': amount, 'description': description})
        print(self.ledger)

    def deposit(self, value):
        self.value += value
        self._add_to_ledger(value, 'deposit')

    def withdraw(self, value):
        if value > self.value:
            return False

        self.value -= value
        self._add_to_ledger(-value, 'withdraw')
        return True

    def get_balance(self):
        return self.value


def create_spend_chart(categories):
    pass


if __name__ == '__main__':
    test = Category('Test')
    test.deposit(1000)
    test.withdraw(500)
    print(test.get_balance())
