S = list(input())
C = input()


def compute(S, C):
    t = 0
    for i in range(len(S)):
        if S[i] == C:
            t += 1
    return t


print("%s occurs %d time(s)" % (C, compute(S, C)))