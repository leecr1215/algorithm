import sys

if __name__ == "__main__":
    x1, y1 = map(int, sys.stdin.readline().rstrip().split(" "))
    x2, y2 = map(int, sys.stdin.readline().rstrip().split(" "))
    x3, y3 = map(int, sys.stdin.readline().rstrip().split(" "))

    x4 = 0
    y4 = 0

    # x4 구하기
    if x1 == x2 : 
        x4 = x3
    elif x1==x3:
        x4 = x2
    else:
        x4 = x1

    # y4 구하기
    if y1 == y2 : 
        y4 = y3
    elif y1 == y3:
        y4 = y2
    else:
        y4 = y1

    print(x4,y4)
