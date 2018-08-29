#!/usr/bin/env python3
# Last modified: 2018-08-26 13:04:23
"""This is the Account module.

This module shows how to use dunder methods.
"""

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'lsieun' 

from functools import total_ordering

@total_ordering
class Account(object):
    """A simple account class"""

    def __init__(self, owner: str, amount: int = 0):
        """
        This is the constructor that let us create
        objects  from this class.
        """
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError('please use int for account')
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __repr__(self):
        return '{}({!r}, {!r})'.format(
            self.__class__.__name__, self.owner, self.amount)

    def __str__(self):
        return '{} of {} with starting amount: {}'.format(
            self.__class__.__name__, self.owner, self.amount)

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    def __reversed__(self):
        return self[::-1]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __add__(self, other):
        owner = "{}&{}".format(self.owner, other.owner)
        start_amount = self.amount + other.amount
        acc = Account(owner, start_amount)
        for t in list(self) + list(other):
            acc.add_transaction(t)
        return acc

    def __call__(self):
        print("Start amount: {}".format(self.amount))
        print("Transactions: ")
        for transaction in self:
            print("\t{}".format(transaction))
        print("\nBalance: {}".format(self.balance))


if __name__ == '__main__':
    acc = Account('bob', 10)
    print("="*20, "Print Section", "="*20)
    print(str(acc))
    print(acc)
    print(repr(acc))
    print("{}".format(acc))
    print("{!s}".format(acc))
    print("{!r}".format(acc))

    print("="*20, "len/getitem Section", "="*20)
    acc.add_transaction(20)
    acc.add_transaction(-10)
    acc.add_transaction(50)
    acc.add_transaction(-20)
    acc.add_transaction(30)
    print("balance: {}".format(acc.balance))

    print("len: {}".format(len(acc)))
    print("transaction list:")
    for t in acc:
        print("\t{}".format(t))
    print("acc[1] = {}".format(acc[1]))
    print("list of reversed: {}".format(list(reversed(acc))))


    print("="*20, "eq/lt", "="*20)
    acc2 = Account("tim", 100)
    acc2.add_transaction(20)
    acc2.add_transaction(40)
    print("acc.balance = {}".format(acc.balance))
    print("acc2.balance = {}".format(acc2.balance))
    print("acc2 > acc: {}".format(acc2 > acc))
    print("acc2 < acc: {}".format(acc2 < acc))
    print("acc2 == acc: {}".format(acc2 == acc))

    print("="*20, "add", "="*20)
    acc3 = acc2 + acc
    print("acc3: {!r}".format(acc3))
    print("acc3.amount = {}".format(acc3.amount))
    print("acc3.balance = {}".format(acc3.balance))
    print("acc3._transactions = {}".format(acc3._transactions))
    

    print("="*20, "call", "="*20)
    acc()
