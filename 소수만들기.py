def solution(nums):
    l = len(nums)
    answer = (l*(l-1)*(l-2))//6
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                stop = False
                num = nums[i]+nums[j]+nums[k]
                for m in range(2, num-1):
                    if num % m == 0:
                        if stop == True:
                            pass
                        else:
                            answer -= 1
                            stop = True
    return answer
