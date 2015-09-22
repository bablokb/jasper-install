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

** This is work in progress (beta-stage), but should already work **


Configure Installation
----------------------

After download of the package (or after cloning the repository) you will
find the installation script `jasper-install` together with some
support files in the root-directory of the project. Configuration is
done using the file `jasper-install.cfg`.

The file contains constants used by the installation program. Usually you
don't have to change any contstants except the value of `DEFAULT_USER` and
those named `INSTALL_xxx`. These constants select which modules the install
script actually installs. You can set the value of these constants to `0`
(don't install) or `1` (install).

Some of these modules do just basic tasks, so you should not change the
value - these constants are labelled *required*. Besides these modules, you
are free to select the STT and TTS engines you wan't (but observe the
dependencies). To understand the background, you should definitely read
the documentation on the project site of Jasper.


Install Jasper
--------------

The installation script `jasper-install` assumes that you start of with
a *clean* installation of Raspbian-Wheezy (after initial configuration
with `raspi-config`). A simple

    sudo ./jasper-install all

should do the job. The script will create a (large) logfile named
`jasper-install.log`, please check that file for errors.

Besides `all` you can pass the names of one or more individual modules to 
`jasper-install`. This is more of a development feature to verify the
correct operation of the given install-task.

If you connect with ssh and don't want to keep the connection open all
the time, you can also start the installation with

    nohup sudo ./jasper-install all > /dev/null &

To monitor the progress in this case, you can use the command

    tail -f jasper-install.log

Note that `jasper-install` takes a lot of time to finish (this also
depends on the configured modules). Running Raspbian off of an HDD/SDD
really speeds things up. Search the web for instructions on how to move
your root-partition to an USB-attached HDD/SDD drive. Also, installation
time is much faster on a model 2, since the compilations of the source
modules use all four available processors.

The install script installs a number of packages using the normal package
management system of Debian (*apt*). Others are downloaded and compiled
from source. All files are installed below `$PREFIX`, which defaults to
`/usr/local`, i.e. you can copy this directory to other computers to
save some time during installation (see section below on details).


Changes to the original install instructions
--------------------------------------------

There are some changes compared to the original install instructions from
Jasper's project site:

  - this script installs all programs globally
  - you can run the jasper-program with the simple command `jasper`, or
    you can install jasper as a system-service`
  - OpenFST is downloaded from the OpenFST-site in a slightly newer version
  - added configure-option to OpenFST to speed-up compilation
  - required package `python-pocketsphinx` was missing from the instruction
  - New download-address for phonetisaurus
  - only compile necessary binary for phonetisaurus
  - New download-address for phonetisaurus FST model


Cloning the installation
------------------------

** this does not work yet! **

Since download and compile of all the prerequisite packages takes
so long, you can take a shortcut to clone Jasper to other computers.

The following steps are necessary:

  1. Copy everything below $PREFIX (i.e. `/usr/local`) to the new
     computer. You can use rsync for the task if you enabled
     root-login on the target computer (*clone*):

         sudo rsync -avz /usr/local/ root@clone:/usr/local

  2. Copy all `jasper-install`-files to the target computer.
  3. Edit `jasper-install.cfg.clone` to reflect your `jasper-install.cfg`
     (read the comments in `jasper-install.cfg.clone`).
  4. Run

         sudo ./jasper-install -C jasper-install.cfg.clone all


Running jasper
--------------

To run jasper as a foreground process from your normal user account
just run the command `jasper`. If you like to see how jasper processes
your commands, run

    jasper --debug

Note that the install-script will create a default jasper configuration 
profile for the default user (as defined in `jasper-install.cfg`).
If you are not happy with the profile, you can delete it and run

    $PREFIX/lib/jasper/client/populate.py

This will run you through the default configuration provided by jaser
itself. You can find details about the initial configuration on the Jasper
[project website](http://jasperproject.github.io/ "project website").

As an alternative, you can install jasper as a system-service. 
If not already done during installation, change
`INSTALL_service` in `jasper-install.cfg` to `1` and run

    sudo ./jasper-install service
    sudo update-rc.d jasper start

The last command is only necessary if you want to start the service at once.
Otherwise, it is automatically started at boot-time.

The configuration file for the service is in `$PREFIX/lib/jasper/profile.yml`.
