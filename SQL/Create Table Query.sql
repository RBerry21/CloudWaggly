  CREATE TABLE dbo.dogowners (
    dog_id UNIQUEIDENTIFIER PRIMARY KEY,
    customer_name NVARCHAR(200) NOT NULL,
	dog_name NVARCHAR(200) NOT NULL,
	customer_postcode NVARCHAR(200) NOT NULL,
	customer_number NVARCHAR(200) NOT NULL,
    customer_email NVARCHAR(200) NOT NULL,
    );

  CREATE TABLE dbo.dogwalkers (
    walker_id UNIQUEIDENTIFIER PRIMARY KEY,
    walker_name NVARCHAR(200) NOT NULL,
	walker_postcode NVARCHAR(200) NOT NULL,
	walker_number NVARCHAR(200) NOT NULL,
    walker_email NVARCHAR(200) NOT NULL
  );
