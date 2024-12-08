def send_email(message, recipient, *, sender ="university.help@gmail.com"):
    if sender == recipient:
        print( "Нельзя отправить письмо самому себе!")

    index1 = recipient.find('@') and sender.find('@')          # index > 0 if '@' in address
    index2 = recipient.find('.com') and sender.find('.com')    # index > 0 if '.com' in address
    index3 = recipient.find('.ru') and sender.find('.ru')      # index > 0 if '.ru' in address
    index4 = recipient.find('.net') and sender.find('.net')    # index > 0 if '.net' in address
    index5 = sender.find('university.help@gmail.com')          # index > 0 if address 'university.help@gmail.com'

    if sender != recipient:
        if index1 < 0:
            print("Невозможно отправить письмо с адреса", sender, "на адрес ", recipient)
        elif index2 < 0 and index3 < 0 and index4 < 0:
            print("Невозможно отправить письмо с адреса", sender, "на адрес ", recipient)
        elif index5 < 0:
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
        else:
            print("Письмо успешно отправлено с адреса ", sender, "на адрес ", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

