class Game:
    top_score=0

    def __init__(self, player_name):
        self.player_name=player_name

    @staticmethod
    def show_help():
        print("help information")

    @classmethod
    def show_top_score(cls):
        print("history record: %d" % cls.top_score)


    def start_game(self):
        print("%s starts game" % self.player_name)

"""
__new__ 为对象分配空间
__init__ 为对象初始化属性
"""
class MusicPlayer:
    instance=None

    def __new__(cls, *args, **kwargs):
        # 创建对象时会自动调用
        print("init object space")
        # 为对象分配空间
        if cls.instance is None:
            cls.instance=super().__new__(cls)

        return cls.instance

    def __init__(self):
        print("initialize the object")

Game.show_help()
Game.show_top_score()
player=Game("eason")
player.start_game()

music1=MusicPlayer()
music2=MusicPlayer()
print(music1)
print(music2)
