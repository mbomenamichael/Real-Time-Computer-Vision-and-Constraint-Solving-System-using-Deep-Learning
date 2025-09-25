def sudoku(f):
    def display(g):
        for n, l in enumerate(g):
            for m, c in enumerate(l):
                print(str(c).replace("0", "."), end="")
                if m in {2, 5}:
                    print("+", end="")
            print()
            if n in {2, 5}:
                print("+" * 11)

    def candidates(q, s):
        l = set(s[q[0]])
        l |= {s[i][q[1]] for i in range(9)}
        k = q[0] // 3, q[1] // 3
        for i in range(3):
            l |= set(s[k[0] * 3 + i][k[1] * 3:(k[1] + 1) * 3])
        return set(range(1, 10)) - l

    def has_duplicates(l):
        q = set(l) - {0}
        for c in q:
            if l.count(c) != 1:
                return True
        return False

    display(f)

    s = []
    t = []
    for nl, l in enumerate(f):
        try:
            n = list(map(int, l))
        except:
            print("Line " + str(nl + 1) + " contains something other than a number.")
            return
        if len(n) != 9:
            print("Line " + str(nl + 1) + " does not contain 9 numbers.")
            return
        t += [[nl, i] for i in range(9) if n[i] == 0]
        s.append(n)
    if nl != 8:
        print("The game has " + str(nl + 1) + " lines instead of 9.")
        return

    for l in range(9):
        if has_duplicates(s[l]):
            print("Line " + str(l + 1) + " is contradictory.")
            return
        col = [s[l][c] for c in range(9)]
        if has_duplicates(col):
            print("Column " + str(l + 1) + " is contradictory.")
            return

    for l in range(3):
        for c in range(3):
            cell = [s[l * 3 + i][c * 3 + j] for i in range(3) for j in range(3)]
            if has_duplicates(cell):
                print("Cell (" + str(l * 3 + 1) + ";" + str(c * 3 + 1) + ") is contradictory.")
                return

    p = [[] for i in t]
    cr = 0

    while cr < len(t):
        p[cr] = candidates(t[cr], s)
        try:
            while not p[cr]:
                s[t[cr][0]][t[cr][1]] = 0
                cr -= 1
        except:
            print("The sudoku has no solution.")
            return
        s[t[cr][0]][t[cr][1]] = p[cr].pop()
        cr += 1


    display(s)
    return(s)
