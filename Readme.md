Jasper Installation Script
==========================

Introduction
------------

This repository contains an installation script for all the libraries and
dependencies of [jasper](http://jasperproject.github.io/ "jasper").

While the jasper project provides an image for the model 1 of the
Raspberry Pi, there is no image for the model 2. Instead of mastering a
big image, I just provide a ready to run installation script.

The installation script will work on a model 1 or a model 2 Raspberry Pi
(Bananapi to be verified).

** This is work in progress (pre beta-stage), it might or might not work **


Configure Installation
----------------------

After download of the package (or after cloning the repository) you will
find the installation script `jasper-install` together with some
support files in the root-directory of the project. Configuration is
done using the file `jasper-install.cfg`.

The file contains constants used by the installation program. Usually you
don't have to change any contstants except those named `INSTALL_xxx`. These
constants select which modules the install script actually installs. You can
set the value of these constants to `0` (don't install) or `1` (install).

Some of these modules do just basic tasks, so you should not change the
value - these constants are labelled *required*. Besides these modules, you
are free to select the STT and TTS engines you wan't (but observe the
dependencies). To understand the background, you should definitely read
the documentation on the project site of Jasper.


Install Jasper
--------------

The installation script `jasper-install` assumes that you start of with
a clean installation of Raspbian-Wheezy. A simple

    sudo ./jasper-install all

should do the job. The script will create a (large) logfile 
`./jasper-install.log`, please check that file for errors.

Besides `all` you can pass the names of one or more individual modules to 
`jasper-install`. This is more of a development feature to verify the
correct operation of the given install-task.

Note that `jasper-install` takes a lot of time to finish (this also
depends on the configured modules). Running Raspbian off of an HDD/SDD
really speeds things up. Search the web for instructions on how to move
your root-partition to an USB-attached HDD/SDD drive. Also, installation
time is much faster on a model 2, since the compilation of the source
modules uses all four available processors.

The install script installs a number of packages using the normal package
management system of Debian (*apt*). Others are downloaded and compiled
from source. All files are installed below `$PREFIX`, which defaults to
`/usr/local`, i.e. you can copy this directory to other computers to
save some time during installation.


Changes to the original install instructions
--------------------------------------------

There are some changes compared to the original install instructions from
Jasper's project site:

  - this script installs all programs globally
  - the jasper-program runs as a system-service with system-user `jasper`
  - configuration is in `/etc/jasper.cfg`
  - OpenFST is downloaded from the OpenFST-site in a slightly newer version
  - Missing package python-pocketsphinx is necessary
  - configure OpenFST to only compile libs
  - New download-address for phonetisaurus
  - only compile necessary binary for phonetisaurus
  - New download-address for phonetisaurus FST model
