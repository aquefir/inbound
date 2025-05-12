#!/usr/bin/env make

include etc/prologue.mk

# name of project used in output binary naming
PROJECT := sample

# put a '1' for the desired target types to compile
EXEFILE :=
SOFILE  := 1
AFILE   := 1

# space-separated path list for #includes
# <system> includes
INCLUDES :=
# "local" includes
INCLUDEL := src

CFILES := \
	src/hello.c
CPPFILES :=
PUBHFILES :=
PRVHFILES :=

# make the linker C++ aware
LD := $(CXX)

# this defines all our usual targets
include etc/epilogue.mk
