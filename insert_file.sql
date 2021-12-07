INSERT INTO Patient(id,email,password,name,address,gender)
VALUES
(101,'pa1@gmail.com','pa1','Patient1','Andhra Pradesh', 'Female'),
(102,'pa2@gmail.com','pa2','Patient2','ghsd','male'),
(103,'pa3@gmail.com','pa3','patient3','sdjfb','male'),
(104,'pa4@gmail.com','pa4','patient4','sdf','female'),
(105,'pa5@gmail.com','pa5','patient5','dfg','male'),
(106,'pa6@gmail.com','pa6','patient6','ddfs','female')
;

INSERT INTO MedicalHistory(id,date,conditions,surgeries,medication)
VALUES
(1,'19-01-21','Accident','Heart surgery','Clopidogrel'),
(2,'22-05-21','Frequent indigestion','none','none'),
(3,'16-11-21','High fever','none','Paracetamol'),
(4,'20-09-21','Covid 19','none','Remdisivir'),
(5,'09-12-21','Kidney failure','none','Dialysis'),
(6,'19-01-21','Cancer','none','Chemotherapy')
;

INSERT INTO Doctor(id,email, gender, password, name)
VALUES
(1,'doc1@gmail.com', 'female', 'doc1', 'Doctor1'),
(2,'doc2@gmail.com', 'male', 'doc2', 'Doctor2'),
(3,'doc3@gmail.com', 'male', 'doc3', 'Doctor3'),
(4,'doc4@gmail.com', 'female', 'doc4', 'Doctor4'),
(5,'doc5@gmail.com', 'male', 'doc5', 'Doctor5'),
(6,'doc6@gmail.com', 'female', 'doc6', 'Doctor6')
;

INSERT INTO Appointment(id,date,starttime,endtime,status)
VALUES
(1, '19-01-21', '09:00', '10:00', 'Done'),
(2, '22-05-21', '10:00', '11:00', 'Done'),
(3, '16-11-21', '14:00', '15:00', 'Done'),
(4, '20-09-21', '22:00', '23:30', 'Cancelled'),
(5, '09-12-21', '10:00', '11:00', 'Ongoing'),
(6, '19-01-21', '18:00', '18:30', 'Ongoing')
;

INSERT INTO PatientsAttendAppointments(patient,appt,concerns,symptoms)
VALUES
(101,1, 'none', 'itchy throat'),
(102,2, 'infection', 'fever'),
(103,3, 'nausea', 'fever'),
(104,4, 'none', 'itchy throat'),
(105,5, 'infection', 'fever'),
(106,6, 'nausea', 'fever')
;

INSERT INTO Schedule(id,starttime,endtime,breaktime,day)
VALUES
(001,'09:00','17:00','12:00','Tuesday'),
(002,'10:00','18:00','12:00','Friday'),
(003,'17:00','23:00','20:00','Saturday'),
(004,'09:00','12:00','10:30','Sunday'),
(005,'09:00','17:00','12:00','Wednesday'),
(006,'17:00','23:00','20:00','Friday')
;

INSERT INTO PatientsFillHistory(patient,history)
VALUES
(101, 1),
(102, 2),
(103, 3),
(104, 4),
(105, 5),
(106,6)
;

INSERT INTO Diagnose(appt,doctor,diagnosis,prescription)
VALUES
(1, 5, 'Bloating', 'Ibuprofen as needed'),
(2, 2, 'Muscle soreness', 'Stretch morning/night'),
(3, 6, 'Vitamin Deficiency', 'Good Diet'),
(4, 1, 'Bloating', 'Ibuprofen as needed'),
(5, 6, 'Muscle soreness', 'Stretch morning/night'),
(6, 4, 'Vitamin Deficiency', 'Good Diet')
;

INSERT INTO DocsHaveSchedules(sched,doctor)
VALUES
(006, 1),
(002, 2),
(002, 3),
(003, 4),
(004, 5),
(005, 6)
;

INSERT INTO DoctorViewsHistory(history,doctor)
VALUES
(1, 5),
(2, 2),
(3, 6),
(4, 1),
(5, 6),
(6, 4)
;