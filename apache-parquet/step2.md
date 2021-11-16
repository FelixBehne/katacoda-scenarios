# Prepare the environment 

To use Parquet and explore its features we first need some data to work with. The data size should ideally be at a multi-million row scale to get a glance of the dimensions Parquet is originally designed for. 
We therefore use trip history data provided by [Capital Bikeshare (n.d.)][1], under the [Capital Bikeshare Data License Agreement][2].

Execute the following commands to download and extract the data.<br>

`wget -i urls.txt && unzip "*.zip" -d ./data  && rm -rf *.zip`{{execute}}

In this scenario we're going to explore Parquet and its performance benefits in comparison to Avro, as row-oriented file format, through python. We therefore need to install their according python implementations.<br>

`pip install fastparquet fastavro`{{execute}}

[1]: https://www.capitalbikeshare.com/system-data
[2]: https://www.capitalbikeshare.com/data-license-agreement