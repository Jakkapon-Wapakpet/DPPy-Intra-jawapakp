#!/usr/bin/env python3

promt = "what you gotta say? : "

while True:
    answer = input(promt)

    if answer == "STOP":
        break

    promt = "I got that! Anything else? : "