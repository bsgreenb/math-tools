def label(plt,text,coords):
  plt.annotate(text, # this is the text
                 coords, # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center',
                 fontsize=16) # horizontal alignment can be left, right or center