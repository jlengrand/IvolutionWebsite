Title: Installation
Tags: face recognition, image processing, computer vision, python, openCV, Ivolution, Facemovie, Everyday, installation
Slug: Installation


__Ivolution should run on most of Windows, Linux and Mac operating systems.__
It was successfully tested on Windows 7, Windows XP and Ubuntu 12.04.

Depending on your operating system though (understand Linux users :), the installation step may require a bit more work.
Please choose below the chapter corresponding to your operating system


## Windows (XP, Vista, Seven)


[Simply download and run the executable](link to installer)(x86).

Once installed, you should be able to run Ivolution through the icon on the Desktop.
Everything should work out of the box without issue.
The software has not been tested (yet) on Windows 8, but there should not be major problems to get it running.

## Ubuntu 12.04

Ivolution is available for Ubuntu in only a few simple steps.
First of all, install Ivolution's dependencies. You can simply do this by running the following line in a terminal :

    :::python
    $ apt-get install my super packages TODO


*__Note__ : You'll need administrator's rights to install the packages (usually means using __sudo__).*


Then, __[download the last stable packages](../pages/Downloads.html)__ and extract here where you want.

Finally, move to the extracted folder in command line and install the package

    :::python
    $ python setup.py install --record ivolution_files

*This time again, you will need administrator's right.*

__Done !__ You can now start using Ivolution by running the following command in a terminal :

    :::python
    Ivolutioner

### Uninstalling the software

*__Note:__*
*The __--record__ option during the install is used to create a list of all the files generated into your system.*
*By default, there is no uninstall solution for python packages and the only solution is to remove all the files one by one.*


You can do this by running the following command in a terminal, where *ivolution_file* is your record file.

    :::python
    [proper command line to uninstall]

**WARNING: This command, if not run correctly, may cause damages! Check the record file first.**

## Other Linux Distributions

For most of all the other Linux distributions, the installation process is similar as the Ubuntu solution __but for the first step__.

You will have to find the name of the packages for your own distribution, or compile them from source if they don't exist.
Here is a list of all the elements you'll need in your system to run Ivolution:

- python 2.7 or more
- opencv 2.4 or more, and all of its dependencies
- wxpython and wxwidgets

Once all the dependencies are satisfied, you can simply [download](link to Linux package) and install the package using the directions __from the Ubuntu chapter__.

## Mac OS

Up to now, I was not able to create application installer as for Windows.
__Mac users should for now follow the Linux guide to install Ivolution.__

An installer may be provided in the future.
You can also try to create it by yourself, using [py2app](link to py2app) (__and in this case, let me know !__)