def main():
    for fizzbuzz in range(1, 101):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("fizzbuzz")
        elif fizzbuzz == 42:
            print("Answer to the ultimate question of life, the universe and everything")
        elif fizzbuzz % 3 == 0:
            print("fizz")
        elif fizzbuzz % 5 == 0:
            print("buzz")
        else:
            print(fizzbuzz)


if __name__ == "__main__":
    main()
