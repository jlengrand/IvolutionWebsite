Title: Installation
Tags: face recognition, image processing, computer vision, python, openCV, Ivolution, Facemovie, Everyday, installation
Slug: Installation


Ivolution should run on most of Windows, Linux and Mac operating systems.
It was successfully tested on Windows 7, Windows XP and Ubuntu 12.04.

Depending on your operating system, the installation step may require a bit more work.
Please choose below the chapter corresponding to your operating system


Windows (XP, Vista, Seven)

Simply download and run the executable here (x86).
Once installed, you should be able to run Ivolution through the icon on the Desktop.
Everything should work out of the box without issue.

The software has not been tested (yet) on Windows 8, but there should not be major problems to get it running.

Ubuntu 12.04

Ivolution is available in Ubuntu in only a few simple steps.
First of all, install Ivolution's dependencies. You can simply do this by running the following line in a terminal :
apt-get install . . .

Note : You'll need administrator's rights to install the packages (usually means using sudo).

Then, download the last stable packages here and extract here where you want.

Finally, move to the extracted folder in a command line and install the package
python setup.py install --record ivolution_files
This time again, you will need administrator's right.

Done ! You can now start using Ivolution by running
Ivolutioner
in a terminal.

Note:
The --record option during the install is used to create a list of all the files generated into your system.
By default, there is no uninstall solution for python packages and the only solution is to remove all the files one by one.

You can do this by running

in a command line, where ivolution_file is your record file.

WARNING: This command, if not run correctly, may cause damages! Check the record file first.

Linux

For most of all the other Linux distributions, the installation process is similar as the Ubuntu solution but for the first step.

You will have to find the name of the packages for your own distribution, or compile them from source if they don't exist.
Here is a list of all the elements you'll need in your system to run Ivolution:

Once all the dependencies are satisfied, you can simply download and install the package using the directions from the Ubuntu chapter.

Mac OS

Up to now, I was not able to create application installer as for Windows.
Mac users should for now follow the Linux guide to install Ivolution.

An installer may be provided in the future.
You can also try to create it by yourself, using py2app (and in this case, let me know !)