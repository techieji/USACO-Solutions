def swap(threads, a, b):
    m = {a: b, b: a}
    return [{a: b, b: a}.get(x, x) for x in threads]

with open('shell.in') as f:
    _ = next(f)
    threads = [1, 2, 3]
    scores = [0, 0, 0]
    for x in f:
        a, b, guess = map(int, x.split())
        threads = swap(threads, a, b)
        scores = [score + (x == guess) for x, score in zip(threads, scores)]

with open('shell.out', 'w') as f:
    print(max(scores), file=f)
