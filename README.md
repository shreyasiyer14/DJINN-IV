#DJINN-IV Game Engine. 
[![Codeship Status for djeof-1/DJINN-IV](https://codeship.com/projects/edde0000-92bf-0133-9835-4219f5e7a61a/status?branch=master)](https://codeship.com/projects/124754)
![Build] (https://travis-ci.org/djeof-1/DJINN-IV.svg?branch=master)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/ce4e118f40f94c3f81a26ba3204cea61/badge.svg)](https://www.quantifiedcode.com/app/project/ce4e118f40f94c3f81a26ba3204cea61)
![License](https://poser.pugx.org/pugx/badge-poser/license?format=plastic%22%3E)
<br />
![Image](https://avatars1.githubusercontent.com/u/13732949?v=3&u=9e161249d86f665b78a1da2194ac28258f086e70&s=140)
<br />
##NOTE
The builds of DJINN have been failing on various deployment tools (Travis CI and Codeship), just because `pygame` cannot be installed simply by using `pip install pygame`. For installing pygame, `apt-get` fetches the correct package. I have already made a `PRE-INSTALL.sh` script file to install all the necessary dependencies. So, let the `build: failing` not scare you from using DJINN :)
<br />
##About DJINN
DJINN IV is a full-fledged 3D game engine, built with OpenGL and Pygame, for Python programming language (Python 2.7 is supported at the moment. Further support will be introduced in future releases) . DJINN IV is a relatively easier to use engine compared to others available in the market, because not only Physics is taken care of for your game, but also other event handling, graphical rendering, textures, and loads more. DJINN IV has a new algorithm for collision detection, to make it seem as realistic as possible, but still to be implemented. This engine, with decent 3D game graphics, is heavily suitable for FPS, SPS, and TPS, as well as MMORPG, and others.
<br />
##Why DJINN? <br />
 Now, we know that there are plenty of professional-quality engines available in the market right now, and that too for free (Consider UDK, Cocos-2Dx, Box2D, etc.) But, the problem is that these engines mostly target C,C++, JavaScript, or HTML5. Very few engines actually are totally built in, and support Python. Also, the engines which are built have a bit cryptic source code, which makes it difficult for the novice developers to contribute to. But, DJINN being totally built using Python, Pygame, and PyOpenGL, makes contributing easier, because of clean organization of source files, and cleaner syntax (Python!). This helps in overall maintainance of the code, as well as makes the bug tracking easier. <br />
 
Considering the small size of the entire engine, it is a nifty tool that can help save you hours of time. Low level integration is on our TODO list, and soom in future releases, it will be implemented. Hardware acceleration will also be implemented. 

  DJINN-IV is an open source game engine, and contributers are welcome to help make DJINN one of the most desirable tools for game developers and enthusiasts.
  
<b><u>REQUIREMENTS:</u></b>

1) Pygame <br />
2) PyOpenGL <br />
3) PyOpenGL accelerate <br />
4) Python 2.7 (maybe it will work for older versions.)
  
<br />
<b><u>INSTALLATION:</u></b>
<br />

<b>Before starting </b> You need to make sure that you have Python installed on your system. For checking, goto the terminal and type in: `python` and an interpreter should start. Now, check the python version which is displayed on the first line of the interpreter. Make sure it is 2.7. If not, goto www.python.org, and goto the "Downloads" page, and download 'Python 2.7 - 32 bit' version (32-bit is crucial). Python for Windows can be downloaded too. Now, with that properly set up, proceed to the following steps: </br>
1) Download the repository as a .ZIP file, and extract it somewhere. Open up the terminal, and change your working directory to the extracted folder. Now, in the terminal type: <br />`chmod +x PRE-INSTALL.sh`<br/>`./PRE-INSTALL.sh` <br />

2) The above commands install the necessary dependencies on your system, for the engine to work upon. <br />

3) Next, you have to install the game engine onto your system, so as to make it work globally. For this, type in the following command in the terminal: <br />
`sudo python setup.py install`<br />

4) This will install djinn on your system, and now it is ready to use. Check the test/example files, in 'tests' folder, to learn about how DJINN actually works,and how to make it work.

##Screenshots
<b>.OBJ model loader </b><br />
![Image](https://github.com/djeof-1/DJINN-IV/blob/master/screenshots/1.png?raw=true)
<b> 2D texturing on shapes. </b> <br />
![Image](https://github.com/djeof-1/DJINN-IV/blob/master/screenshots/2.png?raw=true)
<b> Various drawable 3D and 2D shapes. </b> <br />
![Image](https://github.com/djeof-1/DJINN-IV/blob/master/screenshots/3.png?raw=true)

