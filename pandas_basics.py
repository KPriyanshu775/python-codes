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

#  Practicing the pandas series indexing
# First
import pandas as pd
s = pd.Series(
    [10,20,30,40,50],
    index = ["A","B","C","D","E"]
)
s["A"]
s["C"]

# Second problem
import pandas as pd
s = pd.Series([10,20,30,40,50])
print(s)






