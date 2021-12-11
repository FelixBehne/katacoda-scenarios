Let's check the data size and types of data we've loaded into memory. <br>

`df.info(memory_usage="deep")`{{execute}}

The data contains more than ten million rows and has multiple different data types. Perfect to show the performance and compression advantages of column-oriented file formats like Parquet.

To be able to map the data currently stored in-memory to disk, we must first convert the data to an arrow table.<br>
`df_table = pyarrow.Table.from_pandas(df)`{{execute}}

Parquet allows for multiple compression algorithms to be applied, all coming with advantages and disadvantages. In the following, we will explore the two most popular algorithms already implemented in Pyarrow. 

## Snappy compression 
Snappy is a compression/decompression algorithm built by Google. It aims to be very fast at a reasonable compression. This comes at the cost of compression ratio [(Avram, 2011)][1]. Let's see how it performs on a dataframe of the size of 3.1GB in memory. We can time the execution time with the magical function %time. <br>

`%time pq.write_table(df_table, "historical_trips.parquet", compression="snappy")`{{execute}}

Now let's calculate the compression ratio.<br>

`sys.getsizeof(df)/os.path.getsize("historical_trips.parquet")`{{execute}}

The compression rate is a measurement to measure the relative reduction in size that a compression algorithm can produce. In this case, Parquet can compress the data in a ratio of approximately seventeen to one.

## Gzip compression
After benchmarking the snappy compression, let's now see how the gzip compression compares to that. Gzip was created by Jean-loup Gailly and Mark Adler and was firstly released on 31 October 1992 [(GNU, 2021)][2]. Is's specification can be found [here][3].

`%time pq.write_table(df_table, "historical_trips.parquet.gzip", compression="gzip")`{{execute}}

It is noticeable that gzip takes significantly longer.
Let's see how this has affected the compression rate.<br>

`sys.getsizeof(df)/os.path.getsize("historical_trips.parquet.gzip")`{{execute}}

We can see a huge difference in the compression ratio. It looks like, that gzip can compress files way more efficiently. On the other hand, however, it takes way more time to compress a given file.




[1]: https://www.infoq.com/news/2011/04/Snappy/
[2]: https://www.gnu.org/software/gzip/manual/gzip.html
[3]: https://www.ietf.org/rfc/rfc1952.txt