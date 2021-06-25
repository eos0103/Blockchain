for _ in range(int(input())):
    item_a, item_b = map(int, input().split())
    quo = item_a//item_b
    rem = item_a%item_b
    print("You get",quo,"piece(s) and your dad gets", rem, "piece(s).")