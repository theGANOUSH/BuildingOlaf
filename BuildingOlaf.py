#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2015  <theGANOUSH@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

def main():
	vol = raw_input("Input Total Volume\n")
	x = raw_input("Input Ratio of small\n")
	y = raw_input("Input Ratio of medium\n")
	z = raw_input("Input Ratio of large\n")
	
	pi = 3.0 / (4.0 * 3.141592653590)
	
	sumOfRatios = pow(int(x), 3) + pow(int(y), 3) + pow(int(z), 3)
	
	root = (int(vol) * pi) / sumOfRatios
	
	print("%.2f" % pow(root, (1.0/3.0)))
	
	return 0

if __name__ == '__main__':
	main()

