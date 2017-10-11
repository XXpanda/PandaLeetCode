def max_sequence_sum_3(num_list):
    max_sum = num_list[0]
    i = 0
    num_list_len = len(num_list)
    while i < num_list_len:
        j = i
        while j < num_list_len:
            temp_sum = 0
            k = i
            if k == j:
                temp_sum = max_sum
            while k < j:
                temp_sum += num_list[k]
                k += 1
            if temp_sum > max_sum:
                max_sum = temp_sum
            j += 1
        i += 1
    return max_sum
# [2, 4, 6, -4, -2, 34, -3, 42]


def max_sequence_sum_2(num_list):
    max_sum = num_list[0]
    i = 0
    num_list_len = len(num_list)
    while i < num_list_len:
        j = i
        if i == 0:
            this_sum = max_sum
        else:
            this_sum = 0
        while j < num_list_len:
            this_sum += num_list[j]
            if this_sum > max_sum:
                max_sum = this_sum
            j += 1
        i += 1
    return max_sum

# [2, 4, 6, -4, -2, 34, -3, 42]


def max_sum_rec(num_list, left, right):
    if left == right:
        return num_list[left]
    center = (left + right) / 2
    max_left_sum = max_sum_rec(num_list, left, center)
    max_right_sum = max_sum_rec(num_list, center + 1, right)

    max_left_boarder_sum, left_boarder_sum = float('-inf'), 0
    i = center
    while i >= left:
        left_boarder_sum += num_list[i]
        if left_boarder_sum > max_left_boarder_sum:
            max_left_boarder_sum = left_boarder_sum
        i -= 1

    max_right_boarder_sum, right_boarder_sum = float('-inf'), 0
    i = center + 1
    while i <= right:
        right_boarder_sum += num_list[i]
        if right_boarder_sum > max_right_boarder_sum:
            max_right_boarder_sum = right_boarder_sum
        i += 1
    return max(max_left_sum, max_right_sum, max_left_sum + max_right_sum)


if __name__ == '__main__':
    num_list_test = [-11, -12, -132, -10, -15, -212]
    # print max_sequence_sum_2(num_list_test)
    print max_sum_rec(num_list_test, 0, len(num_list_test) - 1)
