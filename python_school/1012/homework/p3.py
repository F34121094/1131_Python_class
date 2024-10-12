p = eval(input("Player HP:"))
e = eval(input("Enemy HP:"))
who = 0
while 1:
    print("player's round:")
    atk = eval(input("atk:"))
    e -= atk
    print(f"Player_HP: {p}")
    print(f"Enemy_HP: {e}")
    if e <= 0 :
        who = 1
        break
    print("enemy's round:")
    p -= 2
    print(f"Player_HP: {p}")
    print(f"Enemy_HP: {e}")
    if p <= 0:
        who = 2
        break
if who == 1: print("Victory")
else: print("Defeat")