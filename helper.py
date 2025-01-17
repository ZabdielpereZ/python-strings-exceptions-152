import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def d():
    print(d)
    '''' Creates a divider line in the terminal.'''
    print('-' * 50)

def fd():
    print('~'*30)

def welcome():
    print('''  
           _            _       _                                 _ 
          | |          | |     | |                               | |
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __    __ _ _ __  _ __ | |
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|  / _` | '_ \| '_ \| |
| (_| (_| | | (__| |_| | | (_| | || (_) | |    | (_| | |_) | |_) |_|
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|     \__,_| .__/| .__/(_)
                                                     | |   | |      
                                                     |_|   |_|      ''')
          
def reset():
    clear()
    welcome()

def exit():
    print('''  
 _____ _                 _           __                             _   _     _             _ 
|_   _| |               | |         / _|                           | | | |   (_)           | |
  | | | |__   __ _ _ __ | | _____  | |_ ___  _ __   _ __ ___   __ _| |_| |__  _ _ __   __ _| |
  | | | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__| | '_ ` _ \ / _` | __| '_ \| | '_ \ / _` | |
  | | | | | | (_| | | | |   <\__ \ | || (_) | |    | | | | | | (_| | |_| | | | | | | | (_| |_|
  \_/ |_| |_|\__,_|_| |_|_|\_\___/ |_| \___/|_|    |_| |_| |_|\__,_|\__|_| |_|_|_| |_|\__, (_)
                                                                                       __/ |  
                                                                                      |___/  ''')