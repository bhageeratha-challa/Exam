def edgeChasingDeadlockDetection(WFG, n):
    probe = [[False for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if WFG[i][j] == 1:
                probe[i][j] = True
                for k in range(n):
                    if probe[j][k]:
                        probe[i][k] = True
    for i in range(n):
        if probe[i][i]:
            print("Deadlock detected at process", i)


WFG = [[0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 0, 1]]
n = 4
edgeChasingDeadlockDetection(WFG, n)
