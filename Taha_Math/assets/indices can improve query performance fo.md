indices can improve query performance for sorting significantly (especially for huge data). It's not always like a magic. Here is how it can help:

* Pre-sorted structure: If you wanna search each page of a phonebook alphabetically, it would be slow. But if you use the index, it would list names and their relevant page numbers and this help you find what you want sooner. Similar to that, an index create a structure which is pre-sorted for one or more columns. 
And database will save time and hardware resources by using indexes for sorting instead of sorting entire table.

* Reduced I/O operations: Using indexes minimizes accessing disk, especially for large tables, and it will results to improving sorting speed.

* Efficient filtering: If your query also filters data based on the indexed column(s) before sorting, the index can further optimize by only returning relevant rows, reducing the amount of data to sort.

**Things to consider:**

- **Not all sorts benefit:** If your sort criteria involve multiple un-indexed columns or complex functions, indexing might not help much.
- **Trade-offs exist:** Creating and maintaining indexes takes resources and storage space. Frequent updates can make them less effective. Analyze the cost-benefit of indexing based on your specific data size, update frequency, and query patterns.
- **Types of indexes:** Clustered indexes physically order the table based on the key column, providing the fastest sorting but only allowing one per table. Non-clustered indexes offer more flexibility but don't physically rearrange data.

**Best practices:**

- **Index columns used in frequent WHERE and ORDER BY clauses.**
- **Consider selectivity: Index columns with distinct values for better filtering before sorting.**
- **Analyze query plans:** Tools like EXPLAIN in MySQL or db_explain in PostgreSQL can show how your queries utilize indexes and help identify optimization opportunities.

Remember, indexing is just one tool in the toolbox. For optimal performance, consider other factors like query structure, hardware, and database configuration.