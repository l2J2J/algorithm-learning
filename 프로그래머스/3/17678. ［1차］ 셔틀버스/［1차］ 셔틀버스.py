from collections import deque

def solution(n, t, m, timetable):
    answer = 0
    table = []
    max_people = n*m
    for k in timetable:
        a, b = map(int, k.split(':'))
        table.append(60*a + b)
    table = deque(sorted(table))
    people = 0
    bus_time = 540
    idx = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if idx < len(table) and table[idx] <= bus_time:
                cur = table[idx]
                cnt += 1
                idx += 1
                if cnt == m or people + cnt == max_people:
                    answer = cur-1
                    break
            else:
                break
        people += cnt
        
        if i != n-1:
            bus_time += t
        elif cnt != m:
            answer = bus_time
    
    
    a = str(answer // 60) if len(str(answer // 60)) == 2 else '0' + str(answer // 60)
    b = str(answer % 60) if len(str(answer % 60)) == 2 else '0' + str(answer % 60)
    
    answer = a + ':' + b
    return answer