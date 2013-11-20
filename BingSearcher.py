import sys, os.path, webbrowser, string, random

for i in range(30):
    webbrowser.open_new_tab("http://www.bing.com/search?setmkt=en-US&q="+"".join(random.choice(string.letters+string.digits) for x in range(random.randint(1,30))))