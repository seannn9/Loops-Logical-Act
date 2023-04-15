while True:
    N = int(input("Enter value for N: "))
    P = int(input("Pick a pattern (1-3): "))
    if P == 1:
        for i in range(N):
            print('*' * N)
            N-=1
    elif P == 2:
        space = 1
        for i in range(N):
            print(" " * (N-space) + ("*" * space))
            space+=1
    elif P == 3:
        space = 1
        for i in range(N):
            if i == 0:
                print(" " * (N-1) + ("*"))
            else:
                print((" " * (N-space) + ("* ")) + ("* " * (space-1)))
            space += 1
    else:
        print("Invalid pattern")
    
    try_again = input("Try again? y/n: ").upper()
    if (try_again == 'Y'):
        continue
    elif (try_again == 'N'):
        break
    else:
        print("Invalid input")
        break