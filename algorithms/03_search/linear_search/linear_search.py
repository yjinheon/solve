

def linear_search(n : int , v : int):
    a = list(range(1,n+1))
    exist = False

    for i in a:
        if i == v:
            exist = True
            break

    if exist:
        print("Yes")
    else:
        print("No")


def main():
    linear_search(20,3)


if __name__ == "__main__":
    main()
