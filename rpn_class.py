# From:
# https://www.geeksforgeeks.org/evaluate-the-value-of-an-arithmetic-expression-in-reverse-polish-notation-in-python/

# Python 3 code to evaluate reverse polish notation

# function to evaluate reverse polish notation

import itertools
import numpy as np
from scipy.special import factorial


def evaluate_list(expression):
    # for expression already given as a list
    # stack
    stack = []

    # iterating expression
    for ele in expression:

        # ele is a number
        if ele not in '/*+-^!r':
            stack.append(float(ele))

        # ele is an operator
        else:
            # getting operands
            right = stack.pop()
            if ele in '!r':
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
                    stack.append(float('inf'))

            elif ele == '^':
                if right < 100:
                    stack.append(left ** right)
                else:
                    stack.append(float('inf'))

            elif ele == '!':
                if right < 100:
                    stack.append(factorial(right))
                else:
                    stack.append(float('inf'))

            elif ele == 'r':
                if right > 0:
                    stack.append(np.sqrt(right))
                else:
                    stack.append(float('-inf'))

    # return final answer.
    return stack.pop()


def evaluate(expression):
    # splitting expression at whitespaces
    return evaluate_list(expression.split())


def decode_string(str):
    li = []
    for ch in str:
        if ch == 'q':
            li.append('44')
        else:
            li.append(ch)
    return li


str_4444 = '4444'
str_44q = '44q'
str_qq = 'qq'

operas_5 = '+-*/^'


def is_list_valid(mixed):
    # The balance along the list must be > 0 for mixed to be evaluated
    balance = -1
    for ele in mixed:
        if ele in '/*+-^':
            balance -= 1
        elif ele in '!r':
            pass
        else:
            balance += 1
        if balance < 0:
            return balance
    return balance


def make_operands_set(operas, n_opers, with_fact=False, with_sqrt=False):
    itera_n = itertools.combinations_with_replacement(operas, n_opers)
    ini_set = []
    for it in itera_n:
        ini_set.append(''.join(it))
    added_set = list(ini_set)
    if with_fact:
        added_set = [i + '!' for i in added_set]
    if with_sqrt:
        added_set = [i + 'r' for i in added_set]
    return added_set


def make_rpn_seqs(numbers_str, oper_set):
    all_lists_type_2n1 = []
    eles = [numbers_str + i for i in oper_set]
    for iseq in eles:
        iit = itertools.permutations(iseq)
        for i_iit in iit:
            all_lists_type_2n1.append(''.join(i_iit))
    return all_lists_type_2n1


def make_a_values_dict(operas, n_token_opers, str_numbers, with_fact=False, with_sqrt=False):
    list_opers_n = make_operands_set(operas, n_token_opers, with_fact, with_sqrt)
    make_rpn_seqs(str_numbers, list_opers_n)
    all_lists_type_2n1 = make_rpn_seqs(str_numbers, list_opers_n)

    print('fim')
    print(f'tamanho all_lists_type_2n1: {len(all_lists_type_2n1)}')
    print(f'Observar que é 35*7! = {35 * 7 * 6 * 5 * 4 * 3 * 2}')
    print(f'ou é 15*5! = {15 * 5 * 4 * 3 * 2}')

    # 176400, pois 15 seqs operadores * 5! (=120) permutacoes das seqs mistas

    type_n_valid = []
    for i in all_lists_type_2n1:
        if is_list_valid(i) == 0:
            type_n_valid.append(i)

    print(f'tamanho type_n_valid: {len(type_n_valid)}')

    dict_type_n = {}

    cont = 0
    for cand_key in type_n_valid:
        if cand_key not in dict_type_n:
            cont += 1
            # print(cont)
            li_to_eval = decode_string(cand_key)
            value = evaluate_list(li_to_eval)
            # print(f'{li_to_eval} = {value}')
            dict_type_n[cand_key] = value

    return dict_type_n


def sorting_dict(dict_n, print_range):
    # Print dict ordered by values, not keys!
    # https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/

    keys = list(dict_n.keys())
    values = list(dict_n.values())
    sorted_value_index = np.argsort(values)
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

    for i in sorted_dict:
        if print_range[0] <= sorted_dict.get(i) <= print_range[1]:
            print(i, sorted_dict.get(i))
    return sorted_dict

faixa = [92,95]

print('========================')
dict_type_7 = make_a_values_dict(operas=operas_5, n_token_opers=3, str_numbers=str_4444)
print('========================')
dict_type_5 = make_a_values_dict(operas=operas_5, n_token_opers=2, str_numbers=str_44q)
print('========================')
sorting_dict(dict_type_7, faixa)
print('========================')
sorting_dict(dict_type_5, faixa)

print('========================')
dict_type_5_fa = make_a_values_dict(operas=operas_5, n_token_opers=2, str_numbers=str_44q,
                                    with_fact=True)
print('========================')
sorting_dict(dict_type_5_fa, faixa)
print('========================')
dict_type_5_sqr = make_a_values_dict(operas=operas_5, n_token_opers=2, str_numbers=str_44q,
                                     with_sqrt=True)
print('========================')
sorting_dict(dict_type_5_sqr, faixa)

print('========================')
dict_type_7_fa = make_a_values_dict(operas=operas_5, n_token_opers=3, str_numbers=str_4444,
                                    with_fact=True)
print('========================')
sorting_dict(dict_type_7_fa, faixa)
print('========================')
dict_type_7_sqr = make_a_values_dict(operas=operas_5, n_token_opers=3, str_numbers=str_4444,
                                     with_sqrt=True)
print('========================')
sorting_dict(dict_type_7_sqr, faixa)

print('========== FIM ==================')
