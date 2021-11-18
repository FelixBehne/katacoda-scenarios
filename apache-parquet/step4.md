After you've learned how to write a dataframe to disk in Parquet with different compression algorithms, in this step you will learn how to read a Parquet file.

Here, too, pandas comes to our rescue and abstracts from the library's own syntax. Let's start with the snappy compressed file.<br>

`%time pd.read_parquet("historical-trips.parquet", engine="fastparquet")`{{execute}}

Now let's read the gzip file.
`%time pd.read_parquet("historical-trips.parquet.gzip", engine="fastparquet")`{{execute}}

So there is no huge performance difference in both compression algorithms. Hence, these should be selected according to the requirements in terms of write speed versus compression.