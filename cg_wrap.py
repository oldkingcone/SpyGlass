from lib.shell.shells import CgShell

cg_shell = CgShell()
if __name__ == '__main__':
    while True:
        try:
            CgShell().cmdloop()
        except Exception as e:
            print(f"Please enter a valid argument\n->{e}")
            continue
