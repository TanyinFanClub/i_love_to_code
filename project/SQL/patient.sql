drop table if exists patient;

CREATE TABLE patient(
	nric VARCHAR(9) NOT NULL, 
    name VARCHAR(50) NOT NULL,
    dob DATE NULL,
    gender VARCHAR(10) NULL,
    race VARCHAR(20) NULL,
    nationality VARCHAR(30) NULL,
    address VARCHAR(100) NULL,
    mobile_number VARCHAR(20) NULL,
    home_number VARCHAR(20) NULL,
    email varchar(50) NULL,
    next_of_kin VARCHAR(50) NULL,
    next_of_kin_contact VARCHAR(20) NULL,
    CONSTRAINT patient_pk PRIMARY KEY (nric)
);


INSERT INTO patient VALUES("S9476502D", "Apple Tham", "1994-02-12", "f", "chinese", "singaporean","50 Chai Chee Road #09-132", "98756325", "67849304", "apple.tham@gmail.com", "Pear Tham", "84958374");
INSERT INTO patient VALUES("S9873758E", "Ben Chan", "1998-05-19", "m", "chinese", "singaporean","42 Seng Kang Drive #08-211", "93949234", "61029403", "ben.chan@gmail.com", "Ken Chan", "93829403");
INSERT INTO patient VALUES("S9739405A", "Carrey Lim", "1997-08-11", "f", "chinese", "singaporean","12 Choa Chu Kang Cresent #02-12", "95739485", "69049382", "carrey@gmail.com", "Mango Lau", "87394039");
INSERT INTO patient VALUES("S9673847F", "Adam Lee", "1995-02-12", "m", "chinese", "singaporean","13 Rifle Range Road #04-32", "98738495", "67894051", "adam.lee@gmail.com", "Belinda Lee", "84593845");
INSERT INTO patient VALUES("S9349586G", "Dan Kim", "1993-12-12", "m", "chinese", "singaporean","41 Tanjong Pagar Road #25-323", "91839405", "60192849", "dan.k@gmail.com", "Kim Mun Hee", "84859402");
INSERT INTO patient VALUES("S7894834K", "Dean Chan", "1978-03-16", "m", "chinese", "singaporean","50 Orchard Road #09-132", "99584732", "68735263", "dean.c@gmail.com", "Paul Chan", "95049387");
INSERT INTO patient VALUES("S8493859L", "Elijah Lee", "1984-09-12", "f", "chinese", "singaporean","80 Rochor Street 42 #02-121", "97564839", "60987564", "lee.elijah@gmail.com", "Randy Tan", "88593748");
INSERT INTO patient VALUES("S8594837F", "Lindy Lo", "1985-03-16", "f", "chinese", "singaporean","96 Anderson Road #40-123", "98960954", "62940596", "lindy@gmail.com", "Lo Kua Quek", "98748576");
INSERT INTO patient VALUES("S7894856J", "Lester Goh", "1978-04-13", "m", "chinese", "singaporean","67 Yew Tee Avenue 12 #02-98", "98768948", "67859607", "lester.goh@gmail.com", "Kennie Kiao", "88960394");
INSERT INTO patient VALUES("S0195847J", "Lau Kim Geok", "1942-05-18", "f", "chinese", "singaporean","Bukit Timah Road #13-12", "99609854", "68756453", "kimgeok@gmail.com", "Lim Le Keng", "89765498");
INSERT INTO patient VALUES("S9295069L", "Siti Nur Salizah", "1992-05-19", "f", "malay", "singaporean","86 Sungei Kadut Drive #13-13", "98765043", "67869485", "siti.nur@gmail.com", "Shamalah", "88694758");
INSERT INTO patient VALUES("S9123456A", "Sumanthi Singh", "1991-01-14", "f", "indian", "singaporean","69 Bedok Reservoir #08-191", "98765986", "60987648", "sumanthi.singh@gmail.com", "Kumar", "80958473");
INSERT INTO patient VALUES("S9401234C", "Alice Chan", "1994-01-18", "f", "chinese", "singaporean","60 Airport Road #07-02", "97859403", "67930495", "alice.chan@gmail.com", "Mali Chan", "95038576");

#select * from patient