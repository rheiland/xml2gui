# Jupyter Notebook GUI for a PhysiCell project

If you simply want to try the notebook, without downloading anything, try clicking on this Binder badge [![Binder](https://img.shields.io/badge/PhysiCell-JupyterGUI-E66581.svg)](https://mybinder.org/v2/gh/rheiland/xml2gui/master?filepath=PhysiCell.ipynb) to run it from your browser.

<!--
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/rheiland/xml2gui/master?filepath=PhysiCell.ipynb) Click the binder badge to play with the notebook from your browser without installing anything.
-->

If you want to install and run the notebook locally on your computer, follow these steps.

This project requires a Python distribution with modules not found in the standard 
library. In particular, it needs matplotlib (and all its dependencies), scipy.io, and Jupyter (notebooks). You have at least a couple of different options:

1) Perhaps the easiest way to get all of this is to download and install the Anaconda Python 3.x distribution:
https://www.anaconda.com/download/
however, that distribution (which includes a LOT of additional modules), is ~500-600MB.

2) If you want to downlod a much smaller bundle, but in multiple steps, you could try to:
- download the Miniconda Python 3.x installer (preferably 64-bit):  (~30 MB)
https://conda.io/miniconda.html

then install the additional, required modules:
```
conda install matplotlib
conda install scipy
conda install jupyter
```
<hr>
After you have the desired Python modules:

- Copy your project's configuration file (.xml) to this directory, calling it "myconfig.xml"
- Copy your project's executable to this directory, e.g., ```heterogeneity```, in the example below.
- Generate the Python module of widgets for your user params (a "tab" in the Notebook GUI). From a Terminal/Command Prompt window, run:

```python gen_user_tab.py myconfig.xml```

Then run the notebook:

```jupyter notebook PhysiCell.ipynb```


When the notebook starts in your browser, in the "Cell" menu, click "Run All".

Make changes to the configuration parameters via the Jupyter notebook GUI, press the 'Write' button, then run your simulation from a shell window, e.g.:

```
heterogeneity myconfig.xml
```
If you don't have your current working directory in your PATH, you will need to be more explicit, e.g.:
```
./heterogeneity myconfig.xml     # on Unix
.\heterogeneity myconfig.xml     # on Windows
```
