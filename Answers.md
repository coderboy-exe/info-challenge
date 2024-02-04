## ANSWER 1

<!-- ## Problems/Disadvantages in the Original List:

Redundancy: The original list has repeated information for the same article and provider.
Lack of Data Integrity: There's no clear relationship between different entities (e.g., articles, providers).
Inefficiency: Retrieving specific information may require scanning the entire list, which can be inefficient for large datasets.
Limited Scalability: The flat structure may not scale well with thousands of entries. -->

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



## ANSWER 2
![PriceTracker drawio](https://github.com/coderboy-exe/info-strat/assets/71130767/3f22580f-0ef3-4994-8388-42514a24c468)





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

1. **Build the Schema:** Simply run the contents of the [sql/schema.sql](sql/schema.sql) file in order to build the schema and create the tables.

**Schema (MySQL v5.7)**

    CREATE TABLE Providers (
    	provider_no int NOT NULL PRIMARY KEY,
    	provider VARCHAR(50)
    );
    
    CREATE TABLE Articles (
    	article_no int NOT NULL PRIMARY KEY,
    	article VARCHAR(50)
    );
    
    CREATE TABLE Prices (
        price_id INT NOT NULL PRIMARY KEY,
        price INT,
        article_no INT,
        provider_no INT,
        FOREIGN KEY (article_no) REFERENCES Articles(article_no),
        FOREIGN KEY (provider_no) REFERENCES Providers(provider_no)
    );
    
    INSERT INTO Providers (provider_no, provider)
    VALUES
    (1, 'Flutterwave'),
    (2, 'Paystack'),
    (3, 'Stripe');
    
    INSERT INTO Articles (article_no, article)
    VALUES
    (101, 'US Dollar'),
    (102, 'EU Pounds'),
    (103, 'EU Euro'),
    (104, 'SWIZ Swiss');
    
    INSERT INTO Prices (price_id, price, article_no, provider_no)
    VALUES
    (1, 1000, 101, 1),
    (2, 1500, 101, 2),
    (3, 1200, 102, 1),
    (4, 2000, 104, 3),
    (5, 5000, 103, 2),
    (6, 1800, 101, 1),
    (7, 2100, 102, 3),
    (8, 500, 104, 2);
      
---

2. **Run the Query:** Run the contents of the file [sql/query.sql](sql/query.sql) to run the query and return the original table.

**Query #1**

    SELECT 
    Articles.article_no,
    Articles.article,
    LPAD(Providers.provider_no, 4, '0') AS provider_no,
    Providers.provider,
    Prices.price
    FROM Prices
    JOIN Articles ON Prices.article_no = Articles.article_no
    JOIN Providers ON Prices.provider_no = Providers.provider_no
    ORDER BY Articles.article_no;

| article_no | article    | provider_no | provider    | price |
| ---------- | ---------- | ----------- | ----------- | ----- |
| 101        | US Dollar  | 0001        | Flutterwave | 1000  |
| 101        | US Dollar  | 0001        | Flutterwave | 1800  |
| 101        | US Dollar  | 0002        | Paystack    | 1500  |
| 102        | EU Pounds  | 0001        | Flutterwave | 1200  |
| 102        | EU Pounds  | 0003        | Stripe      | 2100  |
| 103        | EU Euro    | 0002        | Paystack    | 5000  |
| 104        | SWIZ Swiss | 0002        | Paystack    | 500   |
| 104        | SWIZ Swiss | 0003        | Stripe      | 2000  |

---

[View on DB Fiddle](https://www.db-fiddle.com/f/7bmFueK5xmNaQKw6k2YB5j/2)
