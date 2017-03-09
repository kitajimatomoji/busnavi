# coding: utf-8

import csv
import time
from datetime import datetime

is_satureday = False
is_holyday = False
alarm_message_list = []

# 何分前にアラーム鳴らすか（5分）
delta = 5



def arrival_check(target_dir, bus_number, delta, h, m):

	# バスの時刻表csvを読み込む
	timetable = []

	with open(target_dir + '/' + str(bus_number) + '.csv', 'r') as f:
	    reader = csv.reader(f)

	    for row in reader:
	    	timetable.append(row)

	# 時間(h)判定
	if h == 0 or h > len(timetable):
		return ''

	# 時間(m)判定
	arrival_list = timetable[h-1]
	print arrival_list
	m_padded = '{0:02d}'.format(m)
	print m_padded
	for arrival in arrival_list:
		if arrival == m_padded:
			return str(delta) + "分後にバスが来ます。" + str(bus_number) + '系統です。'

	return ''



now = datetime.now()
# n分先の時刻を算出する
currenttime_H = int(time.strftime("%H"))
currenttime_M = int(time.strftime("%M")) + delta

if currenttime_M > 59:
	currenttime_H += 1
	currenttime_M -= 60
if currenttime_H > 23:
	currenttime_H -= 24

print currenttime_H, currenttime_M


# 土曜日判定
if now.weekday() == 5:
	is_satureday = True

# 日・祝日判定 [todo:祝日判定]
if now.weekday() == 6:
	is_holyday = True


# 平日・土・日・祝日のダイヤ切り替え（フォルダ切り替え）
target_dir = "weekday"
if is_satureday:
	target_dir = "saturday"
if is_holyday:
	target_dir = "holiday"


message = arrival_check(target_dir, 31, delta, currenttime_H, currenttime_M)
if message != '':
	alarm_message_list.append(message)

message = arrival_check(target_dir, 25, delta, currenttime_H, currenttime_M)
if message != '':
	alarm_message_list.append(message)

for alarm_message in alarm_message_list:
	print alarm_message







