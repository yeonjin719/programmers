def solution(s):
    index = 1
    samecnt = 1
    difcnt = 0
    answer = 0
    x = s[0]
    while True:
        if index >= len(s)-1:
            answer += 1
            print(s)
            break
        else:
            if x == s[index]:
                index += 1
                samecnt += 1
            else:
                difcnt += 1
                index += 1
        if samecnt == difcnt:
            answer += 1
            print(s[:samecnt*2])
            s=s[samecnt*2:]
            x = s[0]
            index = 1
            difcnt = 0
            samecnt = 1
    return answer

s = input()
print(solution(s))