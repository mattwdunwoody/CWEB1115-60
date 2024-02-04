def main():
    format_text()

def get_input():
    user_input = [
            input("Please enter a name: ").capitalize(),
            input("Please enter another name: ").capitalize(),
            input("Please enter a beverage: "),
            input("Please enter a adjective: "),
            input("Please enter another adjective: "),
            input("Please enter a third name: ").capitalize(),
            input("Please enter the name of an animal: "),
            input("Please enter a part of the body: "),
            input("Please enter a a substance: "),
            input("Please enter the name of a company: ")
        ]
    
    for i in range(len(user_input)):
        if user_input[i] == "" or user_input[i] == " ":
            print("No empty inputs allowed! Try again!")
            get_input()

    return user_input

def format_text():

    _user_input = get_input()

    for i in range(4):
        print("")

    print("Your Story...")

    for i in range(2):
        print("")

    print('One day {0} was walking down the street when they saw their friend {1} spill their {2} from across the street. \"Hey!" said {0}. \"What happened?"'.format(*_user_input))
    print('"I spilled my {2}!" said {1}. "My {3}, {4}, {2}!" Just then, their friend {5} turned a corner to only to see the tragedy that was unfolding. "Woah!" said {5}. "Did you just spill your {2}, {1}? Your {3}, {4}, {2}?"'.format(*_user_input))
    print('"Yes!" cried {1}. "I spilled my {2} and now all I can do is cry about it!" Immeditately after {1} said this, a(n) {6} came and started to lick up the {2}! {1} tried to shoo it off, but then it bit their {7}!'.format(*_user_input))
    print('"Ow!" shouted {1}. "This is the worst day ever! I spilled my {2}! My {3}, {4}, {2}! Both my friends {0} and {5} saw it, and now a {6} just bit my {7}! How could this day get any worse!?"'.format(*_user_input))
    print('Almost like they were asking for it, right after {1} said this, a bunch of {8} fell from the sky and got all over {1}. {1} looked up to see plane from {9} flying away. "Well that\'s just great," said {1}. The {6} made a weird noise and then left the scene.'.format(*_user_input))
    print("The End!")
    
    for i in range(4):
        print("")
    
main()