import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime

data = pd.read_csv(r'C:\Users\Soulayman\Desktop\DataFile\Covid.csv')
data[["Region","Confirmed","Deaths","Recovered"]].set_index("Region")
