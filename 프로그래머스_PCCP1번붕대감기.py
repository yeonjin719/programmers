def solution(bandage, health, attacks):
    maxhealth = health
    time = 0
    lasttime = attacks[-1][0]
    cnt = 0
    for i in range(lasttime+1):
        if i == attacks[cnt][0]:
            time = 0
            health -= attacks[cnt][1]
            cnt += 1
            if health <= 0:
                return -1
        else:
            if health == maxhealth:
                pass
            else:
                health += bandage[1]
                time += 1
            if time == bandage[0]:
                health += bandage[2]
                time = 0
            if health > maxhealth:
                health = maxhealth

    answer = health
    return answer

bandage = [3,1, 10]
health = 100
attacks = [[1, 5], [3, 5]]

print(solution(bandage, health, attacks))
