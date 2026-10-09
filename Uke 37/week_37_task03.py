# Zodiac sign from birthday

import pandas as pd

file_path = "/Users/mariefjellbakk-edfeldt/Library/CloudStorage/OneDrive-NorwegianUniversityofLifeSciences/INF201/Uke 37/zodiac_signs.csv"
# fikk file path ved å kopiere fra filen
data_frame = pd.read_csv(file_path, sep=";")
print(data_frame)

birthday = "May 28"
def find_zodiac_sign_and_compatibility(birthday, data_frame): # definerer funksjon med input bursdag og data_frame
    month, day = birthday.split() # deler opp bursdagen i måned og dag
    day=int(day) # gjør om dag til integer

    for index, row in data_frame.iterrows():
        sign_start, sign_end = row["date_range"].split("-") # splitter datoen for start og slutt på stjernetegnet
        start_month, start_day = sign_start.split() # deler opp startdatoen i måned og dag
        end_month, end_day = sign_end.split() # deler opp sluttdatoen i måned og dag

        if ((month == start_month and day >= int(start_day)) or (month == end_month and day <= int(end_day))):
            # hvis mnd er startmåned og dagen er større eller lik startdagen for stjernetegnet, eller mnd er sluttmåned og mindre eller lik sluttdato
            zodiac_sign = row["zodiac_sign"]
            # så er stjernetegnet den radens stjernetegn
            break
    print("Zodiac sign:", zodiac_sign) # printer stjernetegn

    for index, row in data_frame.iterrows():
        if zodiac_sign == row["zodiac_sign"]:
            compatibility = row["compatible"] 
            print("Compatible with:",compatibility)

    for index, row in data_frame.iterrows():
            if zodiac_sign == row["zodiac_sign"]:
                incompatibility = row["incompatible"] 
                print("Incompatible with:", incompatibility)

find_zodiac_sign_and_compatibility(birthday, data_frame)



