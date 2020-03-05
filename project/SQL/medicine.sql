create schema IF NOT EXISTS ESD_Project;
use ESD_Project;

drop table if exists prescription;

CREATE TABLE IF NOT EXISTS prescription(
	queueid VARCHAR(10) NOT NULL, 
    	registration_timestamp date NOT NULL,
    	nric VARCHAR(9) NOT NULL,
    	medication_list VARCHAR(100) NULL,
    	CONSTRAINT prescription_pk PRIMARY KEY (queueid,registration_timestamp),
		CONSTRAINT prescription_fk1 foreign key(queueid) references diagnosis(queueid),
		CONSTRAINT prescription_fk2 foreign key(registration_timestamp) references diagnosis(registration_timestamp),
		CONSTRAINT prescription_fk3 foreign key(nric) references patient(nric)
);

drop table if exists medication;

CREATE TABLE IF NOT EXISTS medication(
	medicine_id VARCHAR(10) NOT NULL, 
    	medicine_name VARCHAR(100) NOT NULL,
    	quantity INT NOT NULL,
    	description VARCHAR(100) NOT NULL,
    	CONSTRAINT medication_pk PRIMARY KEY (medicine_id)
);

INSERT INTO prescription VALUES
('4907', '2020-03-01 12:15:00', 'S6964907Z', ?),
('4908', '2020-03-01 12:30:00', 'S6964908Z', ?);

INSERT INTO medication VALUES
('111','Acetaminophen',10,'Acetaminophen is a pain reliever and a fever reducer.'),
('110','Citalopram',15,'Citalopram is used to treat depression.'),
('559','Corticosteroids',8,'Decreasing inflammation and reducing the activity of the immune system'),
('999','Antidepressants',0,'Good at treating sleeplessness and anxiety.'),
('007','James Bond',7,'No Time to Die')


