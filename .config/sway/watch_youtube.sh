#!/bin/sh
mpv $(xclip -o | sed -n 1p)

