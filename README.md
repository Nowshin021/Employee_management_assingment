# PRT563 – Advanced Data Management
## Assignment 4: Graph Database Design & Implementation using Neo4j

### 📌 Project Overview
This repository contains the database migration, Cypher scripts, and datasets for **PRT563 (Advanced Data Management) Assignment 4**. 

The objective of this project is to migrate an existing relational database (**University HR & Academic Management System** originally implemented in SQLite) to a **Neo4j NoSQL Graph Database**. This graph-based architecture improves scalability, relationship traversal, and high-performance querying in a Big Data environment.

---

### 📂 Repository Structure

```text
├── csv_files/                 # Exported relational data (.csv) for all 18 tables
│   ├── AcademicStaff.csv
│   ├── Campus.csv
│   ├── CasualSessionalStaff.csv
│   ├── Department.csv
│   ├── Employee.csv
│   ├── EmployeePosition.csv
│   ├── EmployementContract.csv
│   ├── Faculty.csv
│   ├── Leave.csv
│   ├── PayRecord.csv
│   ├── PerformanceReview.csv
│   ├── Position.csv
│   ├── ProfessionalStaff.csv
│   ├── Qualification.csv
│   ├── Timesheet.csv
│   ├── Unit.csv
│   └── UnitOffering.csv
├── SQLite.db                  # Original SQLite relational database
├── load_csv.py                # Python automation script to export SQLite tables to CSV
├── import.txt                 # Cypher scripts for creating constraints, indexes, nodes, & relationships
├── queries.txt                # 4 Cypher business query use cases (Basic to Complex)
├── requirements.md            # Assignment specification and guidelines
└── README.md                  # Project documentation and instructions

