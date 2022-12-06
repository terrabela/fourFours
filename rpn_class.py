# From:
# https://www.geeksforgeeks.org/evaluate-the-value-of-an-arithmetic-expression-in-reverse-polish-notation-in-python/

# Python 3 code to evaluate reverse polish notation

# function to evaluate reverse polish notation

import itertools
from scipy.special import factorial


def evaluate_list(expression):
    # splitting expression at whitespaces
    # expression = expression.split()

    # stack
    stack = []

    # iterating expression
    for ele in expression:

        # ele is a number
        if ele not in '/*+-!^':
            stack.append(int(ele))
            # stack.append(ele)

        # ele is an operator
        else:
            # getting operands
            right = stack.pop()
            if ele == '!':
                left = ''
            else:
                left = stack.pop()

            # performing operation according to operator
            if ele == '+':
                stack.append(left + right)

            elif ele == '-':
                stack.append(left - right)

            elif ele == '*':
                stack.append(left * right)

            elif ele == '/':
                if right != 0:
                    stack.append(left / right)
                else:
                    stack.append(None)

            elif ele == '^':
                stack.append(left ** right)

            elif ele == '!':
                stack.append(factorial(right))

    # return final answer.
    return stack.pop()


def evaluate(expression):
    # splitting expression at whitespaces
    expression = expression.split()
    return evaluate_list(expression)


# input expression
arr = "10 6 9 3 + -11 * / * 17 + 5 +"
# arr = "4 ! -4 4 + 7 / ^"
# arr = "4 7 ^"
arrlist = arr.split()

# itera = itertools.permutations(arrlist)
# listaexpr = []
# for i in (itera):
#     listaexpr.append(i)
#     print(''.join(i))

# print(arrlist)
# print(f'comprimento: {len(listaexpr)}')
# print('É o fatorial do comprimento')

# outra jeito
# print('Combinations')
# itera = itertools.combinations('23279', 3)
# for i in itera:
#     print(i)

# print('Combinations with replacement')

# itera = itertools.combinations_with_replacement('23279', 3)
# for i in itera:
#     print(i)

arr1 = '4 4 4 4'
arr2 = '4 4 44'
arr3 = '4 444'
arr4 = '44 44'

operas = '+-*/^'


def is_list_valid(mixed):
    # The balance along the list must be > 0 for mixed to be evaluated
    balance = -1
    for ele in mixed:
        if ele in '/*+-!^':
            balance -= 1
        else:
            balance += 1
        if balance < 0:
            return balance
    return balance


itera3 = itertools.combinations_with_replacement(operas, 3)
for it in itera3:
    print(it)
    print(''.join(it))

seqs3 = []
listnum3 = ['4', '4', '44']
itera2 = itertools.combinations_with_replacement(operas, 2)
for it in itera2:
    listseq = listnum3 + list(it)
    seqs3.append(listseq)

all_lists_type_5 = []
for iseq in seqs3:
    iit = itertools.permutations(iseq)
    for iiit in iit:
        all_lists_type_5.append(list(iiit))


print('fim')
print(f'tamanho: {len(all_lists_type_5)}')

type_5_valid = []
for i in all_lists_type_5:
    if is_list_valid(i) == 0:
        type_5_valid.append(i)

print(len(type_5_valid))
for i in type_5_valid:
    print(f'{i} = {evaluate_list(i)}')


# 1800, pois 15 seqs operadores * 5! (=120) permutacoes das seqs mistas

# calling evaluate()
# answer = evaluate(arr)
# printing final value of the expression
# print(f"Value of given expression'{arr}' = {answer}")
# print(arrlist)
# print(is_list_valid(arrlist))
