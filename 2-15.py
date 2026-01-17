# 優化點:
# deque 替代 del
# q 紀錄已在queue隊伍編號
# team 直接存每個數字對應編號 配合q直接知道是否在queue中
#  遍歷queue時 直接比對隊伍編號不用 in 去確認
now = 1
from collections import deque
while True:
        try:
                queue = deque()
                q = set()
                team = {}
                m = int(input())
                if m == 0:break
                for i in range(m):
                        temp = input().split()
                        for j in temp[1:]:
                                team[j] = i
                print(f"Scenario #{now}")
                now += 1
                while True:
                        cmd = input()
                        if cmd == "DEQUEUE":
                                if len(queue) != 0:
                                        print(queue[0][0])
                                        team_num = team[queue[0][0]]
                                        queue[0].popleft()
                                        if len(queue[0]) == 0:
                                                queue.popleft()
                                                q.remove(team_num)
                        elif cmd == "STOP":break
                        else:
                                cmd , num = cmd.split()
                                team_num = team[num]
                                if team_num in q:
                                    for j in range(len(queue)):
                                            if queue[j] and team[queue[j][0]] == team_num:
                                                    queue[j].append(num)
                                                    break
                                else:
                                    queue.append(deque([num]))
                                    q.add(team_num)
                print()
        except EOFError:
                break