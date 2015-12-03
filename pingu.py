#!/usr/bin/env python
'''
    Pingu is a ping-like utility for checking server availibility
    Copyright (C) 2015 Morgan Brown, Casey Freeburg, Levi Muniz, and Jason Walker. All rights reserved.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import argparse, socket, time

parser = argparse.ArgumentParser(description="Ping-like utility for checking server availibility.",epilog="Copyright (C) 2015 Morgan Brown, Casey Freeburg, Levi Muniz, and Jason Walker. All rights reserved.")
parser.add_argument("HOST", help="The host to connect to")
parser.add_argument("PORT", type=int, help="The port to connect to")
parser.add_argument("-r", "--repeat", action="store_true", help="Repeat this in a loop")
args = parser.parse_args()

def connect(host, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(5)
		s.connect((host, port))
		s.close()
		print("\033[32mCan connect to " + args.HOST + " on port " + str(args.PORT)+ "\033[0m")
	except:
		print("\033[31mCan \033[1mNOT\033[0m\033[31m connect to " + args.HOST + " on port " + str(args.PORT) + "\033[0m")

if args.repeat:
	while True:
		try:
			time.sleep(1)
			connect(args.HOST, args.PORT)
		except KeyboardInterrupt:
			try:
				s.close()
			except:
				pass
			exit()
else:
	try:
		connect(args.HOST, args.PORT)
	except KeyboardInterrupt:
		try:
			s.close()
		except:
			pass
		exit()
