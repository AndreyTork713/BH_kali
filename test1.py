class MyName:
    name = input('Введите ваше имя: ')
    if name == 'Андрей':
        print('Ну наконец-то, привет Андрей!!!')
    elif name == 'Аня':
        print('Аня, я очень рада тебя видеть! Позови, пожалуйста, Андрея.')
    else:
        print('Я вас не знаю, покиньте немедленно',
              'данную изолированную среду! ')


if __name__ == '__main__':
    my_name = MyName()
    print('Это всё')