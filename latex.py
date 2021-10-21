import matplotlib

# Initialize latex
matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

matplotlib.rc('font', size=16)