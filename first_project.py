import json
import time
from time import strftime

import telepot
from telepot.loop import MessageLoop

from database import db


tim = strftime("%Y/%B/%d %I:%M%p")
database = "/home/nsadec/PycharmProjects/StudentBank/database/ksu.db"
json_keyboard = json.dumps({'keyboard': [["اشترك في التذكير للامتحانات"]],
                            'one': False, 'two': True, 'three': True})
bot = telepot.Bot('472639184:AAGUVPX8oZqYUJXts40Kq2tUO95dB4_D094')


def handle(msg):
    chat_id = msg['chat']['id']
    chat_username = msg['chat']['username']
    command = msg['text']
    subscribe = "اشترك في التذكير للامتحانات"
    Suggestion = "اقتراح"

    print('Got command: %s' % command)
    if command == "/start":
        a = " أهلا"
        c = " السلام عليكم ورحمة الله وبركاتة أتمنى أن تكون بأفضل حال "
        v = " يسعدني ويشرفني خدمتك \n أنا البوت الخاص ببنك الطالب"
        h = " ملاحظة: في حالة لم يلبي البوت غرضك فضلا قم بالتواصل معنى على الايميل الخاص بالدعم الفني nsadec@gmail.com"
        b = "فضلا قم بإختيار زر الاشتراك للاشتراك في خدمة التذكير بمواعيد الامتحانات"
        start = "{}\t{}\n{}\n{}\n{}\n\n\n\n{}".format(a, chat_username, c, v, b, h)
        bot.sendMessage(chat_id, start, reply_markup=json_keyboard)

    elif command == "السلام" or command == "السلام عليكم" or command == "السلام عليكم ورحمة الله ويركاته":
        a = "وعليكم السلام ورحمة الله وبركاته \nأهلا بك تفضل انا أنا البوت الخاص ببنك الطالب\nكيف اقدر أخدمك"
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type, user,id,time", "'{}','{}','{}', '{}','{}','{}'".
                           format(command, a, command, chat_username, chat_id, tim))

    elif command == subscribe:
        a = "شكرا لاشتراكك في خدمة ذكرني\n فضلاً اكتب رقم المادة المراد الاشتراك فيها من القائمة أدناه"
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type,user,id, time", "'{}','{}','{}','{}', '{}','{}'"
                           .format(subscribe, a, subscribe, chat_username, chat_id, tim))

    elif command == "من أنت" or command == "من انت":
        a = "أنا البوت الخاص ببنك الطالب لقد قام ببرمجتني الطالبة نورة الوابل كيف ممكن اخدمك "
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type,user,id,time",
                           "'{}','{}','{}','{}', '{}','{}'".format(Suggestion, a, Suggestion, chat_username, chat_id,
                                                                   tim))
            
    elif command == "وش بنك الطالب هذا" or command == "وش هذا بنك الطالب" or command == "وش هذا البوت" or command == "ماهذا البوت":
        a = "بنك الطالب هو مشروع صغير يخزن المصادر المهمة لبعض المواد الدراسية "\
            "حالياً لدينا المصادر الخاصة بمادتي تقنيات المصادر المفتوحة 542، وهندسة البرمجيات 323"\
            ""\
            "كذلك بنك الطالب يقدم خدمة ذكرني، للتذكير بمواعيد الامتحانات الخاصة بالمود المتاحة للاشتراك"\
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type,user,id,time",
                           "'{}','{}','{}','{}', '{}','{}'".format(Suggestion, a, Suggestion, chat_username, chat_id,
                                                                   tim))
    elif command == "نورة":
        a = "اهلا انا لست نورة انا البوت الخاص ببنك الطالب"
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type,user,id,time",
                           "'{}','{}','{}','{}', '{}','{}'".format(Suggestion, a, Suggestion, chat_username, chat_id,
                                                                   tim))
            
    elif command == "مادة" or command == "كورس":
        a = "ماهو اسم المادة"
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type,user,id,time",
                           "'{}','{}','{}','{}', '{}','{}'".format(Suggestion, a, Suggestion, chat_username, chat_id,
                                                                   tim))
            
    elif command == "وش المواد المتاحة مصادرها" or command == "وش المواد الموجودة" or command == "وش الكورسات المتوفرة" or command == "أسماء الكورسات المتاحة":
        a = "حالياً لدينا المصادر الخاصة بمادتي تقنيات المصادر المفتوحة 542، وهندسة البرمجيات 323"
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type,user,id,time",
                           "'{}','{}','{}','{}', '{}','{}'".format(Suggestion, a, Suggestion, chat_username,
                                                                   chat_id,
                                                                   tim))
    elif command == "وش تقصد بالمصادر" or command == "ماذا تعني بالمصادر" or command == "ماهي المصادر اللتي قد أحصل عليها" or command == "زودني بالمصادر":
        a = "المصادر اللتي نملكها: الكتاب الخاصة بالمادة، توصيف المقرر، الشرائح الخاصة بالدكتور"
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type,user,id,time",
                           "'{}','{}','{}','{}', '{}','{}'".format(Suggestion, a, Suggestion, chat_username, chat_id,
                                                                   tim))
            
    elif command == "وجهني":
        a = "اكتب اسم المقرر الذي تحتاج مصادره"\
            "تقنيات المصادر المفتوحة"\
            "هندسة البرمجيات"
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type,user,id,time",
                           "'{}','{}','{}','{}', '{}','{}'".format(Suggestion, a, Suggestion, chat_username, chat_id,
                                                                   tim))
            
    elif command == "Open Source" or command == "اوبن سورس" or command == "المصادر المفتوحة" or command == "تقنيات المصادر المفتوحة" or command == "547" or command == "IT 547" or command == "Open Source Technology" :
        a = "حدد المصدر الذي تريده"\
            "توصيف المصادر المفتوحة"\
            "المرجع الخاص بالمصادر المفتوحة"\
            "الشرائح الخاصة بالمصادر المفتوحة"
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type,user,id,time",
                           "'{}','{}','{}','{}', '{}','{}'".format(Suggestion, a, Suggestion, chat_username, chat_id,
                                                                   tim))

    elif command == "توصيف المصادر المفتوحة" or command == "توصيف اوبن سورس" or command == "توصيف مقرر المصادر المفتوحة":
        a = "توصيف المقرر: يهدف المقرر إلى تعريف الطالبة بتاريخ المصادر المفتوحه والنظام الإيكولوجي (ecosystem)، " \
            "وتزويدها بالمفاهيم المتعلقة بتراخيص البرمجيات الحرة والمصادر المفتوحه، وتكييف برمجيات المصادر المفتوحة " \
            "،وكذلك أساليب إنتاج برمجيات المصادر المفتوحة، بالإضافة إلى أدوات وتقنيات المصادر المفتوحة والتوجه " \
            "المستقبلي لتطورها. "\
            ""\
            ""\
            ""\
            ""
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type,user,id,time",
                           "'{}','{}','{}','{}', '{}','{}'".format(Suggestion, a, Suggestion, chat_username, chat_id,
                                                                   tim))
            
    elif command == "المرجع الخاص بالمصادر المفتوحة" or command == "كتاب الاوبن سورس" or command == "كتاب مقرر المصادر المفتوحة":
        a = "تفضل رابط التحميل" \
            "https://drive.google.com/file/d/1kXIkPqUS5My-24HyPgzufUpMoYZkLUHO/view?usp=sharing"\
            "https://drive.google.com/file/d/1kD3NPdBVlQNc-RNC3iBMtwla0c4YWJzT/view?usp=sharing"\
            ""
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type,user,id,time",
                           "'{}','{}','{}','{}', '{}','{}'".format(Suggestion, a, Suggestion, chat_username, chat_id,
                                                                   tim))
    
    elif command == "الشرائح الخاصة بالمصادر المفتوحة" or command == "الفصول الخاصة بالاوبن سورس" or command == "اوبن سورس تشابترز":
        a = "تفضل رابط التحميل" \
            "http://www.mediafire.com/file/l62soykp2dsg890/Chapters%20Open%20source.zip"\
            ""
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type,user,id,time",
                           "'{}','{}','{}','{}', '{}','{}'".format(Suggestion, a, Suggestion, chat_username, chat_id,
                                                                   tim))
    
    elif command == "software engineer" or command == "سوفتوير" or command == "هندسة" or command == "هندسة البرمجيات" or command == "323" or command == "IT 323" or command == "Software Engineer" :
        a = "حدد المصدر الذي تريده"\
            "توصيف هندسة البرمجيات"\
            "المرجع الخاص بهندسة البرمجيات"\
            "الشرائح الخاصة بهندسة البرمجيات"
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type,user,id,time",
                           "'{}','{}','{}','{}', '{}','{}'".format(Suggestion, a, Suggestion, chat_username, chat_id,
                                                                   tim))
            
    elif command == "توصيف هندسة البرمجيات" or command == "توصيف سوفتوير" or command == "توصيف مقرر هندسة البرمجيات" or command == "توصيف المقرر لهندسة البرمجيات":
        a = "يتبع المقرر مقرر هندسة البرامج-1 حيث أنه يستمر في دراسة دورة حياة تطوير البرامج"\ 
            "ستتمكن الطالبات من معاينة والتمكن من المراحل المتبقية من دورة حياة تطوير البرامج. "\
            "بدءا من لمحة مفصلة عن علميات البرمجة ومراجعة ما قد تم تعلمه في المقرر السابق ، "\
            "ستتعرض الطالبات لتغطية متعمقةلمفاهيم التصميم والتي لم يتم تقديمها في هندسة البرامج I،"\
            "بما في ذلك التصميم المعماري ومباديء تصميم الواجهة. بعد ذلك سيتعرض المقرر لطرق مختلفة لتطوير البرامج،"\
            "بما في ذلك التطوير السريع للبرامج، البرمجة المفرطة، وهندسة البرامج المعتمدة على العناصر."\
            "كما يقدم المقرر بعد ذلك فاعلية البرامج والتحقق منها بما في ذلك عمليات التفتيش ومختلف تقنيات الاختبار الديناميكي."\
            "بعد وضع النظم في الاستخدام لابد من تغييرها إذا كان عليها البقاء صالحة."\
            "يعرض المقرر للطالبات عملية تطوير البرنامج و صيانة البرمجيات. تعتبر "\
            "إدارة الكود وعملية التوثيق للنظام المطور من أهم العناصر في أي تطوير برمجي، يقدم المقرر للطالبات مبادئ إدارة التغيير."\ 
            "وفي التهاية يعطي القرر لمحة موجزة عن إدارة جودة البرمجيات بما فيها مقاييس وقياسات البرامج" 
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type,user,id,time",
                           "'{}','{}','{}','{}', '{}','{}'".format(Suggestion, a, Suggestion, chat_username, chat_id,
                                                                   tim))
    elif command == "المرجع الخاص بهندسة البرمجيات" or command == "كتاب السوفتوير" or command == "كتاب مقرر هندسة البرمجيات":
        a = "تفضل رابط التحميل" \
            "http://www.mediafire.com/file/fqk3cbtbg9ah3sx/Book.pdf"\
            ""
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type,user,id,time",
                           "'{}','{}','{}','{}', '{}','{}'".format(Suggestion, a, Suggestion, chat_username, chat_id,
                                                                   tim))
    
    elif command == "الشرائح الخاصة بهندسة البرمجيات" or command == "الفصول الخاصة بهندسة البرمجيات" or command == "سوفتوير تشابترز":
        a = "تفضل رابط التحميل" \
            "http://www.mediafire.com/file/5v7l3l5vjsyujzj/Chapters%20Software%20Engineer.zip"\
            ""
        bot.sendMessage(chat_id, a, reply_markup=json_keyboard)
        conn = db.create_connection(database)
        with conn:
            db.insert_date(conn, 'bot', "send, mass, type,user,id,time",
                           "'{}','{}','{}','{}', '{}','{}'".format(Suggestion, a, Suggestion, chat_username, chat_id,
                                                                   tim))
    else:
        bot.sendMessage(chat_id, ' لم اعرف ماذا تريد، أكتب "وجهني" أو "ماهذا البوت" حتى أستطيع مساعدتك', reply_markup=json_keyboard)


MessageLoop(bot, handle).run_as_thread()
while 1:
    time.sleep(1)
