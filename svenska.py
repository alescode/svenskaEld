# -*- coding: utf-8 -*-
dict = { \
    "går forbi" : "go past (a place)", \
    "får motion" : "exercise",        \
}

def l(key, value):
    dict[key] = value
    print key, '-->', value

def p():
    for key in dictionary:
        print "%s\t%s\t%s" %(key, '-->', dictionary[key])

