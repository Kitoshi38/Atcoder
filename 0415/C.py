def solve(n, q, queries):
    cards = [[] for _ in range(n+1)]  
    nums = [set() for _ in range(2*10**5+1)]

    for query in queries:
        if query[0] == 1:
            _, i, j = query[0], query[1], query[2]
            cards[j].append(i)   # 箱jにカードxを入れる
            nums[i].add(j)      # カードiに箱jを入れる
        elif query[0] == 2:
            _, i = query[0], query[1]
            sorted_cards = sorted(cards[i])
            print(*sorted_cards)
        elif query[0] == 3:
            i = query[1]
            sorted_nums = sorted(set(nums[i]))
            print(*[n for n in sorted_nums])

n = int(input())
q = int(input())
queries = []
for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

solve(n, q, queries)