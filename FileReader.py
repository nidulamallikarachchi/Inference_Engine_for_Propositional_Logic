class FileReader:
    @staticmethod
    def read(filename):
        tell = []
        ask = ''
        temp = []
        ask_found = False
        with open(filename) as f:
            for line in f:
                temp = line.strip().split(";")
                for x in temp:
                    x = x.lower()
                    if x != "" and x != "tell" and x != "ask":
                        if ask_found:
                            ask = x.replace(" ", "")
                        else:
                            tell.append(x.replace(" ", ""))
                    if x == "ask":
                        ask_found = True
        return tell, ask
