ref =  [['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I'],
        ['J', 'K', 'L'],
        ['M', 'N', 'O'],
        ['P', 'Q', 'R', 'S'],
        ['T', 'U', 'V'],
        ['W', 'X', 'Y', 'Z'],
]

ans = 0 

for i in input():
    for j, res in enumerate(ref):
        if res.count(i) == 1:
            ans += j+3

print(ans)