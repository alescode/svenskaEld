# -*- coding: utf-8 -*-
#! /usr/bin/env python

import cPickle as pickle

dict = {}
box = []

def _save():
    file = open("dict.p", "wb")
    pickle.dump(dict, file)
    file.close()

def _load():
    global dict
    file = open("dict.p", "rb")
    dict = pickle.load(file)
    file.close()

def add(key, value):
    dict[key] = value
    _save()
    print key, '-->', value

def show():
    _load()
    for key in dict:
        print "%s\t%s\t%s" %(key, '-->', dict[key])

if __name__ == '__main__':
    pass
