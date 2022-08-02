

filename = "data_sprav.txt" 
myfile = open(filename, "a+") 
myfile.close 

def searchcontact(): 
    searchname = input( "Введите имя для поиска контактной записи: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print( "Ваша необходимая контактная информация - это:", end = " ") 
            print( line) 
            found = True 
            break 
    if found == False: 
        print( "Искомый контакт недоступен в телефонной книге", searchname) 

def input_firstname(): 
    first = input( "Введите свое Имя: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 

def input_lastname(): 
    last = input( "Введите свою Фамилию: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 

def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input( "Введите свой номер телефона: ") 
    emailID = input( "Введите свой адрес электронной почты: ") 
    contactDetails =("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID +  "]\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print( "Следующие Контактные Данные:\n " + contactDetails + "\nбыл успешно сохранен!") 
