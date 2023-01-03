# Modules
import os
import random

# Check if modules are installed and installs if need
try:
    from colorama import Back, Fore, Style
    from better_profanity import profanity
    import shutil
    import pyperclip
except:
    [os.system(f'pip3 install {i}') for i in ['colorama', 'better_profanity', 'shutil', 'pyperclip']]

# Langs: en, fr, ro, fi, ua, jp, kr
# Bad words to censor
custom_badwords = [
    "bad words here"
    ]

# Version
version = "3.0"

conwidth = shutil.get_terminal_size().columns

# Green text
def green(text):
    print(Fore.GREEN + text + Style.RESET_ALL)

def center_2strings(conwidth, str1, str2):
	return print(str1 + (' ' * (conwidth // 2 - len(str1)) + ': ' + str2))

# Red text
def red(text):
    print(Fore.RED + text + Style.RESET_ALL)

# Line (--------)
def line():
    print(conwidth*"-")

def clear():
    os.system("cls")

# Languages
class en:
    title = f"Text Writer | v. {version}"
    subtitle = "Write text files!"
    fname = "File name: "
    fext = "File extension: ."
    ftext = "File text: "
    done = "Done!"
    to_continue = "Press Enter to continue"
    simple = "Simple"
    censored = "Censored"
    la = "en"

class ro:
    title = f"Text Writer | v. {version}"
    subtitle = "Scrieți fișiere text!"
    fname = "Nume fișier: "
    fext = "Extensie de fișier: ."
    ftext = "Text fișier: "
    done = "Gata!"
    to_continue = "Apăsați Enter pentru a continua"
    simple = "Simplu"
    censored = "Cenzurat"
    la = "ro"

class ua:
    title = f"Записувач тексту | v. {version}"
    subtitle = "Запис текстових файлів!"
    fname = "Назва файлу: "
    fext = "Розширення файлу: ."
    ftext = "Текст файлу: "
    done = "Готово!"
    to_continue = "Натисніть Enter, щоб продовжити"
    simple = "просто"
    censored = "Цензура"
    la = "ua"

class de:
    title = f"Text Writer | v. {version}"
    subtitle = "Textdateien schreiben!"
    fname = "Dateiname: "
    text = "Dateierweiterung: ."
    ftext = "Dateitext: "
    done = "Fertig!"
    to_continue = "Drücken Sie die Eingabetaste, um fortzufahren"
    simple = "Einfach"
    censored = "Zensiert"
    la = "de"

class fi:
    title = f"Text Writer | v. {version}"
    subtitle = "Kirjoita tekstitiedostoja!"
    fname = "Tiedoston nimi: "
    fext = "Tiedostopääte: ."
    ftext = "Tiedoston teksti: "
    done = "Valmis!"
    to_continue = "Jatka painamalla Enter"
    simple = "Yksinkertainen"
    censored = "Sensuroitu"
    la = "fi"

class fr:
    title = f"Text Writer | v. {version}"
    subtitle = "Ecrire des fichiers texte !"
    fname = "Nom du fichier : "
    fext = "Extension de fichier : ."
    ftext = "Texte du fichier : "
    done = "Terminé !"
    to_continue = "Appuyez sur Entrée pour continuer"
    simple = "Simple"
    censored = "Censuré"
    la = "fr"

class jp:
    title = f"テキスト ライター | v. {version}"
    subtitle = "テキスト ファイルを書きます!"
    fname = "ファイル名: "
    fext = "ファイル拡張子: ."
    ftext = "ファイルテキスト: "
    done = "やった！"
    to_continue = "続行するには Enter キーを押してください"
    simple = "単純"
    censored = "検閲済み"
    la = "jp"

class kr:
    title = f"텍스트 작성기 | v. {version}"
    subtitle = "텍스트 파일 쓰기!"
    fname = "파일 이름: "
    fext = "파일 확장자: ."
    ftext = "파일 텍스트: "
    done = "완료!"
    to_continue = "계속하려면 엔터를 누르세요"
    simple = "단순한"
    censored = "검열"
    la = "kr"

# Language setup
clear()
print()
green("LANGUAGE".center(conwidth))
print("Select a language to display the progam. Note: we won't add more languages in future".center(conwidth))
print("If you will type something else instead of a number from 1 to 8,".center(conwidth))
print("a random language will be selected, except korean and japanese.".center(conwidth))
green("\nAvailable languages:\n")
center_2strings(conwidth, ' 1   ' + "English", "English")
center_2strings(conwidth, ' 2   ' + "Deutsche", "German")
center_2strings(conwidth, ' 3   ' + "Français", "French")
center_2strings(conwidth, ' 4   ' + "Română", "Romanian")
center_2strings(conwidth, ' 5   ' + "Suomi", "Finnish")
center_2strings(conwidth, ' 6   ' + "Yкраїнська", "Ukrainian")
center_2strings(conwidth, ' 7   ' + "한국인", "Korean")
center_2strings(conwidth, ' 8   ' + "日本", "Japanese")
print()
line()
k = input("\n>>> ")
line()
if k == "1":
    lang = en
    x = "en"
elif k == "2":
    lang = de
    x = "de"
elif k == "3":
    lang = fr
    x = "fr"
elif k == "4":
    lang = ro
    x = "ro"
elif k == "5":
    lang = fi
    x = "fi"
elif k == "6":
    lang = ua
    x = "ua"
elif k == "7":
    lang = kr
    x = "kr"
elif k == "8":
    lang = jp
    x = "jp"
else:
    y = random.choice([en, fr, de, ro, fi, ua])
    lang = y

# Logic part
def writeFiles():
    clear()
    print("")
    green(lang.title + f" | Lang: {lang.la}".center(conwidth))
    print(lang.subtitle.center(conwidth))
    print()
    name = input(lang.fname)
    ext = input(lang.fext)
    text = input(lang.ftext)
    profanity.load_censor_words(custom_badwords)  
    censored = profanity.censor(text, "#")       
    def process():
        with open(f'{name}.{x}Lang.{ext}', 'w') as f:
            f.writelines(f"[{lang.simple}]\n{text}\n\n[{lang.censored}]\n{censored}")
    pyperclip.copy(text)
    process()
    line()
    green(lang.done)
    input(lang.to_continue)
    clear()
    writeFiles()

writeFiles()
