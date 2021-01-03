from termcolor import colored, cprint


def main():
    print('STDOUT')
    return 'RETURN'

def color():
    cprint('STDOUT', 'green')
    text = colored('RETURN', 'red')
    return text
