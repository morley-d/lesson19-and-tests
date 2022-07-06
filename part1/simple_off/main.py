# Напишите декоратор off, 
# который при вызове функции 
# будет вместо функции выводить 
# в консоль "функция отключена"

def off(func):
    def wrapper(*args, **kwargs):
        print("функция отключена")
    return wrapper

# Ниже следует код для самопроверки:
# TODO Вы можете попробовать задекорировать функцию func
# которая выводит в терминал текст "работаю".

@off
def func():
    print("работаю")

if __name__=="__main__":
    func()