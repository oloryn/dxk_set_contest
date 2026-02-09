# dxk_set_contest

## Purpose

This scratches an itch I've had ever since switching to using the DXLab Suite for my main ham radio logger.  QSOs in contest logs I've imported since switching are marked with the contest id for that contest, as the id is in the N1MM+ ADIF file, or I've specified it as part of the import.  Contest QSOs from before the switch aren't, as contest QSOs weren't so marked in the loggers I used before, and those old logs were imported en masse when I made the switch.

Also, I've been known to operate more that one contest at a time (N1MM+ makes this fairly easy), so I can't just have DXKeeper mark all QSOs within a particular time frame as belonging to a particular contest - QSOs for different contests might very well be interleaved.  What I wanted was a way to read the call and time stamp for QSOs from an archived contest ADIF file (typically from N1MM+) and set just those QSOs with the appropriate id.

This script reads an ADIF file (passed as the second command line argument) and creates a DXKeeper script which sets each QSO in the ADIF file to a specific contest id (passed as the first command line argument).  The script is written to the 'setcontestname.txt' file in the DXKeeper Scripts directory.  You can then run the setcontestname.txt script from within DXKeeper and it will set the QSOs appropriately.  Each time dxk_set_contest is run it appends to setcontestname.txt.  This allows you to run dxk_set_contest multiple times, once for each of multiple contests, and only run the DXKeeper script once.  Once setcontestname.txt is run once into DXKeeper, it should be removed or renamed, so those QSOs won't be re-modified.

## Installation

As DXKeeper runs only on Windows, so does dxk_set_contest (it queries the registry to determine the path to the DXKeeper Scripts directory).

dxk_set_contest runs Python, so you must have a recent version of Python installed.  This can be obtained at [The Python.org download page](https://www.python.org/downloads/.)  When installing Python, check the "Add Python 3.X to PATH" checkbox, or otherwise make sure the Python scripts directory is on the PATH.

Once Python is installed, run

    py -m pip install dxk_set_contest

from the command line to install dxk_set_contest

## Operation
