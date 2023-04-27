for i in [f"{i} X {j} = {i*j}" for j in range(1, 10)
                               for i in range(1, 10)]:
    print(i, end="\n\n")