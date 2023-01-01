import os

try:
    from colorama import Back, Fore, Style
    from better_profanity import profanity
    import shutil
except:
    [os.system(f'pip3 install {i}') for i in ['colorama', 'better_profanity', 'shutil']]

custom_badwords = [
    "your",
    "custom",
    "badwords"
    ]

version = "1.0"

conwidth = shutil.get_terminal_size().columns

def green(text):
    print(Fore.GREEN + text + Style.RESET_ALL)

def line():
    print(conwidth*"-")

def clear():
    os.system("cls")

def writeFiles():
    clear()
    print("")
    green(f"Text Writer | v. {version}".center(conwidth))
    print("Write text files!".center(conwidth))
    name = input("\nFile name: ")
    ext = input("File extenstion: .")
    text = input("Your text: ")
    profanity.load_censor_words(custom_badwords)  
    censored = profanity.censor(text, "#")       
    def process():
        with open(f'{name}.{ext}', 'w') as f:
            f.writelines(censored)
    process()
    line()
    green("Done!")
    input("Press Enter to continue")
    clear()
    writeFiles()

writeFiles()
