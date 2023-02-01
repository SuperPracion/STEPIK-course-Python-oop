try:
    file = open('pentagon_secrets.txt', 'r')
    print(file.read())
except:
    print('Эх, не судьба тайны пентагона узнать')