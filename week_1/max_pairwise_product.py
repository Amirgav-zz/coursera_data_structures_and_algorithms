
# def max_pair_product(numbers):
#     n = len(numbers)
#     max_idx = 0
#     for i in range(n):
#         if (max_idx == 0) or (numbers[i] > numbers[max_idx]):
#             max_idx = i
#
#     max_idx2 = 0
#     for j in range(n):
#         if (max_idx2 != max_idx2) and ((max_idx2 == 0) or (numbers[j] > numbers[max_idx2])):
#             max_idx2 = j
#
#     return numbers[max_idx]*numbers[max_idx2]
#
#
# if __name__ == '__main__':
#     input_n = int(input())
#     numbers = [int(x) for x in input().split()]
#     print(max_pair_product(numbers))

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))