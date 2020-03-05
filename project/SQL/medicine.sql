create schema IF NOT EXISTS ESD_Project;
use ESD_Project;

drop table if exists prescription;

CREATE TABLE IF NOT EXISTS Prescription(
	QueueID VARCHAR(10) NOT NULL, 
    	Registration_timestamp date NOT NULL,
    	NRIC VARCHAR(9) NOT NULL,
    	Medication_ID VARCHAR(10) NOT NULL,
    	CONSTRAINT prescription_pk PRIMARY KEY (QueueID,Registration_timestamp,Medication_ID),
	CONSTRAINT prescription_fk1 foreign key(QueueID) references diagnosis(QueueID),
	CONSTRAINT prescription_fk2 foreign key(Registration_timestamp) references diagnosis(Registration_timestamp),
	CONSTRAINT prescription_fk3 foreign key(NRIC) references patient(NRIC),
	CONSTRAINT prescription_fk4 foreign key(Medication_ID) references medication(Medication_ID)
);

drop table if exists Medication;

CREATE TABLE IF NOT EXISTS Medication(
	Medication_ID VARCHAR(10) NOT NULL, 
    	Medicine_name VARCHAR(100) NOT NULL,
    	Quantity INT NOT NULL,
    	Description VARCHAR(100) NOT NULL,
    	CONSTRAINT medication_pk PRIMARY KEY (medicine_id)
);

INSERT INTO Prescription VALUES
('4907', '2020-03-01 12:15:00', 'S6964907Z', 111),
('4907', '2020-03-01 12:15:00', 'S6964907Z', 110),
('4908', '2020-03-01 12:30:00', 'S6964908Z', 559);

INSERT INTO Medication VALUES
('111','Acetaminophen',10,'Acetaminophen is a pain reliever and a fever reducer.'),
('110','Citalopram',15,'Citalopram is used to treat depression.'),
('559','Corticosteroids',8,'Decreasing inflammation and reducing the activity of the immune system'),
('999','Antidepressants',0,'Good at treating sleeplessness and anxiety.'),
('007','James Bond',7,'No Time to Die')


