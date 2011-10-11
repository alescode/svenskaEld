# -*- coding: utf-8 -*-
#! /usr/bin/env python

import cPickle as pickle

class Eld:
    def __init__(self):
        self.dic = {}
        self.box = []
        # doesn't work self.get = lambda s: s == "dic" and self.dic or self.box
        self.get = lambda s: self.dic if s == "dic" else self.box
        #self._save("dic")
        #self._save("box")

    # private functions for handling objects
    def _save(self, objectName):
        file = open(objectName + ".p", "wb")
        pickle.dump(self.get(objectName), file)
        file.close()

    def _load(self, objectName):
        file = open(objectName + ".p", "rb")
        object = pickle.load(file)
        file.close()
        return object

    def add2Dic(self, key, value):
        self.dic = self._load("dic")
        self.dic[key] = value
        self._save("dic")
        print key, '-->', value

    def add2Box(self, thing):
        self.box = self._load("box")
        self.box.append(thing)
        self._save("box")
        print thing

    def loadFile2Dic(self, fileName):
        file = open(fileName, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            print 0, line
              
    def showBox(self):
        self._box = self._load("box")
        for thing in self._box:
            print thing

    def showDic(self):
        # this line gives trouble if the field is named 'dict' (conflict with the type name)
        self.dic = self._load("dic")
        for key in self.dic:
            print "%s\t%s\t%s" %(key, '-->', self.dic[key])

    def update(self):
        self.dic = self._load("dic")
        self.box = self._load("box")

if __name__ == '__main__':
    pass
