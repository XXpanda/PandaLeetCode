def ways_to_crawl(m, n):
    if m <= 0:
        return 1
    if n <= 0:
        return 1
    # if m == 0 and n == 0:
    #     return 0
    ways = [[0 for i in range(n)] for j in range(m)]
    ways[0][0] = 1
    # ways[0][n-1] = 0
    i = 0
    while i < m:
        j = 0
        while j < n:
            if i == 0 and j == 0:
                j += 1
                continue
            if i == 0:
                ways[i][j] = ways[i][j-1]
                j += 1
                continue
            if j == 0:
                ways[i][j] = ways[i-1][j]
                j += 1
                continue
            ways[i][j] = ways[i-1][j] + ways[i][j-1]
            j += 1
        i += 1

    return ways[m-1][n-1]


def ways_to_crawl_recur(m, n):
    if m == 0 and n == 0:
        return 0
    if n == 0:
        return 1
    if m == 0:
        return 1
    return ways_to_crawl_recur(m, n-1) + ways_to_crawl_recur(m-1, n)


if __name__ == '__main__':
    m = 5
    n = 4
    # print ways_to_crawl(m, n)
    grid = [[0 for i in range(n)] for j in range(m)]
    print ways_to_crawl_recur(m-1, n-1)
