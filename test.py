# l = [
#     {
#         'reviewer_name' :'Michelle Isenberg', # 0
#         'amount_of_reviews': '27 მიმოხილვა', #1
#         'review_score': '5/5',#2
#         'date': '5 თვის წინ',#3
#         'posted_in': 'Google',#4
#         '-ში',#5
#         'review_content': '(თარგმნილია Google-ის მიერ) სასტუმროში ერთი ღამე ორნი ვიყავით და სრულიად კმაყოფილები დავრჩით!',
#                           'ოთახი მართლაც ძალიან დიდია, ძალიან ლამაზად მოწყობილი და სუფთა. …',
#         #6
#         'სხვა',#7
#         '1',#8
#         'გაზიარება',#9

#         'replied_by': 'მფლობელის პასუხი 5 თვის წინ', #10
#         'reply_content': ['(თარგმნილია Google-ის მიერ) Ohhhh Michelle, du machst uns glücklich mit deinem Feedback.',
#         'Und du hast das richtig gesehen, wir stellen unser Team - insbesondere an der Rezeption- grade neu zusammen. Alle hoch motiviert und offensichtlich konzentriert ;) danke für dein Verständnis und wir freuen uns dich bald wieder begrüßen zu dürfen.',

#         '',
#         'Herzlichen Gruß aus dem Aspria,', 'Sandra Schmalzried', 'Მთავარი მენეჯერი',
#         '',
#         '(ორიგინალი)',
#         'Ohhhh Michelle, du machst uns glücklich mit deinem Feedback.',
#         'Und du hast das richtig gesehen, wir stellen unser Team - insbesondere an der Rezeption- grade neu zusammen. Alle hoch motiviert und offensichtlich konzentriert ;) danke für dein Verständnis und wir freuen uns dich bald wieder begrüßen zu dürfen.',
#         '',
#         'Herzlichen Gruß aus dem Aspria,',
#         'Sandra Schmalzried',
#         'General Manager']
# },
#     [
#         'Karin Bugge',
#         '25 მიმოხილვა',
#         '5/5',
#         '2 თვის წინ',
#         'Google',
#         '-ში',
#         '(თარგმნილია Google-ის მიერ) ძალიან სასიამოვნო მიღება და ფიტნეს სტუდიის ტური იყო ძალიან სასიამოვნო.',
#         'მე და ჩემმა შეყვარებულმა მაშინვე გადავწყვიტეთ ხელშეკრულების გაფორმება. …',
#         'სხვა',
#         'მოწონება',
#         'გაზიარება',
#         'მფლობელის პასუხი 2 თვის წინ',
#         '(თარგმნილია Google-ის მიერ) მოხარულნი ვართ, რომ ჩვენმა სერვისმა კარგი შთაბეჭდილება დატოვა. კეთილი იყოს თქვენი მობრძანება ასპრიაში,',
#         'სანდრა შმალზრიედი',
#         'Მთავარი მენეჯერი',
#         '',
#         '(ორიგინალი)',
#         'Wir freuen uns, dass unser Service einen bleibenden guten Eindruck hinterlassen hat. Herzlich willkommen bei uns im Aspria,',
#         'Sandra Schmalzried',
#         'General Manager'

# ]]


reviews =[
        ['Michelle Isenberg', '27 მიმოხილვა', '5/5', '5 თვის წინ', 'Google', '-ში', '(თარგმნილია Google-ის მიერ) სასტუმროში ერთი ღამე ორნი ვიყავით და სრულიად კმაყოფილები დავრჩით!', 'ოთახი მართლაც ძალიან დიდია, ძალიან ლამაზად მოწყობილი და სუფთა. …',
        'სხვა', '1', 'გაზიარება', 'მფლობელის პასუხი 5 თვის წინ', '(თარგმნილია Google-ის მიერ) Ohhhh Michelle, du machst uns glücklich mit deinem Feedback.', 'Und du hast das richtig gesehen, wir stellen unser Team - insbesondere an der Rezeption- grade neu zusammen. Alle hoch motiviert und offensichtlich konzentriert ;) danke für dein Verständnis und wir freuen uns dich bald wieder begrüßen zu dürfen.',
        '', 'Herzlichen Gruß aus dem Aspria,', 'Sandra Schmalzried', 'Მთავარი მენეჯერი', '', '(ორიგინალი)', 'Ohhhh Michelle, du machst uns glücklich mit deinem Feedback.', 'Und du hast das richtig gesehen, wir stellen unser Team - insbesondere an der Rezeption- grade neu zusammen. Alle hoch motiviert und offensichtlich konzentriert ;) danke für dein Verständnis und wir freuen uns dich bald wieder begrüßen zu dürfen.',
        '', 'Herzlichen Gruß aus dem Aspria,', 'Sandra Schmalzried', 'General Manager'
        ],
        ['Karin Bugge', '25 მიმოხილვა', '5/5', '2 თვის წინ', 'Google', '-ში', '(თარგმნილია Google-ის მიერ) ძალიან სასიამოვნო მიღება და ფიტნეს სტუდიის ტური იყო ძალიან სასიამოვნო.', 'მე და ჩემმა შეყვარებულმა მაშინვე გადავწყვიტეთ ხელშეკრულების გაფორმება. …',
         'სხვა', 'მოწონება', 'გაზიარება', 'მფლობელის პასუხი 2 თვის წინ', '(თარგმნილია Google-ის მიერ) მოხარულნი ვართ, რომ ჩვენმა სერვისმა კარგი შთაბეჭდილება დატოვა. კეთილი იყოს თქვენი მობრძანება ასპრიაში,', 'სანდრა შმალზრიედი', 'Მთავარი მენეჯერი',
         '', '(ორიგინალი)', 'Wir freuen uns, dass unser Service einen bleibenden guten Eindruck hinterlassen hat. Herzlich willkommen bei uns im Aspria,', 'Sandra Schmalzried', 'General Manager'
        ],
        ['Alina', '1 მიმოხილვა', '1/5', '5 თვის წინ', 'Google', '-ში', '(თარგმნილია Google-ის მიერ) შაბათიდან კვირამდე აქ ვიყავით ბავშვთან ერთად (4 თვე). საუზმე კატასტროფა იყო ფასისთვის! თონეში უკეთესობისკენ შეგეძლო. თავხედობა!!! წინა მაგიდაც საკმაოდ გადატვირთული დაგვხვდა და ამას ძალიან დიდი დრო დასჭირდა. …',
         'სხვა', '3', 'გაზიარება', 'მფლობელის პასუხი 5 თვის წინ', '(თარგმნილია Google-ის მიერ) გამარჯობა ალინა, უპირველეს ყოვლისა გმადლობთ, რომ დრო დაუთმეთ და გვითხარით თქვენი შთაბეჭდილებები.',
        'ძალიან ვწუხვარ, რომ ჩვენ ნამდვილად ვერ გავამართლეთ თქვენი მოლოდინი ჩვენი ფიტნეს და გამაჯანსაღებელი სასტუმროთ. ჩვენ ვაფიქსირებთ თქვენს ქულებს და სიამოვნებით ვამოწმებთ მათ ოპტიმიზაციის ვარიანტებისთვის.', '', 'Საუკეთესო სურვილებით', 'სანდრა შმალზრიედი', 'Მთავარი მენეჯერი',
        '', '(ორიგინალი)', 'Hallo Alina, erstmal danke für die Zeit uns eure Eindrücke zu schildern.', 'Tut mir sehr leid, dass wir mit unserem Fitness- und Wellness Hotel nicht wirklich euren Erwartungen gerecht werdenkonnten. Eure Punkte nehmen wir auf und prüfen diese gerne bzgl. Optimierungsmöglichkeiten.',
        '', 'Mit den besten Grüßen', 'Sandra Schmalzried', 'General Manager'
        ],
        ['Ka Ba', '7 მიმოხილვა', '4/5', '3 თვის წინ', 'Google', '-ში', '(თარგმნილია Google-ის მიერ) იქ პირველად ვიყავი. ძალიან ლამაზი თანამედროვე დაწესებულება, კარგი პერსონალი, საუკეთესო ფიტნეს დარბაზი და მასაჟი ასევე ძალიან კარგი იყო. მთლიანობაში კარგი კონცეფციაა და ადგილი, სადაც უნდა წახვიდე, როცა შესვენება …',
         'სხვა', 'მოწონება', 'გაზიარება', 'მფლობელის პასუხი 3 თვის წინ', '(თარგმნილია Google-ის მიერ) ოჰჰჰჰ, ჩვენ გავარკვევთ, არის თუ არა ამის გამოსავალი.', '', 'გმადლობთ სასიამოვნო დეტალური გამოხმაურებისთვის,', 'სანდრა შმალზრიედი', 'Მთავარი მენეჯერი', 'ასპრია ბერლინი', '', '(ორიგინალი)', 'Ohhhhh, wir machen uns schlau, ob es hierfür ne Lösung gibt.',
         '', 'Vielen Dank für das schöne ausführliche Feedback,', 'Sandra Schmalzried', 'General Manager', 'Aspria Berlin'
         ],
        ['Gerry Rome', '6 მიმოხილვა', '2/5', 'ერთი თვის წინ', 'Google', '-ში', "Just to make it clear I am writing a review on the gym and not the hotel. I have been a gym member for the past two years. I became a member because the manager insured me that they don't allow aggressivepeople to enrol. Two years after …",
         'სხვა', '3', 'გაზიარება', 'მფლობელის პასუხი 4 კვირის წინ', '(თარგმნილია Google-ის მიერ) საღამო მშვიდობისა გერი, გმადლობთ მიმოხილვისთვის და თქვენი შეშფოთებისთვის. ძალიან ვწუხვარ, რომ თქვენ განიცადეთ სიტუაციები, რამაც დისკომფორტი შეგაწუხათ. მე და ჩემი გუნდი სამუშაო საათებში ადგილზე ვართ და სიამოვნებით მივიღებთ პირდაპირ რჩევას. რა თქმა უნდა, სამწუხაროა, რომ ჩვენს სახლში არის რამდენიმე წევრი, რომლებიც არ იცავენ კლუბურ ეტიკეტს და მადლობელი იქნებიან ნებისმიერი ინფორმაციისთვის. დღე და დრო საკმარისია თქვენი ქულების განსახორციელებლად, რათა შემცირდეს ცალკეული პირები/ჯგუფები. მე და ჩემი გუნდი მოხარული ვიქნებით დაგელაპარაკებით პირადად და მადლობელი ვიქნებით, თუ გამოიყენებთ შესაძლებლობას და დატოვოთ უფრო კონკრეტული ინფორმაცია წევრობის სერვისში ან ელექტრონული ფოსტით: blnmemberservice@aspria.de ან მენეჯმენტი SandraSchmalzried, რადგან ბოლო რამდენიმე თვე იყო მცირე ან საერთოდ არ ყოფილა კონკრეტული გამოხმაურება თქვენ მიერ აღნიშნულ საკითხებზე.',
         'თუმცა, მე ასევე შევნიშნე დადებითი ასპექტები და გმადლობთ, რომ ახსენეთ ისინი თქვენს გამოხმაურებაში. დარწმუნებული არ ვარ, ვინ მოგცათ გარანტია წინასწარ იდენტიფიცირება და უარყო წევრები, რომლებიც არასწორად იქცევიან, მაგრამ შემიძლია დაგარწმუნოთ, რომ ჩვენ მივყვებით ნებისმიერ მითითებებს, რათა მივცეთ ჩვენი წევრები და სტუმრები კლუბში დასასვენებლად.',
         '', 'ასპრიასთბილი მოკითხვით', 'სანდრა შმალზრიედი', 'Მთავარი მენეჯერი', '', '(ორიგინალი)', 'Einen schönen guten Abend Gerry, vielen Dank für Ihre Rezension und Äußern Ihrer Bedenken. Es tut mir sehr leid, dass Sie Situationen erlebten, die bei Ihnen Unbehagen ausgelöst haben. Mein Team und ich sind während der Öffnungszeiten vor Ort und nehmen gerne direkt Hinweise entgegen. Natürlich ist es bedauerlich, dass es vereinzelt Mitglieder in unserem Hause gibt, die sich wohl nicht an die Etikettedes Clubs halten und sind hier für jeden Hinweis dankbar. Es reicht Tag und Uhrzeit aus um Ihren Punkten nachzugehen um die einzelnen Personen / -gruppen einzugrenzen. Mein Team und ich würden uns sehr gerne persönlich mit Ihnen unterhalten und wären Ihnen sehr verbunden, wenn Sie die Möglichkeit nutzen, konkretere Infos beim Membership Service oder per email:blnmemberservice@aspria.de oder Management Sandra Schmalzried zu hinterlassen, da in den letzten Monaten zu den von Ihnen genannten Punkten kaum bis gar keine konkreteren Rückmeldungen eingegangen sind. ', 'Durchaus habe ich aber auch die positiven Aspekte wahrgenommen und danke Ihnen, dass Sie diese in Ihrem Feedback nicht unerwähnt lassen. Ich bin mir nicht sicher, wer Ihnen die Sicherheit gegeben hat, Mitglieder ohne Benehmen vorab zu erkennen und den Zutritt zu verwehren, kann Ihnen aber versichern, dass wir jedem Hinweis nachgehen um unseren Mitgliedern und Gästen im Club einen Ort der Entspannung zu bieten. ', '', 'Mit einem herzlichen Gruß aus dem Aspria', 'Sandra Schmalzried', 'General Manager'],
        ['Nici Theuerkauf', '3 მიმოხილვა', '1/5', '2 თვის წინ', 'Google', '-ში', '(თარგმნილია Google-ის მიერ) სირცხვილია, ყველაფერი, რისთვისაც ეს კლუბი ოდესღაც იდგა, წავიდა. მართლაც კარგი მასწავლებლები იყვნენ და კურსების საოცარი სპექტრი, ახლა საკმაოდ საშუალოა. აუდიტორია ძალიან პროლეტარულია... გაშტერებული, ამაზრზენი …', 'სხვა', '5', 'გაზიარება', 'მფლობელის პასუხი 2 თვის წინ', '(თარგმნილია Google-ის მიერ) ძვირფასო ქალბატონო თეუერკაუფ, ჩვენ ძალიან სერიოზულად ვითვალისწინებთ ინფორმაციას ჩვენი წევრებისა და სტუმრებისგან, როგორც კი ის ეცნობება წევრების სამსახურებს ან ხელმძღვანელობას ან გახდება ცნობილი. საუნის ოსტატები ადგილზე არიან პირდაპირი საჩივრების მისაღებად. თუმცა, ჯერჯერობით, ჩვენ არ მიგვიღია რაიმე გამოხმაურება თქვენი დაკვირვების შესახებ. იმისათვის, რომ ვიმოქმედოთ, სასწრაფოდ გვჭირდება მეტი ინფორმაცია. გთხოვთ დაუკავშირდეთ ჩვენი წევრების სერვისს აქ კლუბში.',
        '', 'გმადლობთ გამოხმაურებისთვის და ძალიან ვწუხვართ, რომ კლუბი აღარ პასუხობს თქვენს მოლოდინებს და იდეებს და რომ საუნაში თქვენი ყოფნა შეფერხდა.', '', 'ძალიან დიდი მადლობა', 'სანდრა შმალზრიედი', 'Მთავარი მენეჯერი', '', '(ორიგინალი)', 'Sehr geehrte Frau Theuerkauf, wir nehmen Hinweise unserer Mitglieder und Gäste sehr ernst, sobald es dem Mitgliederservice oder dem Management zugetragen wird bzw. zur Kenntnis gelangt. Saunameister sind vor Ort um direkte Beschwerden entgegen zu nehmen. Bisher wurde uns jedoch zu Ihren Beobachtungen noch keine Rückmeldungen gegeben. Um agieren zu können benötigen wir dringend mehr Informationen. Bitte wenden Sie sich doch an unseren Mitgliederservice hier im Club.',
        '', 'Wir danken für Ihre Rückmeldung und bedauern es sehr, dass der Club nicht mehr Ihren Erwartungen und Vorstellungen entspricht und Ihr Saunaaufenthalt gestört worden ist.', '', 'Herzlichen Dank', 'Sandra Schmalzried', 'General Manager'
        ],
        ['Sabine hamburg', '5 მიმოხილვა', '2/5', '5 თვის წინ', 'Google',
        '-ში', '(თარგმნილია Google-ის მიერ) საცურაო აუზი რემონტის პროცესში იყო, მაგრამ სწორედ ამიტომ დავჯავშნე სასტუმრო. დაგვიანებით გადახდა არ გადაირიცხა, სამაგიეროდ, უხეში სატელეფონო ზარი მივიღე. ხედი ოთახიდან: ბინძური სახურავი სიგარეტის ნამწვით. საუზმე …',
        'სხვა', '2', 'გაზიარება'
        ]
]

import json
from config import review_fields as fields


def scrap_data():

    review_data = list()
    google_review = []

    for i in range(len(reviews)):
        review = {}
        review_data = reviews[i]
        for field, id in fields.items():
            if isinstance(id, list):
                review[field] = '\n'.join(review_data[id[0]:id[1]])
            elif id < len(review_data):
                review[field] = review_data[id]

        google_review.append(review)

    print(json.dumps(google_review, indent=4))
    # return self.google_review

scrap_data()