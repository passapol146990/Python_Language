from itertools import permutations
def permutation_generator(number):
    permutations_list = list(permutations(number))
    print(f'Number of permutations : {len(permutations_list)}')
    for permutation in permutations_list:
        print(permutation)
def run2():
    input_number = ''
    input_loop = int(input('loop:'))
    for i in range(0,input_loop):
        input_number += input(f'Enter number {i+1} :')
    permutation_generator(input_number)
run2()