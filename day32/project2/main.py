import datetime as dt
import pandas
import random

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {
    (row["month"], row["day"]): row for (index, row) in data.iterrows()
}

if today in birthdays_dict:
    person = birthdays_dict[today]["name"]
    letter_file = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(letter_file, "r") as template_file:
        contents = template_file.read()
        new_letter = contents.replace("[NAME]", person)

# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



