
Now after you've downloaded the Parquet Python interface, let's use it. To do that we need some data to work with. Execute the following command to download trip history data for the years 2015, 2016 and 2017. The data is provided for free by [Capital Bikeshare (n.d.)][1], under the [Capital Bikeshare Data License Agreement][2]. 

`wget -i urls.txt`{{execute}}

In order to read the data into a pandas dataframe we first must unzip the data. Moreover, its advantageous if we also merge all the data into one csv to reduce the number of I/O operations in the further steps. 

```bash
unzip "*.zip" -d ./data
rm -rf *.zip
cd ./data
sed -i '' -e '1d' *.csv
cat *csv > combined.csv
rm 20*.csv && cd ..
python rocket.py
```{{execute}}

Unzipping and merging can take a few seconds. You know it's done when you see a rocket 🚀 take off. 

Now lets start an interactive python session. 

`clear && ipython`{{execute}}

In order to interact with the data in the following steps lets load it into a pandas dataframe.<br>

```python
import os, sys, pyarrow, datetime
import pandas as pd, pyarrow.parquet as pq
from pyarrow import csv

names = ["Duration", "Start Date", "End Date", "Start station number", "Start station", "End station number", "End station", "Bike number", "Member Type"]
df = csv.read_csv("./data/combined.csv", csv.ReadOptions(column_names=names)).to_pandas()
```{{execute}}

[1]: https://www.capitalbikeshare.com/system-data
[2]: https://www.capitalbikeshare.com/data-license-agreement