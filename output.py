def Output(words):
    output = ''
    ret = []
    output += words[0] + '\t' + words[1] + '\t' + words[2] + '\n'

    i = 3
    while i < len(words):
        if not words[i].isdigit():
            output += words[i]
            ret.append(words[i])
            if len(words[i]) == 2:
                output += '\t\t'
            else:
                output += '\t'
            i = i + 1
            if words[i].isdigit():
                output += words[i] + '\t\t' + words[i+1] + '\n'
                ret.extend([words[i], words[i+1]])
                i = i + 2
            else:
                output += '缺\t\t缺\n'
                ret.extend(['缺', '缺'])
    print(output)
    return ret
