def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Original array', numbers)
    new = 11
    numbers.append(new)
    print('Array after append: ', numbers)

if __name__ == "__main__":
    main()