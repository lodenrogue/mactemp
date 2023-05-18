#! /usr/bin/env python3

import sys

names = []
values = []

for line in sys.stdin:
	if len(names) == 0:
		names = line.rstrip().split(', ')
	else:
		values = line.rstrip().split(', ')

temp_count = 0
temp_sum = 0

for index, name in enumerate(names):
	if name.startswith("PMU tdie"):
		value = values[index].replace(',', '')
		temp_sum += float(value)
		temp_count += 1

temp_c = temp_sum / temp_count
temp_f = temp_c * 9/5 + 32

print("{:.0f}".format(temp_f), "F")
