


USE attendance_db;
CREATE TABLE student (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    class_roll_no VARCHAR(20),
    university_roll_no VARCHAR(20),
    dob VARCHAR(20),
    gender VARCHAR(10),
    phone VARCHAR(15),
    email VARCHAR(100),
    course VARCHAR(50),
    department VARCHAR(50),
    section VARCHAR(10),
    batch VARCHAR(20),
    year VARCHAR(10),
    semester VARCHAR(20)
);

CREATE TABLE teacher (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    phone VARCHAR(15),
    email VARCHAR(100),
    department VARCHAR(50),
    subject VARCHAR(50)
);

CREATE TABLE admin (
    admin_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50),
    password VARCHAR(50)
);
INSERT INTO admin (username, password)
VALUES ('admin', 'admin123');

