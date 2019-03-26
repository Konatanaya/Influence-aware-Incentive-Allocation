
class FileIO:
    def readdata(self):
        try:
            file = open('data/new12831.edges','r')
            print(file.read())
        finally:
            if file:
                file.close()
