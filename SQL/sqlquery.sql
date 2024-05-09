-- Drop and then create 'dogowners' table if it doesn't already exist

DROP TABLE IF EXISTS dbo.dogowners;

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES 
  WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = 'dogowners')
BEGIN
  CREATE TABLE dbo.dogowners (
    dog_id UNIQUEIDENTIFIER PRIMARY KEY,
    customer_name NVARCHAR(200) NOT NULL,
	dog_name NVARCHAR(200) NOT NULL,
	customer_postcode NVARCHAR(200) NOT NULL,
	customer_number NVARCHAR(200) NOT NULL,
    owner_email NVARCHAR(200) NOT NULL,
    );
END;

-- Drop and recreate 'walkers' table if it doesn't already exist

DROP TABLE IF EXISTS dbo.dogwalkers;

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES 
  WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = 'dogwalkers')
BEGIN
  CREATE TABLE dbo.dogwalkers (
    walker_id UNIQUEIDENTIFIER PRIMARY KEY,
    walker_name NVARCHAR(200) NOT NULL,
	walker_postcode NVARCHAR(200) NOT NULL,
	walker_number NVARCHAR(200) NOT NULL,
    walker_email NVARCHAR(200) NOT NULL
  );
END;
