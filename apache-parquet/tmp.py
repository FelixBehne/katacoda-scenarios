import time

import datatable as dt

data_path = "~/Downloads/pp-complete.csv"


start = time.time()
df = dt.fread(data_path)
print(df.shape)
print(df.to_pandas().memory_usage(deep=True))
end = time.time()
print("time elapsed {}".format(end - start))
