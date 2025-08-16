def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Original array', arr)
    new=int(input("Insert new number: "))
    pos=int(input("Enter position: "))
    arr.insert(pos, new)
    print('Array after insertion: ', arr)


if __name__ == "__main__":
    main()
