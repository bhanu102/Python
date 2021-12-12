try:
    f = open('contents.txt')
    name=bhanu
except FileNotFoundError:
    print('Sorry. This file does not exist.')
except Exception:
    print('Something went wrong')
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally')