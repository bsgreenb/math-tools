def label(plt,text,coords, offset=(0,10), fontsize=16):
  plt.annotate(text, # this is the text
                 coords, # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=offset, # distance from text to points (x,y)
                 ha='center',
                 fontsize=fontsize) # horizontal alignment can be left, right or center