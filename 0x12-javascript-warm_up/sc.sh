#!/bin/bash
for file in *.js;
do
	sed -i '1s|.*|#!/usr/bin/node|' "$file"
done
