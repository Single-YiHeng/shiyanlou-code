def palindrome(s):
    return s == s[::-1]
if __name__ == '__main__':
    s = input("enter a string:")
    if palindrome(s):
        print("yay a palindrome")
    else:
        print("oh no,not a palindrome")
