def max_flow(C, s, t):
    n = len(C)  # C is the capacity matrix

    F = [[0] * n for i in range(n)]

    path = bfs(C, F, s, t)

    print (path)

    while path != None:

        flow = min(C[u][v] - F[u][v] for u, v in path)

        for u, v in path:
            F[u][v] += flow

            F[v][u] -= flow

        path = bfs(C, F, s, t)

    return sum(F[s][i] for i in range(n))


# find path by using BFS

def bfs(C, F, s, t):
    queue = [s]

    paths = {s: []}

    if s == t:
        return paths[s]

    while queue:

        u = queue.pop(0)

        for v in range(len(C)):

            if (C[u][v] - F[u][v] > 0) and v not in paths:

                paths[v] = paths[u] + [(u, v)]

                print (paths)

                if v == t:
                    return paths[v]

                queue.append(v)

    return None
def max_flow(C, s, t):
    n = len(C)  # C is the capacity matrix

    F = [[0] * n for i in range(n)]

    path = bfs(C, F, s, t)

    print (path)

    while path != None:

        flow = min(C[u][v] - F[u][v] for u, v in path)

        for u, v in path:
            F[u][v] += flow

            F[v][u] -= flow

        path = bfs(C, F, s, t)

    return sum(F[s][i] for i in range(n))


# find path by using BFS

def bfs(C, F, s, t):
    queue = [s]

    paths = {s: []}

    if s == t:
        return paths[s]

    while queue:

        u = queue.pop(0)

        for v in range(len(C)):

            if (C[u][v] - F[u][v] > 0) and v not in paths:

                paths[v] = paths[u] + [(u, v)]

                print (paths)

                if v == t:
                    return paths[v]

                queue.append(v)

    return None
