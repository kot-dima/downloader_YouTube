import youtube_dl as ud

from subprocess import call

while True:
    load = int(input("Hello in Youtube downloader \n 1. Doownload 1 video \n 2. Download playlist \n 3. Show \n 4. Download music \n 0. Exit \n"))
    def downloader(call):
        Urladres = input("Enter URL :")
        command = "youtube-dl " + Urladres + " -c"
        call(command.split(), shell=True)
    def downloader_f(call):
        Urladress = input("Enter URL :")
        command_1 = "youtube-dl -F " + Urladress
        call(command_1.split(), shell=True)
        enter_format = input("Enter format :")
        command_2 = "youtube-dl -f " + enter_format + " " + Urladress + " -c"
        call(command_2.split(), shell=True)
    def downloader_x(call):
        Urladres_a = input("Enter URL :")
        command_3 = "youtube-dl -f bestaudio " + Urladres_a
        call(command_3.split(), shell=True)
    if load == 1:
        downloader(call)
    elif load == 2:
        downloader(call)
    elif load == 3:
        downloader_f(call)
    elif load == 4:
        downloader_x(call)
    elif load == 0:
        break
    else:
        print("Print 1 / 2 / 3...")

