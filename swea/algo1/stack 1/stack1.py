import sys
sys.stdin = open('bracket_input.txt')

def solution(t):

    arr = str(input().strip())
    size = len(arr)
    stak = []

    def find(arr,size):
        for i in range(size):
            if arr[i] == '(':
                stak.append(arr[i])
            #무아 강사님이 하신 조건
            # elif arr[i] == ')' and top >= and stak[top] == '(':
            #     pop(stak)
            elif '(' not in arr:
                stak.append(1)
            else:
                stak.pop()

        if len(stak) > 0:
            return -1
        else:
            return 1

    return find(arr, size)

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        print(f'#{t} {solution(t)}')