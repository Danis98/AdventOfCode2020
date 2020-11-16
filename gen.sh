#!/bin/bash

for i in $(seq -f "%02g" 1 25)
do
	dname="day${i}"
	mkdir "${dname}"
	touch "${dname}/part1.py"
	touch "${dname}/part2.py"
	touch "${dname}/${dname}.input"
done
