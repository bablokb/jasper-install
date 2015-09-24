TODOs for jasper-install
========================

- add processArguments
  - options -C cfgfile, -f force, -h help etc.
  - update readme regarding cloning

- verify system-service jasper
  * start, status, stop
  * amount of text written to syslog?

- add install-scripts for other engines
  * German acoustic modules
    - sphinx
    - julius
      http://www.repository.voxforge1.org/downloads/de/Trunk/Lexicon/Lexicon.tgz
     http://www.repository.voxforge1.org/downloads/de/Trunk/AcousticModels/voxforge_de_simon-2010-04-21.tgz

Later
-----

- add option "-f" to force install of a module

- check if packages from base are runtime or pure buildtime
  (python-pyaudio seems the only runtime package)

- add module devtools_rm

- move all downloads to separate module

- install newer version of gcc and use openfst 1.5.0??
