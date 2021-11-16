According to a study conducted by [Frost & Sullivan (2020)][1], Big Data analytics market revenue is forecasted to grow with a compound annual growth rate of almost 30%. 
This is accompanied by the demand for efficient storage and processing solutions that can meet the requirements of analytical processing applications (OLAP). 

One of the most widely used platforms for this purpose is Apache Hadoop [(Mavridis and Karatza, 2017)][2]. Hadoop is a set of software utilities that facilitates distributed storage and data processing based on the MapReduce processing model [(Fundation, n.d.)][3]. 

|Apache Hadoop|Apache Parquet|
|:-:|:-:|
|![Apache Hadoop](https://upload.wikimedia.org/wikipedia/commons/3/38/Hadoop_logo_new.svg)|![Apache Parquet](https://upload.wikimedia.org/wikipedia/commons/4/47/Apache_Parquet_logo.svg)|


Data can be stored in a variety of data formats, all of which have different advantages. One of the most famous formats is Apache Parquet. 

Apache Parquet is an open-source, general-purpose, columnar file format, that's available to any project in the Hadoop ecosystem. It was initially released in July 2013 as a joint effort by Twitter and Cloudera. The official announcement can be found [here][4].

Parquet is build based on the record shredding and assembly algorithm as described by Google engineers in their paper [Dremel: Interactive Analysis of Web-Scale Datasets](https://research.google/pubs/pub36632/). This algorithm allows for a translation of objects into a columnar format and is, according to the official [documentation](https://parquet.apache.org/documentation/latest/), superior to simply flattening the objects.

This Katacoda is build for absolute beginners and intended to teach the basic interaction with parquet utilizing the python library [fastparquet](https://github.com/dask/fastparquet).



[1]: https://www.statista.com/statistics/947745/worldwide-total-data-market-revenue/
[2]: https://doi.org/10.1016/j.jss.2016.11.037
[3]: https://hadoop.apache.org/
[4]: https://blog.twitter.com/engineering/en_us/a/2013/announcing-parquet-10-columnar-storage-for-hadoop
