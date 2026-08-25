def solution(s):
    answer = 1

    for i in range(len(s)):
        for j in range(len(s)-1, i, -1):
            a = i
            b = j
            while a < b:
                if s[a] == s[b]:
                    a += 1
                    b -= 1
                else:
                    break
            if a >= b: 
                answer = max(answer, j-i+1)
                break
                

    return answer