import time

class View:
    @staticmethod
    def show_message(message):
        print(message)
        
    @staticmethod
    def show_message_fancy_top(message):
        for line in message.splitlines():
            print(line)
            time.sleep(0.03)
        for i in range(14):
            print("\n")
            time.sleep(0.03)
            
    @staticmethod
    def show_message_fancy_bottom(message):
        for i in range(11):
            print("\n")
            time.sleep(0.03)
        for line in message.splitlines():
            print(line)
            time.sleep(0.03)

    @staticmethod
    def get_input(prompt):
        return input(prompt)
    
    @staticmethod
    def debug_msg(message):
        print("DEBUG: " + message)
        
    @staticmethod
    def clear_screen():
        console_height = 14
        for x in range(0, console_height):
            print("\n")
            
    @staticmethod
    def confirm():
        message = "Press Enter to continue..."
        message = [*message]
        for i in message:
            print(i, end="")
            time.sleep(0.01)
        input("")
        
    @staticmethod
    def show_message_scroll(message):
        print(message)
        time.sleep(0.03)
        
    @staticmethod
    def show_message_scroll_lines(message):
        for line in message.splitlines():
            print(line)
            time.sleep(0.05)
       
    @staticmethod
    def show_message_game_over(message):
        for line in message.splitlines():
            print(line)
            time.sleep(0.05)
        for i in range(0, 15):
            print("")
            time.sleep(0.05)
            
    @staticmethod
    def show_message_scroll_horizontally(message):
        message = [*message]
        for i in message:
            print(i, end="")
            time.sleep(0.03)
        print("")
        
    @staticmethod
    def show_message_scroll_horizontally_fast(message):
        message = [*message]
        for i in message:
            print(i, end="")
            time.sleep(0.01)
        print("")
            
    @staticmethod
    def dramatic_pause():
        time.sleep(1)
        
    @staticmethod
    def get_input_scroll_horizontally(message):
        message = [*message]
        for i in message:
            print(i, end="")
            time.sleep(0.03)
        user_input = input("")
        
        return user_input
    
    @staticmethod
    def show_message_fancy_top_scrollhorizontally(message):
        for line in message.splitlines():
            line = [*line]
            for i in line:
                print(i, end="")
                time.sleep(0.03)
            print("")
            time.sleep(0.03)
        for i in range(14):
            print("\n")
            time.sleep(0.03)