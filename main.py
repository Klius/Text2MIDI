#!/usr/bin/env/python
__author__ = 'Klius'
#imports go here
from midiutil import MIDIFile
from random import random
def createMIDI(input):
	degrees  = [60, 62, 64, 65, 67, 69, 71, 72] # MIDI note number
	track    = 0
	channel  = 0
	time     = 0   # In beats
	duration = 1   # In beats
	tempo    = 60  # In BPM
	volume   = 100 # 0-127, as per the MIDI standard

	MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
						 # automatically created)
	MyMIDI.addTempo(track,time, tempo)

	for pitch in input:
		MyMIDI.addNote(track, channel, pitch, time, duration, volume)
		time = time + 1

	with open("major-scale.mid", "wb") as output_file:
		MyMIDI.writeFile(output_file)

def createMIDI2(input):
	# MIDI note number
	track    = 0
	channel  = 0
	time     = 0   # In beats
	lastTime = 0
	duration = 1   # In beats
	tempo    = 150  # In BPM
	volume   = 100 # 0-127, as per the MIDI standard

	MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
						 # automatically created)
	MyMIDI.addTempo(track,time, tempo)

	for group in input:
		if(ord(group[0])<255):
			pitch = ord(group[0])
		else:
			pitch = 127
		if(ord(group[1])<127):
			volume = ord(group[1])
		else:
			volume = 127
		
		print(group)
		MyMIDI.addNote(track, channel, pitch, time, duration, volume)
		if ord(group[0])%2 == 0:
			time += 1
			lastTime = 1
		elif ord(group[0])%3==0:
			time +=0.5
			lastTime = 0.5
		elif ord(group[0])%5==0:
			time += 0.8
			lastTime = 0.8
		else:
			time -= lastTime
		
	
	with open("major-scale.mid", "wb") as output_file:
		MyMIDI.writeFile(output_file)

def readFile(path):
	with open(path) as file:
		content = file.readlines()
	
	content = [x.strip('\n') for x in content]
	
	return content
	
	
def contentToNotes(content):
	result = []
	letterCount = 0
	letterGroup = []
	for line in content:
		for letter in line:
			letterGroup.append(letter)
			letterCount +=1
			if letterCount>1:
				letterCount = 0
				result.append(letterGroup)
				letterGroup = []
				
	return result
			
		
	

file="test.txt"
content=readFile(file)
createMIDI2(contentToNotes(content))

#input = ["h","o","l","a"," ","a", "d", "r", "i"]
#inputToLetters = []
#for letter in input:
#	inputToLetters.append(ord(letter))
	
#createMIDI(inputToLetters)