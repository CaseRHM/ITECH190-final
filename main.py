def capitalize_list(my_list):
    txt = (my_list)
    lyst = txt.upper()
    print(lyst)


def print_list_on_new_lines(my_list):
    for lyst in my_list:
        print(lyst)

def print_list(lyst):
    print(lyst)

def main ():
    my_list = [
        "banana", 
        "whiterice",
        "pizza",
        "apples",
        "cherry",
        "cookie",
        "bread",
        "cake",
        "pancake",
        "chocolate"
        ]
    
    print(my_list)
    print_list_on_new_lines(my_list)
    print(capitalize_list(my_list))


if __name__ == "__main__":
    main()