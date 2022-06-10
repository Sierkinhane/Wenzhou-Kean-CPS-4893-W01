### 1. Install Anaconda on Your Platform

**Step 1 - Download Anaconda**

​      On the web browser, in the official site of [anaconda](https://www.anaconda.com/products/distribution#Downloads), you can download the anaconda installer according to your system.

![](images/anaconda.png)

**Step 2 - Run Executable Installer**

- Windows

  Run the installer and click **next**.

  ![](images/win-install.jpg)

  Make sure to select the checkbox of **Add Anaconda3 to my PATH environment variable**.

  ![](images/add-path.jpg)

- MacOS

  1. Open the **.pkg** installer and follow the installation instructions. It is advised that you install **Anaconda** for the current user and that **Anaconda** **is added to your PATH**.

  2. Once Anaconda is installed, you need to load the changes to your `PATH` environment variable in the current terminal session.

     Open the MacOS Terminal and type:

     ```
     $ cd ~
     $ source .bashrc
     ```

- Linux

  Open the Linux terminal and type and press **enter**:

  ```
  $ bash anaconda-xxx.sh
  ```

  Please add **PATH** to the environment:

  ```
  $ vim ~/.bashrc
  ```

  Add `export PATH="/your/path/to/anaconda3/bin:$PATH"` to **.bashrc**

**Step 3 - Verify Python is installed on your platform**

​     Open the **command prompt** (windows) or **Terminal** (mac os, linux) and type:	

```
$ python
```

You should see something like

```
Python 3.6.3 | Anaconda Inc. |
```

At the Python REPL (the Python `>>>` prompt) try:

```
>>> import this
```

If you see the Zen of Python, the installation was successful. Exit out of the Python REPL using the command `exit()`. Make sure to include the double parenthesis `()` after the `exit` command.

```
>>> exit()
```

### 2. Install Sublime Text

For convinience, I recommend sublime text for coding small projects. You can download it on [the official website](https://www.sublimetext.com/) according to your system.

### 3. Read and Show An Image

1. Download the source code at [here](https://github.com/Sierkinhane/Wenzhou-Kean-CPS-4893-W01/archive/refs/heads/master.zip) and uzip them:

```
import cv2

# load an image
image = cv2.imread("images/logo_cn.png")

# show the image
cv2.imshow('a window', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

2. Open the **command prompt** (windows) or **Terminal** (mac os, linux) at the current dirctory, we should install some packages via pip:

```
$ pip install opencv-python
```

3. Read and show an image:

```
$ python read_and_show_an_image.py
```

