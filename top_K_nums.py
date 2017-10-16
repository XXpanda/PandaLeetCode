def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    num_count_dict = {}
    for num in nums:
        num_count_dict[num] = num_count_dict.get(num, 0) + 1
    num_count_dict_sorted = sorted(num_count_dict.items(), key=lambda d: d[1], reverse=True)
    result_list = []
    for num_tuple in num_count_dict_sorted:
        if num_tuple[1] >= k:
            result_list.append(num_tuple[0])
        else:
            break
    return result_list


if __name__ == '__main__':
    a = [1, 1, 1, 2, 2, 4]
    print topKFrequent(a, 2)
