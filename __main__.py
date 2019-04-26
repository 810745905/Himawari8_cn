import os
import json
from lib import drawpic_CN

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PIC_FILE_0 = os.path.join(BASE_DIR, '0')
ROUTE_CONFIG_FILE = os.path.join(BASE_DIR, 'latlon', 'center4_4.json')
data_path = os.path.join(BASE_DIR, 'data', os.listdir(os.path.join(BASE_DIR, 'data'))[0])
lon_path = os.path.join(BASE_DIR, 'latlon', 'lon.csv')
lat_path = os.path.join(BASE_DIR, 'latlon', 'lat.csv')

with open(ROUTE_CONFIG_FILE, 'r') as f:
    f = json.load(f)
channel = 'VIS'
a = drawpic_CN.DrawConvectiveCloud(data_path, lon_path, lat_path, channel)
a.readlatlon()

for center in f:
    picname0 = os.path.join(PIC_FILE_0, f'{str(center[0]+1)}_{str(center[0]-1)}_{str(center[1]-1)}_{str(center[1]+1)}.png')
    a.draw(center, picname0, pad_dot=-11.2, dpi=100)

    # picname1 = os.path.join(PIC_FILE_1, f'{str(center[0]+1)}_{str(center[0]-1)}_{str(center[1]-1)}_{str(center[1]+1)}.png')
    # a.draw(center, picname1, PAD_DOT=-104.9, DPI=200)
    #
    # picname2 = os.path.join(PIC_FILE_2, f'{str(center[0]+1)}_{str(center[0]-1)}_{str(center[1]-1)}_{str(center[1]+1)}.png')
    # a.draw(center, picname2, PAD_DOT=-155, DPI=300)

    # picname3 = os.path.join(PIC_FILE_3, f'{str(center[0]+1)}_{str(center[0]-1)}_{str(center[1]-1)}_{str(center[1]+1)}.png')
    # a.draw(center, picname3, PAD_DOT=-204.5, DPI=400)
    #
    # picname4 = os.path.join(PIC_FILE_4, f'{str(center[0]+1)}_{str(center[0]-1)}_{str(center[1]-1)}_{str(center[1]+1)}.png')
    # a.draw(center, picname4, PAD_DOT=-254.5, DPI=500)




