import pandas as pd
s = pd.Series([10,20,30,40],
              index=['a','b','c','d'],
              name='Marks')
print(s)

import pandas as pd
temperature = pd.Series(
    [10,20,30,40,50],
    index = ["Sunday","Monday","Thursday","Friday","Saturday"]
)
print(temperature)