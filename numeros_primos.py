def is_prime(a:int) -> bool:
    if a == 1:
        return False
    elif a == 2:
        return True
    for i in range(2,a):
        if a % i == 0:
            return False
        else:
            return True
                    
def run():
    print(is_prime(4))

if __name__ == '__main__':
    run()