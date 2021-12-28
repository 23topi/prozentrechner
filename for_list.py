def test():
    print("test")

def nix():
    print("doof")

y = input("EIngabe: ")
counter = 3
x = ["1", "2", "3"]

while True:

    for i in x:
        if y == i:
            print(i)
            test()
            break
        else:
            nix()


    if counter == 3:
        print("reicht")
        break

