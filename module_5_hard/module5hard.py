# Задание "Свой YouTube":
# Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.
# Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий функционал на сайте.
# Всего будет 3 класса: UrTube, Video, User.
# Общее ТЗ:
# Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.
# Подробное ТЗ:
# Каждый объект класса User должен обладать следующими атрибутами и методами:
# Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
# Каждый объект класса Video должен обладать следующими атрибутами и методами:
# Атрибуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
# Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
# Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
# Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
# Метод log_out для сброса текущего пользователя на None.
# Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
# Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
# Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
# Для метода watch_video так же учитывайте следующие особенности:
# Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
# Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
# Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
# После воспроизведения нужно выводить: "Конец видео"

# Код для проверки:
# ur = UrTube()
# v1 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# # Добавление видео
# ur.add(v1, v2)
# # Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')

# Вывод в консоль:
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist

# Примечания:
# Не забывайте для удобства использовать dunder(магические) методы: __str__, __repr__, __contains__, __eq__ и др. (повторить можно здесь)
# Чтобы не запутаться рекомендуется после реализации каждого метода проверять как он работает, тестировать разные вариации.


import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __contains__(self, other):
        return other.lower() in self.title.lower()

    def __eq__(self, other):
        return other == self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    # def inspect(self):
    # """Check the content"""
    # print("Users are:")
    # for item in self.users:
    # print('    ', item)
    # print("Videos are:")
    # for item in self.videos:
    # print('    ', item)

    def log_in(self, nickname, password):
        for usr in self.users:
            if usr.nickname == nickname and usr.password == hash(password):
                self.current_user = usr

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"User {nickname} already exists")
        else:
            reg_usr = User(nickname, password, age)
            self.users.append(reg_usr)
            self.current_user = reg_usr

    def add(self, *args):
        self.args = args
        for i in args:
            if i.title not in self.videos:
                self.videos.append(i)
            else:
                return f"{i.title} already present"

    def get_videos(self, name):
        # for i in self.videos:
        # if name in i:
        # print(i.title, end = " ")
        # list = []
        # for i in self.videos:
        # if name in i:
        # list.append(i.title)
        # return list
        return [i.title for i in self.videos if name in i]

    def watch_video(self, title):
        for video in self.videos:
            if title == video:
                if self.current_user == None:
                    print("Please log in to watch the video")
                    return
                if video.adult_mode and self.current_user.age <= 18:
                    print("You are not 18 yet please leave this page")
                    return
                for i in range(1, video.duration + 1):
                    time.sleep(1)
                    time_now = video.time_now + i
                    print(time_now, end=" ")
                print("End of Video")
                video.time_now = 0


# Код для проверки:
ur = UrTube()
v1 = Video("Лучший язык программирования 2024 года", 200)
v2 = Video("Для чего девушкам парень программист?", 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos("лучший"))  # Лучший язык программирования 2024 года
print(
    ur.get_videos("ПРОГ")
)  # Лучший язык программирования 2024 года Для чего девушкам парень программист?

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video("Для чего девушкам парень программист?")
ur.register("vasya_pupkin", "lolkekcheburek", 13)
ur.watch_video("Для чего девушкам парень программист?")
ur.register("urban_pythonist", "iScX4vIJClb9YQavjAgF", 25)
ur.watch_video("Для чего девушкам парень программист?")
# Проверка входа в другой аккаунт
ur.register(
    "vasya_pupkin", "F8098FM8fjm9jmi", 55
)  # Пользователь vasya_pupkin уже существует
print(ur.current_user)
# ur.log_out()
# print(ur.current_user) # None
# ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
# ur.inspect()
# # Попытка воспроизведения несуществующего видео
ur.watch_video("Лучший язык программирования 2024 года!")
