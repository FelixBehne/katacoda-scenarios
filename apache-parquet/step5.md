In the last steps you learned how to write data from the in-memory representation two disk. In this step you will learn how to read that data back into a dataframe and how the performance of multiple compression algorithms and partitioned and not partitioned data compares.

## Read operations for Snappy vs. Gzip compression
Let's start with the comparison of gzip vs. snappy compression. We again use the magical %time function to measure how long the execution takes.

```
%time df = pq.ParquetDataset("historical_trips.parquet", use_legacy_dataset=False).read_pandas().to_pandas()
%time df = pq.ParquetDataset("historical_trips.parquet.gzip", use_legacy_dataset=False).read_pandas().to_pandas()
```{{execute}}

We can see, that there is no huge performance difference in both compression algorithms. Hence, these should be selected according to the requirements in terms of write speed versus compression.

## Read operations for Partitioned vs. Unpartitioned data
Partitioning especially shines when read operations limit the data to a subset depending on a filtering condition. Our data has been partitioned by the Start and End Date. Let's filter the data therefore to one date and compare the performance of both data representations.<br>

```
%time df = pq.ParquetDataset("historical_trips_partitioned", filter=[("Start Day", "=", datetime.date(2015,01,01))] use_legacy_dataset=False).read_pandas().to_pandas()

%time df = pq.ParquetDataset("historical_trips_partitioned", filter=[("Start Day", "=", "2015-01-01")] use_legacy_dataset=False).read_pandas().to_pandas()
```{{execute}}

The read operation on the partitioned data is four times faster than the one on unpartitioned data. Hence, we can see that partitioning allows for an enormous performance increase.