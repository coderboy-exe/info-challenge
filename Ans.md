## ANSWER 1

## Problems/Disadvantages in the Original List:

Redundancy: The original list has repeated information for the same article and provider.
Lack of Data Integrity: There's no clear relationship between different entities (e.g., articles, providers).
Inefficiency: Retrieving specific information may require scanning the entire list, which can be inefficient for large datasets.
Limited Scalability: The flat structure may not scale well with thousands of entries.


### Problems/Disadvantages in the Original List:

1. **Redundancy:**
   - *Issue:* The same information about articles and providers is repeated for each entry, leading to redundancy.
   - *Consequence:* This redundancy consumes more space and can lead to inconsistencies if there are updates or changes.

2. **Lack of Data Integrity:**
   - *Issue:* There is no clear relationship between different entities, making it difficult to enforce data integrity and consistency.
   - *Consequence:* Inconsistent or invalid data may be introduced, affecting the reliability and accuracy of the data.

3. **Inefficiency:**
   - *Issue:* Retrieving specific information may require scanning the entire list, leading to inefficiency, making it difficult to optimize queries.
   - *Consequence:* As the dataset grows, query performance will likely degrade.

4. **Limited Scalability:**
   - *Issue:* The flat structure is not suitable for scaling with a large number of entries.
   - *Consequence:* Managing and querying data becomes more challenging as the dataset expands, making the system impossible to perform optimally.


## ANSWER 3

#TODO



## ANSWER 3

### Advantages of the New Data Model:

1. **Normalization:**
   - *Advantage:* The data is organized into separate tables, and redundancy is minimized through normalization.
   - *Benefit:* This reduces storage space, ensures data consistency, and simplifies updates, leading to a more efficient use of resources.

2. **Clear Relationships:**
   - *Advantage:* Entities like "Article", "Provider" and Price are clearly defined with relationships in the new data model.
   - *Benefit:* This provides a structured and organized representation of the data, making it easier to understand and maintain.

3. **Scalability:**
   - *Advantage:* The new model is designed to be more scalable and efficient for handling a large number of entries.
   - *Benefit:* As the dataset grows, the database structure can handle the increased load more effectively, maintaining better performance.

In summary, the move to a normalized data model addresses the issues of redundancy, data integrity, and scalability, providing a more efficient and organized way to manage and query the data. It sets a foundation for a system that can handle growth and changes more effectively.


## ANSWER 4

- Simply run the contents of the file `sql/schema.sql` in order to build the schema and create the tables.
- Run the contents of the file `sql/query.sql` to run the query and return the original table.