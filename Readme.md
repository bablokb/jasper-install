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

For a Pi model 1, you must set `INSTALL_phonetisaurus_src=1`. For a
model 2, you are free to install from the Jessie package repository
(`INSTALL_phonetisaurus=1`) or from source.

Some of the modules do just basic tasks, so you should not change the
value - these constants are labelled *required*. Besides these modules, you
are free to select the STT and TTS engines you wan't (but observe the
dependencies). To understand the background, you should definitely read
the documentation on the project site of Jasper.


Install Jasper
--------------

The installation script `jasper-install` assumes that you start of with
a *clean* installation of Raspbian-Wheezy (after initial configuration
with `raspi-config`). You need at least 4 GB free disk-space on the
root-partition, i.e. a 8GB (micro-) SDHC with expanded root-partition
should do fine.

A simple

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

or

    grep "info:" jaspler-install.log

Note that `jasper-install` takes a lot of time to finish (this also
depends on the configured modules). Running Raspbian off of an HDD/SDD
speeds things up by about 5%. Search the web for instructions on how to move
your root-partition to an USB-attached HDD/SDD drive. Also, installation
time is much faster on a model 2, since the compilation of the source
modules uses all four available processors.

The install script installs a number of packages using the normal package
management system of Debian (*apt*). Others are downloaded and compiled
from source. All files are installed below `$PREFIX`, which defaults to
`/usr/local`, i.e. you can copy this directory to another computer to
save some time during installation of a second machine(see the section
below labeled *Cloning the Installation* for details).


Some Timings
------------

As noted above, the whole `jasper-install` script takes a long time to
finish. A complete installation will take

  - 7-8h on a Raspberry Pi Model 1
  - 3-4h on a Raspberry Pi Model 2

Timings depend on the speed of your SDHC-cards as well as the speed
of your internet connection. OpenFST is the module taking longest,
compile and linking of it alone takes more than 5h on a model 1
(about 2h on a model 2).


Changes to the original install instructions
--------------------------------------------

There are some changes compared to the original install instructions from
Jasper's project site:

  - this script installs all programs globally
  - you can tailor the installation to your needs, e.g. if you don't plan
    to use phonetisaurus, you don't have to install all the programs
    needed by this STT-engine
  - you can run the jasper-program with the simple command `jasper`, or
    you can install jasper as a system service`
  - Jasper is not added to a user's crontab (use the system service if you want
    to start Jasper automatically at boot time)
  - OpenFST is downloaded from the OpenFST-site in a slightly newer version
  - added configure-option to OpenFST to speed-up compilation
  - required package `python-pocketsphinx` was missing from the instruction
  - New download-address for phonetisaurus
  - only compile necessary binary for phonetisaurus
  - New download-address for phonetisaurus FST model
  - Download acoustic model and lexicon for Julius
  - create default profile.yml with all configuration-options
    (non-active STT/TTS-engines are added as comments)


Cloning the installation
------------------------

**this does not work yet!**

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
just run the command `jasper` (your user account must be a member of 
the `audio` group and you should have configured this user as the
*DEFAULT_USER* in `jasper-install.cfg`). If you like to see how jasper
processes your commands, run

    jasper --debug

Note that the install-script will create a default jasper configuration 
profile for the default user (as defined in `jasper-install.cfg`).
If you are not happy with the profile, you can delete it and run

    $PREFIX/lib/jasper/client/populate.py

This will run you through the default configuration provided by jaser
itself. You can find details about the initial configuration on the
[Jasper project website](http://jasperproject.github.io/
"Jasper project website").

As an alternative, you can install jasper as a system-service. 
If not already done during installation, change
`INSTALL_service` in `jasper-install.cfg` to `1` and run

    sudo ./jasper-install service
    sudo update-rc.d jasper start

The last command is only necessary if you want to start the service at once.
Otherwise, it is automatically started at boot-time.

The configuration file for the service is in `$PREFIX/lib/jasper/profile.yml`.

Sometimes, the service has problems to start right after installation and
reboot. In this case, delete the directory `$PREFIX/lib/jasper/vocabularies`
and restart the service.


Renaming Jasper
---------------

If you have trouble pronouncing "Jasper", then you can change the
signal word from "Jasper" to "Thomas". You just have to define
`INSTALL_thomas=1` in `jasper-install.cfg`. Note that this changes
the file `$PREFIX/lib/jasper/jasper.py` and some files in
`"$PREFIX/lib/jasper/static`. If you want to return to the original
state, you should fetch the files from Jasper's Github-project.

If you prefer a different name, you should follow the instructions on
the project website of Jasper.
