# Jupyter Notebook GUI for a PhysiCell project

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


Make changes to the configuration parameters via the Jupyter notebook GUI, press the 'Write' button, then run your simulation from a shell window, e.g.:

```
heterogeneity myconfig.xml
```
If you don't have your current working directory in your PATH, you will need to be more explicit, e.g.:
```
./heterogeneity myconfig.xml     # on Unix
.\heterogeneity myconfig.xml     # on Windows
```

To launch the notebook, click this button: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/rheiland/binder-test/master?filepath=PhysiCell.ipynb) then click 'Run' in the notebook to render the GUI.
