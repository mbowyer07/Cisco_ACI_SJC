#!usr/bin/env python
import sys
from os.path import exists

prompt1 = ('source: ')
prompt2 = ('destination: ')
prompt3 = ('Yes or No: ')
prompt4 = ('No, really; just \'Yes\' or \'No\' ')

print """

=========================================
  This is the Replicator Script
  Stargate fans know what that can mean
  Use with Extream Caution
=========================================
"""
print '\nFirst, I\'ll need to know the source file...'
print '(if it\'s not in the local working directory, you\'ll \
need to provide the full path name)\n'

in_file = raw_input(prompt1)

filecheck1 = (exists(in_file))
if filecheck1 != True:
	print '\nUmmm... the source file you entered doesn\'t exist'
	print 'Please check the spelling and/or path and try again\n'
	in_file = raw_input(prompt1)
else:
	source_file = open(in_file)
	indata = source_file.read()
	print '\nThe input file is %d bytes long (just checking)' % len(indata)

print '\nOk, now I need the destination file name...\n'

out_file = raw_input(prompt2)

print "\nOk, copying from %s to %s...\n" % (in_file, out_file)

# we could to these two on one line, but how? reflect on that...
source_file = open(in_file)
indata = source_file.read()
filecheck2 = (exists(out_file))

print "But before we do anything we'll regret, does the destination \
file already exist?"

if filecheck2 == True:
	print '''
	Warning: The destination file already exists...
	Warning: If you continue, the file will be over-written!
	Warning: This action, once undertaken, CANNOT be un-done!

	Hit RETURN to continue or CTRL-C to abort
	'''
else:
	print '\n\tNope, no one here by that name...\n'
	print '\nIf you\'re ready, hit RETURN to continue, CTRL-C to abort.'
raw_input()

outdata = open(out_file, 'w+')
outdata.write(indata)

if filecheck2 == True:
	print '\nAlright, but don\'t say I didn\'t warn ya...'
	print '\n  (because I did...)'
	print '\nOk, all done...\n\n'
else:
	print 'Alright... request completed'

print '\nWould you like to see the results?\n'
print '(use with caution if the file is large)'

answer = raw_input(prompt3)
print '\nYou answered %r' % answer
print ''

readit = str(answer.lower())

if readit == "yes":
	outdata.seek(0)
	print '++++++ Start of file ++++++'
	for line in outdata:
		x = line
		print (x)
	print '++++++ End of file ++++++'
	print 'All done... Thank you for playing... Don Pardo, tell them \
what they\'ve won!\n'
	outdata.close()
	index=10
	
elif readit == "no":
	print '\nWoW! You\'re a trusting sole!! 8^) '
	print '(personally, I would have checked...)\n'
	index=20
	
else:
	index=0

while index <= 3:
	
	index += 1

	if index == 1:
		print '''
	Look, I know I'm just a stupid computer program...

	But even I know the difference between what I asked for...

	And what you typed...

	Please enter 'Yes' or 'No'

	'''
		answer2 = raw_input(prompt4)
		print '\nYou answered %r this time\n' % answer2
		readit2 = str(answer2.lower())

		if readit2 == "yes":
			print '====== Start of File ======'
			outdata.seek(0)
			for line in outdata:
				x = line
				print (x)
			print '====== End of File ======'
			print '\n All done...\n'
			outdata.close()
			index=10
			
		elif readit2 == "no":
			print '\nReally?!? Wow!! You\'re a trusting sole! 8^)'
			print '(personally, I would have checked... just sayin\'...\n)'
			index=20
			
	if index == 2:
		print '''
	Strike Two...

	Come on, fella... help me out here...

	Just enter 'Yes' or 'No'

	'''
		answer3 = raw_input(prompt4)
		print '\nYou answered %r this time' % answer3
		readit3 = str(answer3.lower())

		if readit3 == "yes":
			print '\n====== Start of File ======'
			outdata.seek(0)
			for line in outdata:
				x = line
				print (x)
			print '\n====== End of File ======'
			print '\n All done...'
			print '     (guess "third time\'s the charm for you, eh?...)\n'
			outdata.close()
			index=10
			
		elif readit3 == "no":
			print '\nReally?!? Wow!! You\'re a trusting sole! 8^)'
			print '(personally, I would have checked... just sayin\'...)'
			print '     (guess "third time\'s the charm for you, eh?...)\n'
			index=20
			
	if index == 3:
		print '''

	Strike THREE!! You're Outta Here!!

	Come back when you can follow directions, Slugger...

		'''
		index = 30
		outdata.close()			
