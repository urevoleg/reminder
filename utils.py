import time
import os
import telepot

def logfile(string, to_catalog=time.strftime('c://logger/%Y%m/'), filename=time.strftime('report.log')):
    string = time.strftime('%d.%m.%y %H:%M:%S.') + str(time.time() - int(time.time()))[2:] + '\t' + string + '\n'

    if os.path.exists(to_catalog):
        with open(to_catalog + filename, 'a') as f:
            f.write(string)
    else:
        os.makedirs(to_catalog)
        with open(to_catalog + filename, 'w') as f:
            f.write(string)

# телеграмм токен
token = 'your_tlg_token'

def tlg_msg(message):
    try:
        TelegramBot = telepot.Bot(token)
        """
        chat_id - идентификатор канала в телеге куда собираешься слать напоминалки
        """
        TelegramBot.sendMessage(chat_id = 'your_chat_id', text = message)
        report = time.strftime('%d.%m.%y %H:%M') + '\t'
        report += 'telegram message to notification\t200 OK'
        #logfile(report, dest + foldername, 'report.log')
        print(report)
    except Exception as e:
        report = time.strftime('%d.%m.%y %H:%M') + '\t' + str(e)
        #logfile(report, dest + foldername, 'report.log')
        print(report)