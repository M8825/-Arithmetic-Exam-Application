# write your code here
usr_inp = input().split()

if '+' in usr_inp:
    x = int(usr_inp[0])
    y = int(usr_inp[2])
    print(x + y)
elif '*' in usr_inp:
    x = int(usr_inp[0])
    y = int(usr_inp[2])
    print(x * y)

elif '-' in usr_inp:
    x = int(usr_inp[0])
    y = int(usr_inp[2])
    print(x - y)

