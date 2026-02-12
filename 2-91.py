n = int(input())
for i in range(n):
    try:
        game_name = input()
        t = int(input())
        team = {}
        for j in range(t):
            team[input()] = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
        g = int(input())
        for j in range(g):
            temp = input()
            a , goal , b = temp.split("#")
            a_goal , b_goal = map(int, goal.split("@"))
            if a_goal > b_goal:
                team[a][0] += 3
                team[a][2] += 1
                team[b][4] += 1
            elif a_goal < b_goal:
                team[b][0] += 3
                team[a][4] += 1
                team[b][2] += 1
            else:
                team[a][0] += 1
                team[b][0] += 1
                team[a][3] += 1
                team[b][3] += 1
            team[a][1] += 1
            team[b][1] += 1
            team[a][5] += (a_goal - b_goal)
            team[b][5] += (b_goal - a_goal)
            team[a][6] += a_goal
            team[b][6] += b_goal
            team[a][7] += b_goal
            team[b][7] += a_goal
        j = 0
        print(game_name)
        for k , v in sorted(team.items() , key = lambda x: (-x[1][0] , -x[1][2] , -x[1][5] , -x[1][6] , x[1][1] , (x[0]).lower())):
            j += 1
            print(f"{j}) {k} {v[0]}p, {v[1]}g ({v[2]}-{v[3]}-{v[4]}), {v[5]}gd ({v[6]}-{v[7]})")
        if i != n - 1:print()
    except EOFError:break
