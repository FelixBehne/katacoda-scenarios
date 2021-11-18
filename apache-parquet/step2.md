# Prepare the environment 

Now after you've downloaded the Parquet Python interface, let's use it. To do that we need some data to work with. Execute the following command to download trip history data for the years 2015, 2016 and 2017. The data is provided for free by [Capital Bikeshare (n.d.)][1], under the [Capital Bikeshare Data License Agreement][2]. 

`wget -i urls.txt`{{execute}}

In order to read the data into a pandas dataframe we first must unzip the data. Moreover, its advantageous if we also merge all the data into one csv to reduce the number of I/O operations in the further steps. 

```
unzip "*.zip" -d ./data
rm -rf *.zip
cd ./data
sed -i 1d *.csv
cat *csv > combined.csv
rm 20*.csv && cd ..
python rocket.py
```{{execute}}

Wait now until the rocket 🚀 took of and proceed with starting an interactive Python session to load the data into memory.
``` 
clear
ipython 
import pandas as pd
from fastparquet import ParquetFile, write

df = df = pd.read_csv(
    "./data/combined.csv",
    names=[
        "Duration",
        "Start Date",
        "End Date",
        "Start station number",
        "Start station",
        "End station number",
        "End station",
        "Bike number",
        "Member Type",
    ],
    parse_dates=["Start Date", "End Date"],
)

```{{execute}}

[1]: https://www.capitalbikeshare.com/system-data
[2]: https://www.capitalbikeshare.com/data-license-agreement