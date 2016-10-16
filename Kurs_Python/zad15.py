def table(x1, x2, y1, y2):
    print([" "] + list(range(x1, x2+1)))

    for i in range(y1, y2+1):
        print([i] + list(map(lambda x: x*i, range(x1, x2+1))))
