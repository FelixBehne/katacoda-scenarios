Let's check the data size and types of the data we've loaded into memory. <br>

`df.info(memory_usage="deep")`{{execute}}

The data contains more than ten million rows and has multiple different data types. Perfect to show the performance and compression advantages of column-oriented file formats like Parquet.

To write the dataframe to the disk in Parquet format, we can use the builtin dataframe property. This requires, in addition to a file path, an engine and a compression to be specified. As engine we can use the fastparquet implementation, as compression we can choose between the default snappy and a gzip compression. Both come with different advantages for different use cases. 

## Snappy compression 
Snappy is a compression/decompression algorithm build by Google. Its aim is to be very fast at a reasonable compression. This comes at the cost of compression ratio [(Avram, 2011)][1]. Let's see how it performs on a dataframe of the size of 4.3GB in memory. We can time the execution time with the magical function %timeit. <br>

`%time df.to_parquet("historical-trips.parq", engine="fastparquet", compression="snappy")`{{execute}}

Now let's calculate the compression ratio.<br>

`sys.getsizeof(df)/os.path.getsize("historical-trips.parquet")`{{execute}}

The compression rate is a measurement to measure the relative reduction in size that a compression algorithm can produce. In this case Parquet is able to compress the data in a ratio of  8 to one.

## Gzip compression
After benchmarking the snappy compression, let's now see how the gzip compression compares to that. Gzip was created by Jean-loup Gailly and Mark Adler and was firstly released at the 31 October 1992 [(GNU, 2021)][2]. Is's specification can be found [here][3].

`%time df.to_parquet("historical-trips.parquet.gzip", engine="fastparquet", compression="gzip")`{{execute}}

It is noticeable that gzip takes significantly longer, almost 25 times. 
Let's see how this has affected the compression rate.<br>

`sys.getsizeof(df)/os.path.getsize("historical-trips.parquet.gzip")`{{execute}}

We can see a huge difference in the compression ratio. It seems like gzip is able to compress the data almost twice as much compared to snappy. 






[1]: https://www.infoq.com/news/2011/04/Snappy/
[2]: https://www.gnu.org/software/gzip/manual/gzip.html
[3]: https://www.ietf.org/rfc/rfc1952.txt