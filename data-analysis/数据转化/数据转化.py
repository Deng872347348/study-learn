
import pandas as pd
import numpy as np
df=pd.DataFrame({'A':[1,2,11,11,33,34,35,40,79,99],

                'B':[1,2,11,11,33,34,35,40,79,99]})
result= pd.cut(x=df["A"],bins=10,right=True,retbins=True)
print(result)