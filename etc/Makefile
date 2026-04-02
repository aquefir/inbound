#!/usr/bin/env make

include etc/prologue.mk

# name of project used in output binary naming
# shared library: libsample.so, sample.dll
# static library: libsample.a, sample.lib
# executable: sample, sample.exe, sample.com
PROJECT := sample

# put a '1' for the desired target types to compile
# leave blank to not compile them
EXEFILE :=
SOFILE  := 1
AFILE   := 1

# space-separated path list for #includes
# <system> includes
INCLUDES :=
# "local" includes
INCLUDEL := src

SFILES := \
	src/hi.s \
	src/hey.asm # both work
CFILES := \
	src/hello.c
CPPFILES := \
	src/howdy.cpp \
	src/yo.cxx \
	src/greetings.cc \
	src/salutations.c++ # all work
# Objective-C
MFILES :=
# Objective-C++
MMFILES :=
# "public" headers, i.e. in a project's include/
# also to be distributed as public API on Unices
PUBHFILES :=
# "private" headers, i.e. in a project's src/
# not to be distributed or exposed in any public API
PRVHFILES :=

# Specify sources for specific platforms like so
# all platform specifiers work for all file types, except with MFILES
# and MMFILES which only take DARWIN86 and DARWINM1
CFILES.LINUX32 :=
CFILES.LINUX64 :=
CFILES.FREEBSD :=
CFILES.OPENBSD :=
CFILES.DARWIN86 :=
CFILES.DARWINM1 :=
CFILES.ILLUMOS :=
CFILES.IBMPC :=
CFILES.PCDOS :=
CFILES.WIN311 :=
CFILES.WINNT32 :=
CFILES.WIN95 :=
CFILES.WINNT64 :=
CFILES.AGBHB :=
CFILES.AGBSP :=

# make the linker C++ aware
LD := $(CXX)

# this defines all our usual targets
include etc/epilogue.mk
