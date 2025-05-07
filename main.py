from decorators.message_formatter import my_decorator, my_decorator2

@my_decorator
def sports():
    return "i am very fond of playing football"

user_input = input("Enter your favourite Video Game: ")

@my_decorator2
def video_games():
    return f"my favourite video game is: {user_input}"

if __name__ == "__main__":
    video_games()
    sports()
    


 