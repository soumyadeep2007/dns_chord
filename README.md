# DNS on Chord
An implementation of DNS on [Chord](https://pdos.csail.mit.edu/papers/ton:chord/paper-ton.pdf). Chord has been implemented on [DistAlgo](http://distalgo.cs.stonybrook.edu/home), a research programming language for writing distributed algorithms.

# Instructions and notes

1. To start, please download and install DistAlgo from: 
https://sourceforge.net/projects/distalgo/?source=typ_redirect
The installation instructions reside in DistAlgo's README.

2. To run the system: python -m da --message-buffer-size 1000000 -F output --logfile --logfilename test.log src/chord/main.da
This command will run the system and output to the file test.log inside the root directory of the project.

3. Sample logs from our test runs have been included in the logs folder.
Statistics Logs: Logs used to perform analysis and plot different graphs for different results.
QueryResolution Logs: Logs showing how dns queries were resolved in chord system.
