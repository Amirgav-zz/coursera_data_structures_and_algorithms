# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_idx = 0
    for i in range(n):
        if numbers[i] > numbers[max_idx]:
            max_idx = i

    max_idx2 = 0 if max_idx != 0 else 1

    for j in range(n):
        if (j != max_idx) and (numbers[j] > numbers[max_idx2]):
            max_idx2 = j

    return numbers[max_idx]*numbers[max_idx2]



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))