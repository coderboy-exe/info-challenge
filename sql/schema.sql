
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