# coding=utf-8
# bool finished = FALSE; # 是否获得全部解?
# backtrack(int a[], int k, data input)
# {
#    int c[MAXCANDIDATES]; /*这次搜索的候选 */
#    int ncandidates; /* 候选数目 */
#    int i; /* counter */
#    if (is_a_solution(a,k,input))
#    process_solution(a,k,input);
#    else {
#        k = k+1;
#        construct_candidates(a,k,input,c,&ncandidates);
#        for (i=0; i<ncandidates; i++) {
#            a[k] = c[i];
#            make_move(a,k,input);
#            backtrack(a,k,input);
#            unmake_move(a,k,input);
#            if (finished) return; /* 如果符合终止条件就提前退出 */
#        }
#    }
# }


def swap(array, idx1, idx2):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp


def permutation(array, idx, length):
    if length == idx:
        print array
    else:
        for i in range(idx, length):
            swap(array, idx, i)
            permutation(array, idx + 1, length)
            swap(array, idx, i)


def sub_sequence(str_list, idx_list, idx, n, size):
    if n == 0:
        print '{}'
    elif n == 1:
        temp_list = []
        for i in range(idx, size):
            idx_list[i] = 1
            for j in range(0, size):
                if idx_list[j]:
                    temp_list.append(str_list[j])
            print temp_list
            temp_list = []
            idx_list[i] = 0

    else:
        for i in range(idx, size):
            idx_list[i] = 1
            sub_sequence(str_list, idx_list, i + 1, n - 1, size)
            idx_list[i] = 0


def phone_digit_num_combination(table, idx, digit_list, digit_string, result):
    if not digit_string:
        return []
    if idx == len(digit_string):
        result.append(''.join(digit_list))
    else:
        candi = table[int(digit_string[idx])]
        for i in range(len(candi)):
            digit_list.append(candi[i])
            phone_digit_num_combination(table, idx+1, digit_list, digit_string, result)
            digit_list.pop()


if __name__ == '__main__':
    array_test = [1, 2, 3]
    idx_list = [0]*3
    # permutation(array_test, 0, len(array_test))
    for i in range(len(array_test)+1):
        sub_sequence(array_test, idx_list, 0, i, 3)
    # table_test = [" ", " ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    # digit_string_test = '234'
    # digit_list_test = []
    # idx = 0
    # result = []
    # phone_digit_num_combination(table_test, idx, digit_list_test, digit_string_test, result)
    # print result