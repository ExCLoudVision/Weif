import colorama, os
import sys

class Tee(object):
    def __init__(self, input_handle, output_handle):
        self.input = input_handle
        self.output = output_handle

    def readline(self):
        result = self.input.readline()
        self.output.write(result)

        return result
if not sys.stdin.isatty():
    sys.stdin = Tee(input_handle=sys.stdin, output_handle=sys.stdout)


colorama.init()

def clear():
    if os.name != "nt":
        os.system("clear")
    else:
        os.system("cls")

clear()
print("\n\npress ctrl + c to execute the code\n\npress weif.exit to close this session\n\npress !run to execute the code" )
def main():
    full_code = """"""
    code = input("  [ Weif ] ")
    if code.startswith("weif."):
        code = code.replace("weif.", "")
        if code == "exit":
            clear()
            exit()
        if code == "help":
            print(" - weif.exit quit this session")
            print(" - weif.save save this session (not work u can help please pull request)")
            print(" - weif.clear clear the console")
        if code == "clear":
            clear()
        if code == "save":
            path = input(" path :")
            def write():
                with open(path, 'w') as f:
                    lignes_code = full_code.split("\n")
                    for x in lignes_code:
                        f.writelines(full_code)
            try:
                write()
            except:
                open(path, "w+").close()
                write()
    else:
        
        while(1):
            try:
                buf = input("           ")
                if buf == "!run":
                    break
                code += "\n" + buf
                full_code += buf + "\n"
                
            except KeyboardInterrupt:
                break
        print("\n")
        try:
            exec(code)
        except Exception as e:
            print(e)
        print("\n")
while(1):
    main()
