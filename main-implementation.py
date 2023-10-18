import datetime as dt
import smtplib
import pandas
import random

my_email = '-'
password = '-'

current = dt.datetime.now()
today = (current.month, current.day)
print(today)

birthday_df = pandas.read_csv('birthdays.csv')
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthday_df.iterrows()}

if today in birthday_dict :
    num_letter = random.randint(1,3)
    receipent = birthday_dict[today].Name
    relative_path = f'letter_templates/letter_{num_letter}.txt'
    with open(relative_path, "r") as letterfile :
        letter = letterfile.read()
        letter_to_send = letter.replace('[NAME]', f'{receipent}')
        # print(letter_to_send)

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection :
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=birthday_dict[today].email, 
            msg=f"Subject:Happy Birthday!\n\n{letter_to_send}"
            )


