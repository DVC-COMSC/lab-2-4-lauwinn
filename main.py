def main():
    ##################################################
    # Comlete your code here
    ##################################################

    original_str = "Python Programming"
    sub1 = original_str.split()[1]
    sub2 = original_str[:-11]
    merged_str = sub1 + ' ' + sub2
    print(sub1)
    print(sub2)
    print(merged_str)

    pass


if __name__ == '__main__':
    main()
