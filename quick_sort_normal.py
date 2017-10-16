def swap(a, x, y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp


def median(a, left, right):
    center_index = (left + right) / 2
    if a[center_index] < a[left]:
        swap(a, left, center_index)
    if a[right] < a[center_index]:
        swap(a, center_index, right)
    swap(a, center_index, right)
    return a, a[right]


# def quick_sort_core(a, left, right):
#     a, pivot = median(a, left, right)
#     i = left
#     j = right - 1
#     while i < j:
#         while i < j and a[i] < pivot:
#             i += 1
#         # a[]
#         while i < j and a[j] > pivot:
#             j -= 1
#         if i < j:
#             a = swap(a, i, j)
#         else:
#             break
#     a = swap(a, i, right)
#     quick_sort_core(a, left, i - 1)
#     quick_sort_core(a, i + 1, right)
#     return a
#
#
# def quick_sort_main(a):
#     # print a
#     print quick_sort_core(a, 0, len(a) - 1)


def partition(a, low, high):
    pivot = a[low]
    while low < high:
        while low < high and a[high] >= pivot:
            high -= 1
        a[low] = a[high]
        while low < high and a[low] <= pivot:
            low += 1
        a[high] = a[low]
    a[low] = pivot
    return low


def quick_sort_sub(a, low, high):
    if low < high:
        pivot_index = partition(a, low, high)
        quick_sort_sub(a, low, pivot_index-1)
        quick_sort_sub(a, pivot_index+1, high)


def quick_sort(a):
    quick_sort_sub(a, 0, len(a)-1)

if __name__ == '__main__':
    xxx = [5, 4, 14, 6, 2, 10, 7]
    # xxx = [7,3,5,6,2,4,1]
    # print median(xxx, 0, 3)
    quick_sort(xxx)
    print xxx

    # quick_sort1(xxx, 0, len(xxx) - 1)
    # print xxx
