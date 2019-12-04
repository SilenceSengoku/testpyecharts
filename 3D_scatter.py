import random
from pyecharts import options as opts
from pyecharts.charts import Scatter3D
import pandas as pd

dataset = pd.read_csv(r'C:\Users\Administrator\PycharmProjects\Isolation Forest'
                       r'\optimization\Iso_list.csv', engine='python')


#print(std_MA)
minscore = min(dataset['IsoFst_Score'])
maxscore = max(dataset['IsoFst_Score'])
print(minscore)
print(maxscore)


data = [list(z)
        for z in zip(dataset['x'],dataset['y'],dataset['IsoFst_Score'])]

c = Scatter3D().add("feature", data ,
                    grid3d_opts = opts.Grid3DOpts(width=200, height=200, depth=200),
                    #Axis3DOpts = opts.Axis3DOpts

                    #opts(boxWidth=dataset['x'],boxHeight = dataset['y'],boxDepth = ['IsoFst_Score'])
                    ).set_global_opts(title_opts=opts.TitleOpts("Scatter3D-Isolation Forest"),
                                      visualmap_opts=opts.VisualMapOpts(range_color=[ '#FF0000','#313695'],#色码对照表：http://www.ezxcom.com/gn/ztools/color/index.php
                                                              min_=minscore,max_ = maxscore))
#print(Faker.values())
'''
c = (
    Scatter3D()
        .add_xaxis("x", dataset['x'])
        .add_yaxis("y", dataset['y'])
        .add_zaxis("y", dataset['IsoFst_Score'])

)
'''
c.render("Isolation_Forest_feather.html")