create schema IF NOT EXISTS ESD_Project;
use ESD_Project;

drop table if exists ward;

CREATE TABLE IF NOT EXISTS Ward(
	NRIC VARCHAR(9) NOT NULL,
    name VARCHAR(50) NOT NULL,
    Diagnosis VARCHAR(100) NOT NULL,
    Risks VARCHAR(100) NOT NULL,
    Dietary_Requirements VARCHAR(100) NOT NULL,
    -- Remarks VARCHAR(100) NOT NULL, 
    Timestamp date NOT NULL,
    CONSTRAINT ward_pk PRIMARY KEY (NRIC)
);


INSERT INTO Ward VALUES
('S1778303C', 'Alima Tillman', 'Hand, foot and mouth disease', 'NA', 'Regular Diet', '2020-02-15 16:40:00'),
('S7442555J', 'Freya Moss', 'Chickenpox', 'NA', 'Clear Liquid Diet', '2020-02-29 14:15:00'),
('S3413264Z', 'Kellie Moran', 'Measles', 'NA', 'Mechanical Soft Diet', '2020-03-01 12:15:00'),
('S8354591G', 'Zaynah Oconnor', 'Ringworm', 'NA', 'Regular Diet', '2020-03-02 12:45:00'),
('S9314907F', 'Calista Delaney', 'Hand, foot and mouth disease', 'NA', 'GI Soft Diet', '2020-03-03 18:15:00'),
('S6232771E', 'Boris James', 'Conjunctivitis', 'Fall Risk', 'Low Fiber Diet', '2020-03-03 22:15:00'),
('S5182858E', 'Carlton Hills', 'Whooping cough', 'Fall Risk', 'Fat-Restricted Diet', '2020-03-03 23:50:00'),
('S4355110H', 'Fred Mahoney', 'Streptococcal sore throat', 'Fall Risk', 'Salt-restricted Diet', '2020-03-06 09:15:00'),
('S0571147I', 'Brandy Holt', 'Mumps', 'NA', 'Regular Diet', 'Fat-Restricted Diet', '2020-03-08 15:59:00');


