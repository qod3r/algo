from coins import greedy


clients = [123, 300, 99]
reserve = {
    100: 2,
    50: 10,
    10: 10,
    4: 10,
    3: 10,
    1: 10
}

for c in clients:
    used = greedy(c)
    after_use = {key: reserve[key] - used.get(key, 0) for key in reserve}
    if any(x < 0 for x in after_use.values()):
        print("not enough mony")
        print(dict((k, v) for k, v in after_use.items() if v < 0))
        break
    reserve = after_use
    print(f"request: {c}")
    print(f"used: {dict((k, v) for k, v in used.items() if v > 0)}")
    print(f"left: {reserve}\n")
    