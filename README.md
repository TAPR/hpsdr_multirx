hpsdr_multirx -- 11 August 2017 -- John Ackermann N8UR -- jra@febo.com

The hpsdr_multirx.grc Gnuradio flowgraph allow SDR receivers that support
the HPSDR "old protocol" to record semi-wideband (384ksample/second)
chunks of RF spectrum.  Depending on the hardware, up to seven independent
receivers may be configured.

There is also a single-channel version with added capability to measure
the amplitude of the strongest signal in the sampled spectrum.  It's still
a work in progrerss.

If there is time before the eclipse, I will upload variants preconfigured
for six, three, and two channels.

These programs rely on:

1.  Gnuradio installed on a Linux computer.  Development was done 
on a Linux Mint 18.2 system with the standard gnuradio ".deb" 
packages installed via apt-get, and the instructions below assume a
debian-based system.  Other means of installing gnuradio may put
files in different locations, so might require configuration changes.
It should be possible to install on a Windows system, but I haven't 
tested that.

NOTE:  Building the digital_rf tools from MIT-Haystack requires version
3.0 or later of the "cmake" tool.  Current versions of Ubuntu/Linux Mint
include versions that work.  However, earlier versions such as Ubuntu 14.04
or Mint 17.x have an earlier version.  There are weird conflicts if you
try to install the new cmake on an older system.  The best bet is to use
a system based on Ubuntu 16.04/Linux Mint 18 or later.

2.  The standard development environment plus tools needed for gnuradio.
    Install them with:
	* sudo apt-get install build-essential
	* sudo apt-get build-dep gnuradio

3.  N5EG, Tom McDermott's, gr-hpsdr blocks.   Here is how to install them:

	* Create a directory in your home directory for your gnuradio
	  files.  I call mine "gr-projects" and will use that in these 
	  instructions, but use whatever name you'd like.

	* Issue these commands:
		cd ~/gr-projects
		git clone https://github.com/Tom-McDermott/gr-hpsdr
		cd gr-hpsdr
		mkdir build 
		cd build 
		cmake ..
		make 
		sudo make install 
		sudo ldconfig 

	* cd ~/gr-projects
	* git clone https://github.com/Tom-McDermott/gr-hpsdr.git
	* cd gr-hpsdr
	* mkdir build 
	* cd build 
	* cmake ..
	* make 
	* sudo make install 
	* sudo ldconfig 

4.  The MIT-Haystack "Digital RF" blocks.  Here is how to install them:

	* Issue this command to install dependencies:

		sudo apt-get install libhdf5-dev python-dev
		python-numpy gnuradio-dev libboost-dev swig python-h5py
		python-tz python-dateutil python-setuptools
		sudo apt-get install Build: libhdf5-dev python-dev
		python-numpy gnuradio-dev libboost-dev swig python-h5py
		libhdf5 pytz python-dateutil python-setuptools

	  (Some of these will probably be already installed)

	* Issue these commands:
		* cd ~/gr-projects
		* git clone https://github.com/MITHaystack/digital_rf.git
		* cd digital_rf
		* mkdir build
		* cd build
		*cmake ..
		* make
		* sudo make install
		* sudo ldconfig

Once these blocks have been installed, the hpsdr_multirx program should
be ready to run.  You can run the Gnuradio Companion (grc) program from
either the start menu, or a command line, and then navigate to and open
hpsdr_multirx.grc.

You'll see the flowgraph diagrammed on the grc workspace.  You'll want to
configure a couple of variables for your installation, and also decide
on how the program operates by enabling or disabling certain of the blocks.

To enable/disable, hover the mouse on a block and right-click.  You'll see
a menu option to enable or disable.  Click that if required.  Disabled
blocks are grayed-out in the workspace.

Open the "hpsdr_multirx_config.png" file that should accompany this
README.  It shows the flowgraph with some cribnotes on the changes you
might want to make.  Here are more details about those selections:

	* Note that some versions of Linux assign different interface
	  names to the ethernet connection.  The HermesNB block will show
	  what interfaces it thinks are available, or you can issue the
	  command "ifconfig" at Linux command prompt to see what's been
	  assigned -- it's likely to be either "eth0" or on the newest
	  OS versions something like "enXX".

	* By default, the system is set up for four receivers.  You
	  can increase the number by copy/pasting to create additional
	  rx frequency and sink blocks, as well as adjusting the number
	  of inputs for the GUI sink.

	* By default, the center frequencies of the four receivers are:
		* rx0 3.675 MHz (covers ~3.487-3.862 MHz)
		* rx1 7.175 MHz (covers ~6.987-7.362 MHz)
		* rx2 10.100 MHz (covers ~9.912-10.287 MHz)
		* rx3 14.175 MHz (covers ~13.987-14.362 MHz)

	* The working_dir variable should be set to the directory under
	  which data files will be stored.

	*  IMPORTANT: if you are using the standard Gnuradio file sink
           blocks, the working directory must exist before the flowgraph
	  is run.

	* The metadata variable should be edited to include your call
	  (or name), the receiver type, and a description of the antenna.
	  The variable is in the form of a Python "dict".  The syntax
	  is as follows: {key1:val1,key2:val2,key3:val3} with any key
	  or value that is a string enclosed in single quotes.  I suggest
	  the following format for the solar eclipse experiment:
	  {'call':'your_call','grid:'your_grid','rx':'your_rx','ant':'your_ant'}
	  Use six-character grid value if possible, and if you don't have a
	  ham call, use your name instead.

	* The rx_samp_rate variable should be set to match the "RX Sample
	  Rate" setting in the HermesNB block.

	* The group of four "File Sink" blocks can be enabled (either
	  individually or as a group) to record band data in the raw
	  binary form that gnuradio uses by default.  For the eclipse
	  experiment, disable these blocks.

	* The group of four "Digital RF Channel" blocks write data to
	  files in the HDF5 format.  Enable the blocks matching the
	  number of receivers you are using.  USE THIS FORMAT FOR
	  THE ECLIPSE TEST!

	* The "QT GUI Frequency Sink" block puts a nifty spectrum display
	  on the screen showing signals on each receiver.  This is really
	  pretty to look at but uses quite a bit of CPU.  Use this block
	  for testing, but you might want to disable it when recording
	  data to ease the processor load.

	* You must have one active sink block (either GUI or file/channel
	  sink) for each receiver output from HermesNB.  If you're using
	  less than four channels, reduce the "Num Recvs" value in the
	  HermesNB block to match, disable the file blocks related to the
	  disabled receivers, and reduce the number of inputs in the
	  Frequency sink.  If you increase the receiver number later,
	  you'll need to rewire those connections.

To stop the program (and stop recording data, close the GUI window
or click the stop icon in the Gnuradio Companion window.

Using an i7-6700T @ 2.8 GHz with a solid state disk, I've had no trouble
recording four 384ksample/second channels. If you see underruns 
("U" characters) or other errors in the gnuradio console, first try
disabling the frequency sink block.  If you still have errors, you mayi
need to reduce the number of receivers.

