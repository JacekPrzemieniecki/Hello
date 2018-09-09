from datetime import datetime, timedelta
import os
import shutil
import sys
import time

chars = {
    'a': "     " +
         " WWW " +
         "W   W" +
         "W   W" +
         "WWWWW" +
         "W   W" +
         "W   W",
    'b': "     " +
         "WWWW " +
         "W   W" +
         "WWWW " +
         "W   W" +
         "W   W" +
         "WWWW ",
    'c': "     " +
         " WWW " +
         "W   W" +
         "W    " +
         "W    " +
         "W   W" +
         " WWW ",
    'e': "     " +
         "WWWWW" +
         "W    " +
         "WWWW " +
         "W    " +
         "W    " +
         "WWWWW",
    'h': "     " + 
         "W   W" +
         "W   W" +
         "WWWWW" +
         "W   W" +
         "W   W" +
         "W   W",
    'l': "     " +
         "W    " +
         "W    " +
         "W    " +
         "W    " +
         "W    " +
         "WWWWW",
    'o': "     " +
         " WWW " +
         "W   W" +
         "W   W" +
         "W   W" +
         "W   W" +
         " WWW ",
    ' ': "     " +
         "     " +
         "     " +
         "     " +
         "     " +
         "     " +
         "     "
}


filename = "file"
git_date = None

def git_print_start():
    global git_date
    git_date = datetime.utcnow().date() - timedelta(days=365) + timedelta(hours=12)
    while (git_date.weekday() is not 6):
        git_date = git_date + timedelta(days=1)
    if os.path.exists(filename):
        os.remove(filename);
    open(filename, 'a').close()


def git_print(active):
    global git_date

    cur_time = int(time.mktime(git_date.timetuple()))
    dt = "{0} +0000".format(cur_time)
    os.environ["GIT_AUTHOR_DATE"] = dt
    os.environ["GIT_COMMITTER_DATE"] = dt
    if active:
        with open(filename, 'a') as f:
            f.write('1')
        os.system("git add .")
        os.system("git commit -m {0}".format(cur_time))
        print('*', end='')
    else:
        print(' ', end='')
    git_date = git_date + timedelta(days=1)

def main():
    if (len(sys.argv) is not 2):
        print("usage: github_print.py <text_to_print>")
        return

    if os.path.exists(".git"):
        shutil.rmtree(".git")

    os.system("git init")

    text = sys.argv[1]
    print(text)
    git_print_start()
    print(git_date)

    textChars = [chars[c] for c in text]
    for letterIdx in range(len(textChars)):
        char = textChars[letterIdx]
        for letterCol in range(5):
            for row in range(7):
                git_print(char[row*5+letterCol] is 'W')

        for row in range(7):
            git_print(False)



if __name__ == "__main__":
    main()