def make_repeater_fo(n):
    def repeater(x):
        assert type(x) == str , "Solo puedes usar letras"
        return x*n
    return repeater

def run():
    repeat_5 = make_repeater_fo(5)
    print(repeat_5(2))

if __name__ == "__main__":
    run()
