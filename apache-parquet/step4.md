# Partitioning

In the previous step you've learned how to map data from an in-memory representation into one file. However, this approach lead to performance penalties, in cases where data get's added incrementally or read operations depend on one or multiple variables. To overcome this penalties, Parquet offers a way of partitioning data into multiple small pieces.

Parquet creates a folder for each key and treats the resulting file system as one coherent file. This in combination with columnar storage and columnar compression can significantly improve I/O performance.

On the basis of which column the data should best be partitioned, depends considerably on the use case. However, care should be taken that the cardinality of the column on the basis of which partitioning is to be carried out is not too high in order to counteract the creation of a very large number of small files.

In our case, let's partition our data on the start date. One can easily imagine many queries that depend on this information.
However, we first need to reduce its resolution to the date only to avoid the creation of two many small files.<br>

```
df["Start Day"] = df["Start Date"].dt.date
```{{execute}}
Now we can use the newly created columns as basis for the partitioning.<br>

`pq.write_to_dataset(df_table, 'historical_trips_partitioned', partition_cols=["Start Date"], use_legacy_dataset=False)`{{execute}}

Let's see what happened.<br>
```
!cd .. && ls | head -4
```{{execute}}

As expected, a folder has been created, containing the data partitioned by the columns given.