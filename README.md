# Mastering Quantum Computing with IBM QX

<a href="https://www.packtpub.com/application-development/mastering-quantum-computing-ibm-qx?utm_source=github&utm_medium=repository&utm_campaign=9781789136432 "><img src="https://d255esdrn735hr.cloudfront.net/sites/default/files/imagecache/ppv4_main_book_cover/10518_cover.png" alt="Mastering Quantum Computing with IBM QX" height="256px" align="right"></a>

This is the code repository for [Mastering Quantum Computing with IBM QX](https://www.packtpub.com/application-development/mastering-quantum-computing-ibm-qx?utm_source=github&utm_medium=repository&utm_campaign=9781789136432), published by Packt.

**Learn quantum computing by implementing quantum programs on IBM QX and be at the forefront of the next revolution in computation**

## What is this book about?
Quantum computing is set to disrupt the industry. IBM Research has made quantum computing available to the public for the first time, providing cloud access to IBM QX from any desktop or mobile device. Complete with cutting-edge practical examples, this book will help you understand the power of quantum computing in the real world.

This book covers the following exciting features:
* Study the core concepts and principles of quantum computing 
* Uncover the areas in which quantum principles can be applied 
* Design programs with quantum logic 
* Understand how a quantum computer performs computations 
* Work with key quantum computational algorithms including Shor's algorithm and Grover's algorithm 
Develop the ability to analyze the potential of quantum computing in your industry 

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1789136431) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter01.

The code will look like the following:
```
from qiskit.tools.visualization import plot_histogram
plot_histogram(job_exp.result().get_counts(qc))
```
### To setup book code and Python virtual environment
Run the following commands step wise to set up Python virtual environment:
* ```git clone https://github.com/PacktPublishing/Mastering-Quantum-Computingwith-IBM-QX.git```
* ```cd Mastering-Quantum-Computing-with-IBM-QX```
* ```python3 -m venv book```
* ```source book/bin/activate```
* ```pip install -r requirements.txt```
* ```pip install ipykernel```
* ```ipython kernel install --user --name=bookkernel```

Note: if Python is a version of Python 3 on your system, you may need to/want to type Python instead of Python3 above

### To run a jupyter notebook from commandline, exporting results to Markdown
Use the following command to run Jupyter Notebook:
```
jupyter notebook
```

Navigate to your notebook in the browser. Then go to Kernel | bookkernel in the
notebook's UI.

**Following is what you need for this book:**
If you're a developer or data scientist interested in learning quantum computing, this book is for you. You're expected to have basic understanding of the Python language, but knowledge of physics, quantum mechanics, or advanced mathematics is not required.

With the following software and hardware list you can run all code files present in the book (Chapter 1-).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| All | Python 3.4+ | Cross platform |
| All | qiskit 0.7.0 | Cross platform |
| All | numpy 1.16.0 | Cross platform |
| All | matplotlib 3.0.2 | Cross platform |
| 8 | pygame 1.9.4 | Cross platform |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://www.packtpub.com/sites/default/files/downloads/9781789136432_ColorImages.pdf).

### Related products
* Hands-On Cybersecurity with Blockchain [[Packt]](https://www.packtpub.com/networking-and-servers/hands-cybersecurity-blockchain?utm_source=github&utm_medium=repository&utm_campaign=9781788990189) [[Amazon]](https://www.amazon.com/dp/B07DTB3SLX)

* Blockchain for Enterprise [[Packt]](https://www.packtpub.com/big-data-and-business-intelligence/blockchain-enterprise?utm_source=github&utm_medium=repository&utm_campaign=9781788479745) [[Amazon]](https://www.amazon.com/dp/1788479742)

## Get to Know the Author
**Dr. Christine Corbett Moran**
is a researcher and engineer at NASA JPL, specializing in cybersecurity. She also serves as a guest scientist at Caltech, specializing in astrophysics. Her research spans fundamental physics and computer science, and she has published peer-reviewed papers on astrophysics, astronomy, artificial intelligence, and quantum computing, garnering thousands of citations. Her software products range from iOS applications to quantum computing simulators and have received millions of downloads. She has a PhD and master's in Astrophysics from the University of Zurich, and a B.S. in Computer Science and Engineering, and a B.S. in Physics from MIT. She can be found on Twitter at @corbett.

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSdy7dATC6QmEL81FIUuymZ0Wy9vH1jHkvpY57OiMeKGqib_Ow/viewform) if you have any feedback or suggestions.
