def solution(board, h, w):
    color = board[h][w]
    answer = 0
    dh = [0,1,-1,0]
    dw = [1,0,0,-1]
    for i in range(4):
        if dh[i]+h >= len(board) or dw[i]+w >= len(board) or dh[i]+h < 0 or dw[i]+w <0:
            pass
        elif color == board[dh[i]+h][dw[i]+w]:
            answer += 1
        else:
            pass
    return answer
