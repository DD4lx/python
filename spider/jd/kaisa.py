import urllib
from urllib import parse

def str2url(s):
    #s = '9hFaF2FF%_Et%m4F4%538t2i%795E%3pF.265E85.%fnF9742Em33e162_36pA.t6661983%x%6%%74%2i2%22735'
    num_loc = s.find('h')
    rows = int(s[0:num_loc])
    strlen = len(s) - num_loc
    cols = int(strlen/rows)
    right_rows = strlen % rows
    new_s = list(s[num_loc:])
    output = ''
    for i in range(len(new_s)):
        x = i % rows
        y = i / rows
        p = 0
        if x <= right_rows:
            p = x * (cols + 1) + y
        else:
            p = right_rows * (cols + 1) + (x - right_rows) * cols + y
        output += new_s[int(p)]
    return parse.unquote(output).replace('^', '0')


def main():
    s = "9hFx%215%E183k4E%f23t%i218E2%46%e%%5b81t2aF192F5973y55E46epFm1%%71E83F%EE-d8e%mi852671%7a36-51ca31.9EF99256uD5%6f1aA2n%22566E.t125be98%8e2116%33mh5%E3cdc2.tF9%85_7p_45-2855"
    result_str = str2url(s)
    print(result_str)

if __name__ == '__main__':
    main()
