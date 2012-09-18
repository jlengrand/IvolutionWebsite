Title: About
Tags: face recognition, image processing, computer vision, python, openCV, Ivolution, Facemovie, Everyday, About
Slug: About

### Other informations

__Ivolution__ was created as a pet project, to help a friend currently [travelling around the world](http://ungrandtour.blogspot.nl/) (Warning, french inside).
It is still in early development, but pretty much already achieves what it was created for !

### License

The project is under the __[simplified BSD license](http://www.linfo.org/bsdlicense.html)__. So here are the rules :

<center>
Copyright (c) 2012, Julien Lengrand-Lambert
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the organization nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

</center>

[Here is where you can learn more about this license]http://www.linfo.org/bsdlicense.html).

The important thing to note is that __I can not be taken responsible for any problem you might encounter__ (but I'd be glad to help you solve them if you have some).
I never experienced any problem using Ivolution (nor all my users), but you are advised to make a copy of the images your are about to process first.

### Technology used

To create this project, I used a lot of different tools that are going to be listed here.

- The whole project is written in [Python](http://www.google.nl/url?sa=t&rct=j&q=python&source=web&cd=1&cad=rja&ved=0CCUQFjAA&url=http%3A%2F%2Fwww.python.org%2F&ei=g61TUJeiJ4nK0QXjwYCgBw&usg=AFQjCNG7frXlIQC6rpM3VV6f5i7nq5VeIg) (2.7). It allows rapid prototyping, has a, Python and huge amount of libraries available and also has the advantage to be portable (Windows, Linux, Web development, . . . ). I know I won´t be limited in the future by using Python.
- All the image processing is performed using the excellent [OpenCV](http://www.google.nl/url?sa=t&rct=j&q=opencv&source=web&cd=8&cad=rja&ved=0CEkQFjAH&url=http%3A%2F%2Fopencv.org%2F&ei=ja1TUMzYFaX80QX964HYCQ&usg=AFQjCNGUr-UTYvy3hRjaFyy2oCg43JU9Vw) library, through its Python bindings. If you have to develop image processing algorithms quickly and efficiently, Python and OpenCV are the tools you want. I used the OpenCV 2.4 version, to be compatible with the current package of Ubuntu.
- I started developing the GUI in [GTK+](http://www.google.nl/url?sa=t&rct=j&q=pygtk&source=web&cd=1&cad=rja&ved=0CCMQFjAA&url=http%3A%2F%2Fpygtk.org%2F&ei=k61TUJGQFKik0AXpv4GABg&usg=AFQjCNECVx76WbL-0AoZB9sMwXU5lYNQuQ) ([here is a picture of what it looked like](https://dl.dropbox.com/u/4286043/ivolution_gtk.png)), but finally switched to [WxPython](http://www.google.nl/url?sa=t&rct=j&q=wxpython&source=web&cd=1&cad=rja&ved=0CCMQFjAA&url=http%3A%2F%2Fwxpython.org%2F&ei=mq1TUP29EaLA0QWY64C4Bw&usg=AFQjCNE8M7EcUd4oQf5NyzG9qiWL15zPhQ). GTK+ is nice for Linux environments but made my software OS dependant, which I didn´t want.
- I used [py2exe](http://www.py2exe.org/) combined to [NSIS](http://nsis.sourceforge.net/Main_Page) in order to create proper Windows executables. Both are simple to use, even though you may something have to dig into 3 years old forum posts to find the solution to your problems. I´d definitely use them again if needed in future projects.
- In order to automate everything I used [ant](http://ant.apache.org/). I love ant because you can do pretty much everything you want with it, from compiling to move folder back and forth or even prepare coffee.
Coming from the linux world, ant is a must if you want to save time.
- Finally, this whole website was created using [Pelican](http://docs.getpelican.com/en/latest/index.html). I was searching for an Octopress equivalent, but written in Python.
I found Pelican and stick with it since them. The documentation is really complete and you can start working in minutes. Plus it was created by a french man!

That´s all for now folks. If you have other questions, just ask ;)


### About the developer

My name is __[Julien Lengrand-Lambert](https://plus.google.com/u/0/107343304730454368817)__, and I am as french software engineer currently living in the Netherlands.
You can learn more about me (and the development of Ivolution) on __[my website](http://www.lengrand.fr)__, or on my __[G+ page](https://plus.google.com/u/0/107343304730454368817)__.

To follow my projects real time, you can also watch me on __[GitHub](https://github.com/jlengrand)__.

For Ivolution related matters, the official email address is __ivolution.app@gmail.com__, but you can also mail me personally using __ju.lien@leng.rand.fr__ (without the dots in julien and lengrand :)).


### Acknowledgements

the following is a list of persons or ressources that helped me developing Ivolution :

- As a starter for the application, I used an [excellent face detection example](http://japskua.wordpress.com/2010/08/04/detecting-eyes-with-python-opencv/) from __Japskua__.
- I use __Gene Cash__'s [exif library](http://sourceforge.net/projects/exif-py/) to extract information from EXIF metadata contained in the images
- The current logo of Ivolution comes from a picture by __[Luc Viatour](http://www.Lucnix.be)__ and taken from Wikipedia.
- Ivolution was developed based on an original idea from __Axel Catoire__, who is currently [travelling around the world](http://ungrandtour.blogspot.com/).
