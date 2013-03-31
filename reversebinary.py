import sys

def reverse_binary(input_number):
    try:
        bin_number = bin(int(input_number))
    except:
        return "Error, please enter an integer."
    reversed_bin = ''.join(reversed(bin_number[2:]))
    return int('0b' + reversed_bin, 2)

if __name__ == '__main__':
    print reverse_binary(sys.stdin.readline())
