# Inheritance

from Chef import Chef

class Main:

    def main():
        myChef = Chef()
        hotdish = myChef.make_hotdish()
        spam = myChef.make_fried_spam()
        spam_hotdish = myChef.make_spam_hotdish()

        from WICopycatChef import WICopycatChef

        WICopycatChef = WICopycatChef()
        wi_hotdish = WICopycatChef.make_hotdish()
        wi_spam = WICopycatChef.make_fried_spam()
        wi_spam_hotdish = WICopycatChef.make_spam_hotdish()

        print(f'Step 1: {hotdish}\nStep 2: {spam}\nThe result: {spam_hotdish}\n')
        print(f'Step 1: {wi_hotdish}\nStep 2: {wi_spam}\nThe result: {wi_spam_hotdish}\n')

    if __name__ == '__main__': main()