#!/usr/bin/env python3


import unittest
import itertools
import string
import random
import strjump


class TestCase(unittest.TestCase):

    def test_compiler1(self):
        string = [
            '1:',
            strjump.Reference(1),
            ',2:',
            strjump.Reference(2),
            '|',
            strjump.Identifier(1, 'f'),
            'irst|',
            strjump.Identifier(2, 's'),
            'econd|'
        ]
        #print("String to process:", '"' + strjump.tools.repr_string(string) + '"')
        result = strjump.process(string)
        #print("Result:", '"%s"' % result)
        self.assertEqual('1:9,2:15|first|second|', result)

    def test_compiler2(self):
        string = [
            '1:',
            strjump.Identifier(1, 'f'),
            'irst,2:',
            strjump.Reference(2),
            ',|1:',
            strjump.Reference(1),
            ',|',
            strjump.Identifier(2, 's'),
            'econd|'
        ]
        #print("String to process:", '"' + strjump.tools.repr_string(string) + '"')
        result = strjump.process(string)
        #print("Result:", result)
        self.assertEqual('1:first,2:19,|1:2,|second|', result)

    #def test_compiler3(self):
    #    for _ in range(1000):
    #        n = 150
    #        base = string.ascii_lowercase + string.digits
    #        base = ''.join(base[random.randint(0, 35)] for i in range(n))
    #        i0 = random.randint(5, n / 2) - 1
    #        i1 = i0 + random.randint(5, n / 2) - 1
    #        if i1 == 10 ** (len(str(i1)) - 1):
    #            i1 -= 1
    #        ref = str(i1)
    #        lref = len(ref)
    #        lst = [base[:i0], strjump.Reference(1), base[i0 + lref:i1],
    #               strjump.Identifier(1, base[i1]), base[i1 + 1:]]
    #        base = base[:i0] + ref + base[i0 + lref:]
    #        #print("String to process:", '"' + strjump.tools.repr_string(lst) + '"')
    #        rst = strjump.process(lst)
    #        self.assertEqual(base, rst)
    #
    #def test_compiler4(self):
    #    for _ in range(1000):
    #        n = 150
    #        base = string.ascii_lowercase + string.digits
    #        base = ''.join(base[random.randint(0, 35)] for i in range(n))
    #        i1 = random.randint(5, n / 2) - 1
    #        if i1 == 10 ** (len(str(i1)) - 1):
    #            i1 -= 1
    #        i0 = i1 + random.randint(5, n / 2) - 1
    #        ref = str(i1)
    #        lref = len(ref)
    #        lst = [base[:i1], strjump.Identifier(1, base[i1]), base[i1 + 1:i0],
    #               strjump.Reference(1), base[i0 + lref:]]
    #        base = base[:i0] + ref + base[i0 + lref:]
    #        #print("String to process:", '"' + strjump.tools.repr_string(lst) + '"')
    #        rst = strjump.process(lst)
    #        self.assertEqual(base, rst)

    def test_compiler5(self):

        lst = ["3:",
        strjump.Reference('3-1277'),
        ",|",
        strjump.Identifier('3-1277', '-'),
        "a:",
        strjump.Reference('3-1280'),
        ",-b:",
        strjump.Reference('3-1279'),
        ",-n:",
        strjump.Reference('3-1278'),
        ",-t:",
        strjump.Reference('3-1281'),
        ",;;;;|",
        strjump.Identifier('3-1278', '-'),
        "m:",
        strjump.Reference('3-1284'),
        ",;;;;|",
        strjump.Identifier('3-1279',';'),
        ";;;|",
        strjump.Identifier('3-1280',';'),
        ";;",
        strjump.Reference('3!1'),
        ";|",
        strjump.Identifier('3-1281', '-'),
        "f:",
        strjump.Reference('3-1283'),
        ",-g:",
        strjump.Reference('3-1282'),
        ",;;;;|",
        strjump.Identifier('3-1282', ';'),
        ";;",
        strjump.Reference('3!4'),
        ";|",
        strjump.Identifier('3-1283', ';'),
        ";;",
        strjump.Reference('3!5'),
        ";|",
        strjump.Identifier('3-1284', '-'),
        "j:",
        strjump.Reference('3-1285'),
        ",;;",
        strjump.Reference('3-1286'),
        ";;|",
        strjump.Identifier('3-1285', ';'),
        ";;",
        strjump.Reference('3!3'),
        ";|",
        strjump.Identifier('3-1286', ';'),
        ";;",
        strjump.Reference('3!2'),
        ";|",
        strjump.Identifier('3!0', '-'),
        "b,-c,d,|",
        strjump.Identifier('3!1', '-'),
        "a,-c,d,|",
        strjump.Identifier('3!2', '-'),
        "n,-m,i,|",
        strjump.Identifier('3!3', '-'),
        "n,-m,-j,|",
        strjump.Identifier('3!4', '-'),
        "t,-g,i,|",
        strjump.Identifier('3!5', '-'),
        "t,-f,i,|"]

        #print("String to process:", '"' + strjump.tools.repr_string(lst) + '"')
        result = strjump.process(lst)
        #print("Result:", result)
        ref = "3:5,|-a:50,-b:45,-n:34,-t:58,;;;;|-m:91,;;;;|;;;;|;;;131;|-f:83,-g:75,;;;;|;;;159;|;;;168;|-j:106,;;114;;|;;;149;|;;;140;|-b,-c,d,|-a,-c,d,|-n,-m,i,|-n,-m,-j,|-t,-g,i,|-t,-f,i,|"
        self.assertEqual(result, ref)
