import cmaps
import h5py
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


class DrawConvectiveCloud(object):
    def __init__(self, data_path, lon_path, lat_path,channel):
        self.data_path = data_path
        self.lon_path = lon_path
        self.lat_path = lat_path
        self.channel = channel
        self.sat_data = list()
        self.lat = list()
        self.lon = list()

    def readlatlon(self):
        h5file = h5py.File(self.data_path, 'r')
        data = h5file.get(self.channel)
        info = list(data.attrs.items())
        sat_data = data.get('Data')[:]
        print(sat_data.max())
        print(sat_data.min())
        self.sat_data = sat_data.T
        self.lon = np.loadtxt(open(self.lon_path, "rb"), delimiter=",", skiprows=0)
        self.lat = np.loadtxt(open(self.lat_path,"rb"),delimiter=",",skiprows=0)

    def draw(self, center, picname, pad_dot=0, dpi=0):
        fig = plt.figure(figsize=(10, 10), dpi=dpi)
        ax = fig.add_subplot(111)
        ax.set_axis_off()
        m = Basemap(
            epsg=3857,
            llcrnrlon=center[1]-2, llcrnrlat=center[0]-2,
            urcrnrlon=center[1]+2, urcrnrlat=center[0]+2,
            resolution='l', area_thresh=10000
        )
        x, y = m(self.lon, self.lat)  # 将lats / lons转换为地图投影坐标
        # ct = np.array([[0, 151, 1], [255 , 255, 0],[250, 203, 1], [252, 123, 0],
        #                [254, 0, 0],[200, 1, 0], [147, 2, 0],[255, 0, 254]]) / 255
        # # m.contourf(x, y, self.sat_data, [750, 850], colors=[ct[0], ct[0]])
        # m.contourf(x, y, self.sat_data, [850, 875], colors=[ct[0], ct[0]])
        # m.contourf(x, y, self.sat_data, [875, 900], colors=[ct[1], ct[1]])
        # m.contourf(x, y, self.sat_data, [900, 925], colors=[ct[2], ct[2]])
        # m.contourf(x, y, self.sat_data, [925, 950], colors=[ct[3], ct[3]])
        # m.contourf(x, y, self.sat_data, [950, 975], colors=[ct[4], ct[4]])
        # m.contourf(x, y, self.sat_data, [975, 1000], colors=[ct[5], ct[5]])
        # m.contourf(x, y, self.sat_data, [1000, 1020], colors=[ct[6], ct[6]])
        # m.contourf(x, y, self.sat_data, [1020, 1500], colors=[ct[7], ct[7]])
        levels = np.linspace(680, 1050, 50)
        m.contourf(x, y, self.sat_data, levels=levels, cmap=cmaps.selfgray)
        plt.show()
        plt.savefig(picname,
                    transparent=True,
                    bbox_inches='tight',
                    pad_inches=pad_dot / dpi
                    )
        plt.close()




