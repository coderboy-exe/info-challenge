SELECT 
Articles.article_no,
Articles.article,
LPAD(Providers.provider_no, 4, '0') AS provider_no,
Providers.provider,
Prices.price
FROM Prices
JOIN Articles ON Prices.article_no = Articles.article_no
JOIN Providers ON Prices.provider_no = Providers.provider_no
ORDER BY Articles.article_no