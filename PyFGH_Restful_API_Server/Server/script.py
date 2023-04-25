import sys
import ast

def main():
    # Get the command line arguments
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]


    # use ast.literal_eval() to parse the string and create a list
    result = ast.literal_eval(arg2)


    # Print the arguments
    print(arg1)
    print(arg2)


if __name__ == "__main__":
    main()
