#!/usr/bin/env python

def options(opt):
	opt.load('compiler_cxx')

def configure(conf):
	conf.load('compiler_cxx qt5')

def build(bld):
	bld.program(source='main.cpp', use='QT5GUI')
