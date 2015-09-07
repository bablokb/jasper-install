Jasper Installation Script
==========================

This repository contains an installation script for all the libraries and
dependencies of [jasper](http://jasperproject.github.io/ "jasper").

While the jasper project provides an image for the model 1 of the
Raspberry Pi, there is no image for the model 2. Instead of mastering a
big image, I just provide a ready to run installation script.

The installation script `jasper-install` assumes that you start of with
a clean installation of Raspbian-Wheezy. A simple

    sudo su -
    ./jasper-install all

should do the job (assuming that you copied the installation script to root's
home-directory `/root`). The script will create a (large) logfile 
`/root/jasper-install.log`, please check that file for errors.

** This is work in progress (alpha-stage), don't use it yet **

