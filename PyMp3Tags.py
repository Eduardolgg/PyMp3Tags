#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# PyMp3Tags.py
#
# Copyright (C) 2016  Eduardo L. García Glez <eduardo.l.g.g@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import sys
parameters = [
	{ "name" : "artist", "option": "-a", "value": None },
	{ "name": "album", "option": "-l", "value": None },
	{ "name": "year", "option": "-y", "value": None },
	{ "name": "gener", "option": "-g", "value": None }
]
path = "./"

mp3InfoExe = "mp3info"

def main(argv):
	if (len(argv) < 1):
		printUsage()
		return
	initParameters(argv)
	mp3Files =  getMp3Files(path)
	writeTags(mp3Files)

def writeTags(mp3Files):
	for songFile in mp3Files:
		runWithParams = mp3InfoExe + serializeParams() 
		runWithParams += ' -t "' + getSongTitle(songFile) + '"'
		runWithParams += ' -n ' + getSongNumber(songFile) + ' '
		runWithParams += path + "/" + songFile
		#print runWithParams
		os.system(runWithParams)

def getSongTitle(songFile):
	songTitle = songFile.replace("_", " ").replace("-", " ")
	songTitle = songTitle[len(getSongNumber(songFile)) + 1:len(songFile)-4]
	return songTitle.title()
	
def getSongNumber(songFile):
	songNumber = ""
	for char in songFile:
		if (char.isdigit()):
			songNumber += char
		else:
			break
	return songNumber

def serializeParams():
	serialParams = ''
	for param in parameters:
		if (param["value"] != None):
			serialParams += ' ' + param["option"] 
			serialParams += ' "' + param["value"] + '"'
	return serialParams

def initParameters(argv):
	global path
	path = argv[len(argv) - 1]
	for param in parameters:
		try:
			index = argv.index(param["option"])
			param["value"] = argv[index + 1]
		except Exception, e:
			# Parameter not found: Keep the default.
			pass


def getMp3Files(path):
	files = getFiles(path)
	return filterFiles(files)

def getFiles(path):
	for base, dirs, files in os.walk(path):
		return files

def filterFiles(files):
	mp3Files = [];
	for file in files:
		if (isMp3File(file)):
			mp3Files.append(file)
	return mp3Files

def isMp3File(file):
	return file.endswith(".mp3")

def printUsage():
	print "Add tags to mp3 by getting the track number and song name of the file name."
	print ""
	print "Usage: PyMp3Tags.py [options] songs_dir"
	print ""
	print "Options:"
	print "\t-a artist"
	print "\t-l album name"
	print "\t-y year"
	print "\t-g genre. View mp3info man for more info."
	print ""
	print "Considerations:"
	print "\t* The track number and song name is extracted from the file name."
	print "\t* File name format: 00_Song_Title.mp3"
	print ""
	print "\t\t > 00: Is a track number and can be one or more digits."
	print ""
	print "\t\t > Song_title: It is the name of the song and will delete"
	print "\t\t   the characters - and _ will be replaced by white space "
	print "\t\t   and the title converted to camel case."
	print ""
	print "\t* This script needs mp3info to work properly."

if __name__ == "__main__":
	main(sys.argv[1:])
