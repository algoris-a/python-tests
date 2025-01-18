# For this to work, need to install/update Pillow:
# pillow-11.0.0
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
from openpyxl.drawing.spreadsheet_drawing import OneCellAnchor, AnchorMarker
from openpyxl.drawing.xdr import XDRPositiveSize2D
from openpyxl.utils.units import pixels_to_EMU, cm_to_EMU

# This will create spakline-like small graph

dpi = 300

# Define test list with values
data_list = [0.000, 0.360, 0.753, 0.546, 0.984, 0.233, 0.531, 1.239, 1.833, 1.539, 2.043, 2.197, 0.000]
data= pd.Series(data_list)

# Create small plot (no titles, no labels)
fig, ax= plt.subplots()
ax.plot(data, linewidth=0.25)

# Remove frame from the plot
# Selecting the axis-X making the bottom and top axes False.
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
# Selecting the axis-Y making the right and left axes False
plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)

# Iterating over all the axes in the figure
# and make the Spines Visibility as False
for pos in ['right', 'top', 'bottom', 'left']:
    plt.gca().spines[pos].set_visible(False)

# plt. show()

# save to jpeg
fig.set_size_inches([62/dpi, 18/dpi])
fig.savefig(r'C:\Users\agori\Python\python-tests\pyplot_test.png', dpi=dpi)

# create test excel file with added jpeg
wb = openpyxl.Workbook()

ws = wb.worksheets[0]
ws['A2'].value = 'Plot:'

img = openpyxl.drawing.image.Image(r'C:\Users\agori\Python\python-tests\pyplot_test.png')

# simple way to add image
# ws.add_image(img, 'B2')
# more refined way to add image (with small offset from top corner of the cell to
# avoid covering top and left cell grid lines
# source: https://stackoverflow.com/questions/55309671/moreprecise-image-placement-possible-with-openpyxl-pixelcoordinates-instead

size= XDRPositiveSize2D(pixels_to_EMU(img.width), pixels_to_EMU(img.height))
# EMU: English Metric Unit (one inch equates to 914400 EMUs and a centimeter is 360000)
cellh = lambda x: cm_to_EMU((x * 49.77)/99)
cellw = lambda x: cm_to_EMU((x * (18.65-1.71))/10)

col_offset= cellw(0.01)
row_offset= cellh(0.05)

# row/column indexing starts with 0
marker= AnchorMarker(col=1, colOff=col_offset, row=1, rowOff=row_offset)
img.anchor = OneCellAnchor(_from=marker, ext=size)
ws.add_image(img)

wb.save(r'C:\Users\agori\Python\python-tests\pyplot_test.xlsx')
