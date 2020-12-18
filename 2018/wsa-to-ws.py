import sys

def main(argv):
    filename = argv[0]
    
    # read assembly
    with open(filename, "r") as wsafile:
        wsa_lines = wsafile.readlines()
    
    ws_commands = []
    # convert
    for line in wsa_lines:
        ws_commands.append(convert(line))
        
    # write to file
    print(''.join(ws_commands) + '\n\n')
    
commands = {
    'push'  : '  ',
    'dup'   : ' \n ',
    'swap'  : ' \n\t',
    'drop'  : ' \n\n',
    'add'   : '\t   ',
    'sub'   : '\t  \t',
    'mul'   : '\t  \n',
    'div'   : '\t \t ',
    'mod'   : '\t \t\t',
    'store' : '\t\t ',
    'retrieve' : '\t\t\t',
    'label' : '\n  ',
    'call'  : '\n \t',
    'jmp'   : '\n \n',
    'jz'    : '\n\t ',
    'jn'    : '\n\t\t',
    'ret'   : '\n\t\n',
    'end'   : '\n\n\n',
    'printc': '\t\n  ',
    'printi': '\t\n \t',
    'readc' : '\t\n\t ',
    'readi' : '\t\n\t\t'
}
    
def convert(line):
    line = line.strip()
    if len(line) == 0 or line.startswith('#') or line.startswith(';'):
        return ''
    if line.startswith('label_'):
        c,v = line.split('_')
        return commands[c] + convert_num(v[:-1])
    elif ' ' in line:
        c,v = line.split(' ')
        if v.startswith('label_'):
            _,v = v.split('_')
        return commands[c] + convert_num(v)
    else:
        return commands[line]
        
def convert_num(cp):
    num = int(cp)
    if num == 0:
        return '  \n'
    pos = num >= 0
    s = ''
    while num != 0:
        if num % 2 == 0:
            s += ' '
        else:
            s += '\t'
        num = int(num / 2)
    s = s[::-1]
    s = (' ' if pos else '\t') + s
    s += '\n'
    return s
    
if __name__ == "__main__":
    main(sys.argv[1:])
    
    
    
    
    