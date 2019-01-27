# Mastering-Quantum-Computing-with-IBM-QX
Mastering Quantum Computing with IBM QX, by Dr. Christine Corbett Moran published by Packt


# To setup your virtual environment:
```
git clone https://github.com/PacktPublishing/Mastering-Quantum-Computing-with-IBM-QX.git
python3 -m venv book
source book/bin/activate
pip install -r requirements.txt
pip install ipykernel
ipython kernel install --user --name=bookkernel
```
# To run Jupyter notebook
`jupyter notebook`

Then go to Kernel->bookkernel in the UI

## To run a jupyter notebook from commandline, exporting results to Markdown
`jupyter nbconvert --to markdown --execute Chapter1_WhatIsQuantumComputing/Hello\ Quantum\ World.ipynb --ExecutePreprocessor.kernel_name=bookkernel`