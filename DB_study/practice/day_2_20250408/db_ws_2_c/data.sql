-- Active: 1744077438218@@127.0.0.1@3306
# 1.
SELECT BillingCountry, SUM(Total) AS TotalSales FROM invoices GROUP BY BillingCountry;

# 2.
SELECT strftime('%Y', InvoiceDate) AS Year, SUM(Total) AS TotalSales FROM invoices GROUP BY strftime('%Y', InvoiceDate);

# 3.
SELECT BillingState, SUM(Total) AS TotalSales FROM invoices WHERE BillingCountry = 'USA' AND InvoiceDate > '2010-01-02' GROUP BY BillingState;

# 4.
SELECT BillingCountry, MAX(Total) AS MaxOrderAmount FROM invoices WHERE BillingCountry IN ('Germany', 'France') GROUP BY BillingCountry;

