import matplotlib

# Initialize latex

# https://stackoverflow.com/a/53586419/378622
# Conditionally run install if on Google Colab
try:
  import google.colab
  import os
  # We're in colab
  os.system('apt install texlive-fonts-recommended texlive-fonts-extra cm-super dvipng')
except:
  pass

matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

matplotlib.rc('font', size=16)