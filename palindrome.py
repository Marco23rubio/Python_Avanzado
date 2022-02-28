def is_palindrome(a:str) -> bool:
    a = a.replace(" ","").lower()
    return a == a[::-1]

def run():
    print (is_palindrome(101))

if __name__ == "__main__":
    run()