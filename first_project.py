import json
import time
from time import strftime
import telepot
from telepot.loop import MessageLoop

from database import db

tim = strftime ("%Y/%B/%d %I:%M%p")
database = "/home/nsadec/PycharmProjects/StudentBank/database/ksu.db"
json_keyboard = json.dumps({'keyboard': [["اشترك في خدمة ذكرني بإمتحاني"],['جدول الاختبارات']],
                             'one': True, 'two': True, 'three': True})
json_keyboard1 = json.dumps({'keyboard': [["اشترك في خدمة ذكرني بإمتحاني"],['جدول الاختبارات'],['وجهني'],['ماهذا البوت']],
                             'one': True, 'two': True, 'three': True})
json_keyboard2 = json.dumps({'keyboard': [["ارسال تذكير بموعد اختبار"]],
                             'one': True, 'two': True, 'three': True})
json_keyboard3 = json.dumps({'keyboard': [["تعليم الاكتروني"],['قواعد بيانات'],['هندسة برمجيات'],['تقنيات المصادر المفتوحة'],['البرمجة الغرضية الموجهه'],["الرجوع للخلف"]],
                             'one': True, 'two': True, 'three': True, 'for': True, 'five': True})
json_keyboard4 = json.dumps({'keyboard': [["اشترك في التذكير للامتحانات"],['مشرف']],
                             'one': True, 'two': True, 'three': True})
json_keyboard5 = json.dumps({'keyboard': [['جميع الايام'],["يوم الاحد"],["يوم الاثنين"],["يوم الثلاثاء"],["يوم الاربعاء"],["يوم الخميس"],['الرجوع للخلف']],
                             'one': True, 'two': True, 'three': True, 'for': True, 'five': True})
json_keyboard6 = json.dumps({'keyboard': [["تعليم الاكتروني"],['قواعد بيانات'],['هندسة برمجيات'],['تقنيات المصادر المفتوحة'],['البرمجة الغرضية الموجهه']],
                             'one': True, 'two': True, 'three': True})
bot = telepot.Bot('472639184:AAGUVPX8oZqYUJXts40Kq2tUO95dB4_D094')


def handle(msg):
    chat_id = msg['chat']['id']
    chat_username = msg['chat']['username']
    command = msg['text']
    conn = db.create_connection(database)
    print ('Got command: %s' % command)
    with conn:
        if chat_id == 330750673:
            if command == "/start":
                a = " أهلا"
                c = " السلام عليكم ورحمة الله وبركاتة أتمنى أن تكون بأفضل حال "
                v = " يسعدني ويشرفني خدمتك \n أنا البوت الخاص ببنك الطالب"
                h = " ملاحظة: في حالة لم يلبي البوت غرضك فضلا قم بالتواصل معنى على الايميل الخاص بالدعم الفني nsadec@gmail.com"
                b = "فضلا قم بإختيار زر الاشتراك للاشتراك في خدمة التذكير بمواعيد الامتحانات"
                start = "{}\t{}\n{}\n{}\n{}\n\n\n\n{}".format (a, chat_username, c, v, b, h)
                bot.sendMessage (chat_id, start, reply_markup=json_keyboard4)
            elif command == "مشرف":
                        bot.sendMessage(chat_id, "فضلا اختر المقرر", reply_markup=json_keyboard3)
            elif command == command:
                    if command == "الرجوع للخلف":
                        bot.sendMessage(chat_id, "الصفحة الرئيسية", reply_markup=json_keyboard4)
                    if command == "/start":
                        bot.sendMessage(chat_id, "الصفحة الرئيسية", reply_markup=json_keyboard4)
                    n = db.select_data(conn, '*', 'subscription', " coursename = '{}'".format(command),fetchall=True)
                    if n == None:
                        bot.sendMessage(chat_id, "عفوا هذه المادة غير موجودة في قائمتي", reply_markup=json_keyboard3)

                    else:
                        for a in n:
                            print(a[0])
                            v = "اهلا "
                            f = "هذا تذكير مني انا بوت بنك الطالب باختبارك والذي سوف يكون غداً في مادة {}".format(command)
                            bot.sendMessage(a[0], '{}{}'.format(v, f),reply_markup=json_keyboard3)
        else:
            if command == "/start":
                a = " أهلا"
                c = " السلام عليكم ورحمة الله وبركاتة أتمنى أن تكون بأفضل حال "
                v = " يسعدني ويشرفني خدمتك \n أنا البوت الخاص ببنك الطالب"
                h = " ملاحظة: في حالة لم يلبي البوت غرضك فضلا قم بالتواصل معنى على الايميل الخاص بالدعم الفني nsadec@gmail.com"
                b = "فضلا قم بإختيار زر الاشتراك للاشتراك في خدمة التذكير بمواعيد الامتحانات"
                start = "{}\t{}\n{}\n{}\n{}\n\n\n\n{}".format(a, chat_username, c, v, b, h)
                bot.sendMessage(chat_id, start, reply_markup=json_keyboard)
            elif command == command:
                if command == "جدول الاختبارات" or  command == "جميع الايام" :
                    n = db.select_data(conn, '*', 'exams',None, fetchall=True)
                    if n is not None:
                        print(n)
                        for a in n:
                            g = a[0]
                            o = a[1]
                            f = a[2]
                            p = "_______________________________________________"
                            h = '{}\t\t\t{}\t\t\t{}\n{}\n'.format(g, o, f, p)
                            bot.sendMessage(chat_id, h, reply_markup=json_keyboard5)
                elif command == "يوم الاحد" or command  == "يوم الاثنين" or command == " يوم الثلاثاء" or command ==  "يوم الاربعاء" or command == "يوم الخميس":
                    n = db.select_data(conn, '*', 'exams', "day = '{}'".format(command), fetchall=True)
                    if n is not None:
                        print(n)
                        for a in n:
                            g = a[0]
                            o = a[1]
                            f = a[2]
                            p = "_______________________________________________"
                            h = '{}\t\t\t{}\t\t\t{}\n{}\n'.format(g, o, f, p)
                            bot.sendMessage(chat_id, h, reply_markup=json_keyboard5)
                elif command == "اشترك في خدمة ذكرني بإمتحاني":
                    bot.sendMessage(chat_id, "فضلا اختر احدى المواد الموجدة في القائمة", reply_markup=json_keyboard6)
                if command == command:
                    n = db.select_data(conn, '*', 'subscription', "id = '{}' and coursename = '{}'".format(chat_id,command), fetchall=False)
                    if n is not None:
                        bot.sendMessage(chat_id, "انت مشترك في هذه المادة", reply_markup=json_keyboard6)
                    else:
                        db.insert_date(conn, 'subscription', "id, coursename",
                                       "'{}','{}'".format(chat_id,command))
                        bot.sendMessage(chat_id, "شكرا لك تم اشتراكك بنجاح", reply_markup=json_keyboard6)
                elif command == "الرجوع للخلف":
                            bot.sendMessage(chat_id, "", reply_markup=json_keyboard)

                elif command == command:
                    n = db.select_data(conn, 'mass', 'sbot', "send = '{}'".format(command), fetchall=False)
                    if n is not None:
                        print(n)
                        for a in n:
                            print(n)
                            db.insert_date(conn, 'bot', "send, mass,user,id, time",
                                           "'{}','{}','{}','{}', '{}'".format(command, a, chat_username,
                                                                              chat_id, tim))
                            bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
                    else:
                        bot.sendMessage(chat_id,
                                        ' لم اعرف ماذا تريد، إختر "وجهني" أو "ماهذا البوت" حتى أستطيع مساعدتك',
                                        reply_markup=json_keyboard1)

            else:
                bot.sendMessage(chat_id,
                                ' لم اعرف ماذا تريد، إختر "وجهني" أو "ماهذا البوت" حتى أستطيع مساعدتك',
                                reply_markup=json_keyboard1)


MessageLoop (bot, handle).run_as_thread ()
while 1:
    time.sleep (1)