According to a study conducted by [Frost & Sullivan (2020)][1], Big Data analytics market revenue is forecasted to grow with a compound annual growth rate of almost 30%. 
This is accompanied by the demand for efficient storage and processing solutions that can meet the requirements of analytical processing applications (OLAP). 

One of the most widely used platforms for this purpose is Apache Hadoop [(Mavridis and Karatza, 2017)][2]. Hadoop is a set of software utilities that facilitates distributed storage and data processing based on the MapReduce processing model [(Fundation, n.d.)][3]. 

Within the hadoop ecosystem data can be stored in a variety of formats, all of which have different advantages. One of the most famous formats is Apache Parquet.

Apache Parquet is an open-source, general-purpose, columnar file format. It was initially released in July 2013 as a joint effort by Twitter and Cloudera. The official announcement can be found [here][4].

<p float="left" style="text-align: center; font-size: 6.8px; line-height:30px">
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/38/Hadoop_logo_new.svg" width=49% />
  <img src="https://upload.wikimedia.org/wikipedia/commons/4/47/Apache_Parquet_logo.svg" width=49%/> 
  Sources: https://upload.wikimedia.org/wikipedia/commons/3/38/Hadoop_logo_new.svg, https://upload.wikimedia.org/wikipedia/commons/4/47/Apache_Parquet_logo.svg
</p>

Due to it's columnar-oriented design, it comes with many performance advantages over row-oriented file formats. <br>

In this scenario you will learn how to work with parquet in python, how parquet performs when dealing with millions of rows and how it compares to row-oriented file formats like Avro.<br>

**Let's get started 🚀**


[1]: https://www.statista.com/statistics/947745/worldwide-total-data-market-revenue/
[2]: https://doi.org/10.1016/j.jss.2016.11.037
[3]: https://hadoop.apache.org/
[4]: https://blog.twitter.com/engineering/en_us/a/2013/announcing-parquet-10-columnar-storage-for-hadoop
