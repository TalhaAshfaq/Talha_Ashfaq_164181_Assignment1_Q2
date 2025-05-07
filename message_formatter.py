def my_decorator(func):
    def emoji():
        print("⚽⚽⚽⚽⚽⚽")
        print(func())
        print("⚽⚽⚽⚽⚽⚽")
    return emoji

def my_decorator2(func):
    def emoji2():
        print("🎮🎮🎮🎮🎮🎮")
        print(func())
        print("🎮🎮🎮🎮🎮🎮")
    return emoji2


#sports()