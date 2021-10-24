from annotation import label

# Plot a line with arrows on both ends
def plot_line(plt, start, end, txt= None):
  plt.annotate(s='', xy=end, xytext=start, arrowprops=dict(arrowstyle='<->'))

  if txt:
    label(plt, txt, end)

def plot_parallel(plt, point, arrow1, arrow2, color):
  plt.annotate(s='', xy=arrow1, xytext=point, arrowprops=dict(arrowstyle='-|>', ec=[0, 0, 0, 0], fc=color, mutation_scale=15), zorder=5)
  plt.annotate(s='', xy=arrow2, xytext=point, arrowprops=dict(          arrowstyle='-|>', ec=[0, 0, 0, 0], fc=color, mutation_scale=15), zorder=5)
