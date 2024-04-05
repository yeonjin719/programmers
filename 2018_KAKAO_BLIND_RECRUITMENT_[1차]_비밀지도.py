def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        num1 = arr1[i]
        num2 = arr2[i]
        ans = ""
        for _ in range(n):
            if (num1 % 2) + (num2 % 2) > 0:
                ans = "#"+ans
            else:
                ans = " "+ans
            num1 //= 2
            num2 //=2
        answer.append(ans)
    return answer

# n=5
# arr1=[9, 20, 28, 18, 11]
# arr2=[30, 1, 21, 17, 28]
# solution(n, arr1, arr2)

# n=6
# arr1=[46, 33, 33 ,22, 31, 50]
# arr2=[27 ,56, 19, 14, 14, 10]
# solution(n, arr1, arr2)