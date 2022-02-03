def main():
    import random,secrets,sys,os,json
#DATA OF THE APP
    DB_FILE = "db.json"
    DB = json.loads(open(DB_FILE).read())["DATABASE"]
    lower_case_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_case_letters = [l.upper() for l in lower_case_letters]
    numbers = [str(i) for i in range(0,10)]
    special_characters = ['@' , '#' , '$' , '*' , '<' , ']' , '{' , '_' , '-']
    user_input = " ".join(sys.argv[1:])
    user_input_formated = user_input.split()
    options_list = ['-p' , '-u' , '-g' , '-h','--help']
    def error_messege():
        print('\nuse --help for options')
        exit()
    for i in user_input.split():
        if '-' in i and i not in options_list:error_messege()
    if user_input == "--help" or user_input == "-h":
        print("""\n    -u to set the username length\n    -p to set the password length\n    -g gender (male , female)\n    --help , -h for help\n\n    example:\n        app.py -u 20 -p 60 -g male
""")
        exit()
#subject info generator such as first name , last name and gender
    gender = random.choice(['male' , 'female'])
    first_name_gender = None
    for i in range(int(len(user_input_formated))):
        if user_input_formated[i] == '-g':gender = user_input_formated[i+1]
    if gender == 'male':first_name_gender = 'male_name'
    elif gender == 'female':first_name_gender = 'female_name'
    else:error_messege();exit()
    first_name = random.choice(DB[first_name_gender])
    last_name = random.choice(DB["family_name"])
    print(f'''$SUBJECT_INFO\n  first-name:{first_name}\n  last-name:{last_name}\n  gender:{gender}''')
#username generator
    length = random.randrange(15 , 20)
    if user_input != "":
        for i in range(int(len(user_input_formated))):
                if user_input_formated[i] == '-u':
                    length = int(user_input_formated[i+1])
    uresult = list()
    data_type = [lower_case_letters , upper_case_letters , numbers]
    for i in range(length):
        data_type_form = random.choices(data_type , weights=[21,15,2])
        char_data = secrets.choice(data_type_form[0])
        uresult.append(char_data)
    username="".join(uresult)
    print(f'''\n$USERNAME:\n  username-length: {length}\n  {username}''')
#password generator
    length = random.randrange(40 , 65)
    if user_input != "":
        for i in range(int(len(user_input_formated))):
                if user_input_formated[i] == '-p':
                    length = int(user_input_formated[i+1])
    presult = list()
    data_type = [lower_case_letters , upper_case_letters , numbers , special_characters]
    for i in range(length):
            data_type_form = secrets.choice(data_type)
            char_data = secrets.choice(data_type_form)
            presult.append(char_data)
    password="".join(presult)
    print(f'''\n$PASSWORD:\n  password-length: {length}\n  {password}''')
try:main()
except KeyboardInterrupt:print('\nKeyboard Interrupt');exit()
