import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return hash(self.password)


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for i in self.users:
            if i.nickname == login and hash(i.password) == hash(password):
                self.current_user = i

    def register(self, nickname, password, age):
        for i in self.users:
            if i.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return None
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *adding_videos):
        for k in adding_videos:
            can_add = True
            for i in self.videos:
                if i.title == k.title:
                    can_add = False
                    break
            if can_add:

                print('shok')
                self.videos.append(k)

    def get_videos(self, search):
        title_list = []
        for i in self.videos:
            if search.lower() in i.title.lower():
                title_list.append(i.title)
        print(title_list[:])
        return title_list

    def watch_video(self, search):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        elif self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            for i in self.videos:
                if search == i.title:
                    a = i.duration - i.time_now
                    for j in range(1, a + 1):
                        time.sleep(1)
                        print(j)
                    print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 1, adult_mode=True)

# Добавление видео
ur.videos.append(v1)

ur.add(v1, v2)

# Проверка поиска
ur.get_videos('лучший')
ur.get_videos('ПРОГ')

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
