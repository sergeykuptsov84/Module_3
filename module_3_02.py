def send_email(message, recipient, sender ="university.help@gmail.com"):
    if sender == recipient:
        print( "Нельзя отправить письмо самому себе!")
    # if sender != "university.help@gmail.com"
    #     print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса" , sender, "на адрес" , recipient)
    index1 = recipient.find('@')
    index2 = recipient.find('.com')
    index3 = recipient.find('.ru')
    index4 = recipient.find('.net')
    if sender!= recipient:
        if index1 < 0:
            print("Невозможно отправить письмо с адреса", sender, "на адрес ", recipient)
        elif index2 < 0 and index3 < 0 and index4 < 0:
            print("Невозможно отправить письмо с адреса", sender, "на адрес ", recipient)
        else:
            print("Письмо успешно отправлено с адреса ", sender, "на адрес ", recipient)



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')


