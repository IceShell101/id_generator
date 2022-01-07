try:
    import random
    import secrets
    import sys
    import os
    import json
#DATA OF THE APP
    DB_FILE = "db.json"
    DB = json.loads(open(DB_FILE).read())["DATABASE"]
    lower_case_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_case_letters = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    special_characters = ['@' , '#' , '$' , '*' , '<' , ']' , '{' , '_' , '-']

    user_input = " ".join(sys.argv[1:])
    user_input_formated = user_input.split()

    options_list = ['-p' , '-u' , '-g' , '-h','--help']
    def error_messege():
        print('\nuse --help for options')
        exit()
    for i in user_input.split():
        if '-' in i and i not in options_list:
            error_messege()
    if user_input == "--help" or user_input == "-h":
        print("""
    -u to set the username length
    -p to set the password length
    -g gender (male , female)
    --help , -h for help

    example:
        g_account.py -u 20 -p 60
""")
        exit()
#subject info generator such as first name , last name and gender
    gender = random.choice(['male' , 'female'])
    first_name_gender = None
    for i in range(int(len(user_input_formated))):
        if user_input_formated[i] == '-g':
            gender = user_input_formated[i+1]

    if gender == 'male':
        first_name_gender = 'male_name'
    elif gender == 'female':
        first_name_gender = 'female_name'
    else:
        error_messege()
        exit()
    first_name = random.choice(DB[first_name_gender])
    last_name = random.choice(DB["family_name"])

    print('$SUBJECT_INFO')
    print(f'  first-name:{first_name}')
    print(f'  last-name:{last_name}')
    print(f'  gender:{gender}')

#username generator
    length = random.randrange(15 , 20)
    if user_input != "":

        for i in range(int(len(user_input_formated))):
                if user_input_formated[i] == '-u':
                    length = int(user_input_formated[i+1])
    result = []
    data_type = [lower_case_letters , upper_case_letters , numbers]
    for i in range(length):
        data_type_form = random.choices(data_type , weights=[21,15,2])
        char_data = secrets.choice(data_type_form[0])
        result.append(char_data)
    username="".join(result)
    print("\n$USERNAME:")
    print(f"  username-length: {length}")
    print(f'  {username}')
            

#password generator
    length = random.randrange(40 , 65)
    if user_input != "":
        for i in range(int(len(user_input_formated))):
                if user_input_formated[i] == '-p':
                    length = int(user_input_formated[i+1])
    result = []
    data_type = [lower_case_letters , upper_case_letters , numbers , special_characters]
    for i in range(length):
            data_type_form = secrets.choice(data_type)
            char_data = secrets.choice(data_type_form)
            result.append(char_data)
    password="".join(result)
    print("\n$PASSWORD:")
    print(f"  password-length: {length}")
    print(f'  {password}')
        
except KeyboardInterrupt:
    print('\nKeyboard Interrupt')
    exit()

