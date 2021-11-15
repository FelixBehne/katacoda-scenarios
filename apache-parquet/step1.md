# Row oriented vs. columnar oriented file system 

Similar to databases, file formats can be distinguished by the way they store data internally.

A distinction is made between row- and column-oriented file formats, which offer different advantages for different application purpose.

Row-oriented file formats (e.g. Avro, CSV, TSV, JSON) store data row by row. 
They are best suited for OLTP applications due to the following advantages:
* Good Insert, update and delete operations performance
* Single values can be retrieved through efficient index and off-set
computations 

Column-oriented file formats (e.g. Parquet, OCR) store data column by column.
They are best suited for OLAP applications due to the following advantages:
* Data can be retrieved with far fewer read operations than for row-oriented storage

