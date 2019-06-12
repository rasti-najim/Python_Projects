# Enter a string and the program will reverse it and print it out.

string = input()


def reverse_str(string):
    new_string = string[::-1]
    print(new_string)


reverse_str(string)
