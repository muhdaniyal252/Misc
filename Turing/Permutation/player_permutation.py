from itertools import combinations

n = 6
m = 6
games = [
    [3,1,4,5,6,2],  # Round 1
    [5,3,2,4,1,6],  # Round 2
    [5,3,6,4,2,1],  # Round 3
    [6,5,3,2,1,4],  # Round 4
    [5,4,1,2,6,3],  # Round 5
    [4,1,6,2,5,3]   # Round 6
]
n = 6
m = 6
games = [
    [1, 6, 3, 4, 5, 2],  # Round 1
    [6, 4, 2, 3, 1, 5],  # Round 2
    [4, 2, 1, 5, 6, 3],  # Round 3
    [4, 5, 1, 6, 2, 3],  # Round 4
    [3, 2, 5, 1, 6, 4],  # Round 5
    [2, 3, 6, 4, 1, 5]   # Round 6
]

n = 2
m = 1
games = [
    [1,2]
]

n = 4
m = 2
games = [
    [1,2,3,4],
    [4,3,1,2]
]

n = 4
m = 2
games = [
    [1,2,3,4],
    [1,3,2,4]
]
x = list(range(1,n+1))

pairs = list(combinations(x,2))
pairs = [[i[0],i[1],False] for i in pairs]

team_size = int(n/2)

rounds = dict()

for i in range(m):
    rounds.update({
        i+1:[games[i][:team_size],games[i][team_size:]]
    })


for _,teams in rounds.items():
    for pair in filter(lambda x: not x[2],pairs):
        x = pair[0]
        y = pair[1]
        team1 = teams[0]
        team2 = teams[1]
        if (x in team1 and y in team2) or (x in team2 and y in team1):
            pair[2] = True

all(i[2] for i in pairs)

        
