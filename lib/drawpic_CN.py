# import cmaps
import h5py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


class DrawConvectiveCloud(object):
    def __init__(self, data_path, channel):
        self.data_path = data_path
        self.channel = channel
        self.sat_data = list()
        self.lat = list()
        self.lon = list()

    def readlatlon(self):
        h5file = h5py.File(self.data_path, 'r')
        data = h5file.get(self.channel)
        info = list(data.attrs.items())
        sat_data = data.get('Data')[:]
        self.sat_data = sat_data.T
        Prjct = str(info[3][1], 'utf-8')
        Width = info[4][1]
        Height = info[5][1]
        W0 = info[6][1]
        E0 = info[7][1]
        Space = info[8][1]

        if Prjct == 'E':
            la = (Height * Space / 100.0 - Space / 100.0) / 2
            Minlat = W0 - la
            Maxlat = W0 + la
            lo = (Width * Space / 100.0 - Space / 100.0) / 2
            Minlon = E0 - lo
            Maxlon = E0 + lo

        lon = list()
        lat = list()
        for x in range(0, Width):
            for y in range(0, Height):
                lon.append((Maxlon - Minlon) * x / Width + Minlon)
                lat.append((Maxlat - Minlat) * (Height - y) / Height + Minlat)
        self.lon = np.array(lon).reshape(1920, 1080)
        self.lat = np.array(lat).reshape(1920, 1080)

    def draw(self, center, picname, PAD_DOT=0, DPI=0):
        fig = plt.figure(figsize=(40, 40), dpi=DPI)
        ax = fig.add_subplot(111)
        ax.set_axis_off()
        m = Basemap(
            epsg=3857,
            llcrnrlon=center[1] - 1, llcrnrlat=center[0]-1,
            urcrnrlon=center[1] + 1, urcrnrlat=center[0]+1,
            resolution='l', area_thresh=10000
        )
        x, y = m(self.lon, self.lat)  # 将lats / lons转换为地图投影坐标
        m.contourf(x, y, self.sat_data)
        plt.savefig(picname,
                    transparent=True,
                    bbox_inches='tight',
                    pad_inches=PAD_DOT / DPI
                    )
        plt.close()




