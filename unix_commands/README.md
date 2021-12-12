# Unix-utilities imitation

This folder contains 7 scripts that partially imitate the work of common Unix utilities (however their functionality is very restricted). 
The scripts have the same names as standard Unix utilities. You can get information about each programm by `./script_name.py -h`.

### Requirements

- The scripts use standard python library only, so you don't need to install any other modules.
- The correct work was tested on Ubuntu 20.04. (and the scripts cannot work correctly in Windows OS because of many reasons).
- The scripts were tested with python 3.8.10 and 3.9.5

### Installation

- Clone repository into your local machine:<br>
`git clone git@github.com:Ann-Krlv/BI_2021_Python.git`

- Or copy this folder manually

- You need the unix_commands folder<br>
`cd ./unix_commands`

**Installation and usage option №1**

This variant is simplier and don't add files into PATH

- Please, make sure that all scripts are executable<br>
- if not, print `chmod +x cat.py grep.py ls.py mkdir.py rm.py sort.py tail.py wc.py`.<br> 
- Now you can run scripts by `./script_name.py -args file`<br>
 i.g. `./ls.py` or `./wc.py -clw text.txt` or `./mkdir.py -p dir1/dir2 dir3`

**Installation and usage option №2**

This variant copies all scripts into first folder in your PATH.

- Make sure that install.py is executable (if not, print `chmod +x install.py`)
- (other files do not have to be executable)
- Run install.py: `./install.py`
- Done! Now you can run scripts without path (i. g `ls.py` or `mkdir.py -p dir1/dir2 dir3`)
