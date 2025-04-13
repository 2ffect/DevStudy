-- Active: 1744077438218@@127.0.0.1@3306
# 1.
SELECT InvoiceId, InvoiceDate FROM invoices;

# 2.
SELECT * FROM invoices WHERE BillingCountry = 'USA' AND "Total" >= 10;

# 3.
SELECT * FROM invoices WHERE BillingCity IN ('London', 'Berlin');

# 4.
SELECT * FROM invoices ORDER BY Total DESC LIMIT 1;

# 5.
SELECT * FROM invoices WHERE InvoiceDate > '2013-04-01' AND Total > 3;

# 6.
SELECT * FROM invoices WHERE BillingCountry = 'USA' AND BillingSTate = 'CA' AND Total > 10;

# 7.
SELECT * FROM invoices WHERE BillingCountry = 'Canada' AND BillingSTate = 'ON' AND BillingCity = 'Toronto';

# 8.
SELECT * FROM invoices WHERE InvoiceDate < '2023-01-01' AND Total >= 50 OR BillingCountry = 'Brazil';