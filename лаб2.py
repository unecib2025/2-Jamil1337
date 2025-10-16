1.
#a = input()
#if len(a) < 8:
#    print('Слишком короткий пароль')
#else:
#    print('Пароль принят')
2.
#status = input('Введите статус сервера')
#if status == 'online':
#    print('Связь установлена')
#elif status == 'offline':
#    print('Связь не установлена')
3.
#a = int(input())
#if 1<=a<=30:
#    print('Низкий уровень угрозы')
#elif 31<=a<=70:
#    print('Средний уровень угрозы')
#elif 71<=a<=100:
#    print('Критический уровень угрозы')
#else:
#    print('Ошибка ввода')
4.
#checksum_original = input()
#checksum_current = input()
#status = "Файл не изменён" if checksum_original == checksum_current else "Файл повреждён"
#print(status)
5.
event_code = input('Введите код события (ERR, WRN, INF): ')
match event_code:
    case "ERR":
        print('Ошибка системы')
    case "WRN":
        print('Предупреждение')
    case "INF":
        print('Информационное сообщение')
    case _:
        print('Неизвестный код события')