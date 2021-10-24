from annotation import label

# Plot a line with arrows on both ends
def plot_line(plt, start, end, txt= None):
  plt.annotate(s='', xy=end, xytext=start, arrowprops=dict(arrowstyle='<->'))
  if txt:
    label(plt, txt, end)