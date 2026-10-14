# PRT563 – Advanced Data Management
## Assignment 4: Graph Database Design & Implementation using Neo4j

### 📌 Project Overview
This repository contains the database migration, Cypher scripts, data assets, and report deliverables for **PRT563 (Advanced Data Management) Assignment 4**. 

The objective of this project is to migrate an existing relational database (**University HR & Academic Management System** originally designed and implemented in SQLite) to a **Neo4j NoSQL Graph Database**. This graph-based architecture eliminates complex multi-table joins, accelerates relationship traversal, and enhances analytical querying capabilities in a Big Data environment.

---

### 📂 Repository Structure

```text
Employee_management_assingment/
├── csv_files/                 # Exported relational datasets (.csv)
│   ├── AcademicStaff.csv
│   ├── Campus.csv
│   ├── CasualSessionalStaff.csv
│   ├── Department.csv
│   ├── Employee.csv
│   ├── EmployeePosition.csv
│   ├── EmploymentContract.csv
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
├── cypher_queries/            # Execution scripts for Neo4j AuraDB & Desktop
│   ├── import.txt             # Task 2: Schema constraints, indexes, nodes, and relationships
│   └── queries.txt            # Task 3: Four practical Cypher business use case queries
├── graphs/                    # Project visual artifacts and diagrams
│   └── workflow.png           # Project hierarchical workflow & methodology diagram
├── Report_development/        # Assignment report submissions
│   └── Advance_data_management_SYD_02_Project_Report.docx  # Final group project report
├── SQLite.db                  # Assessment 2 source relational database
├── load_csv.py                # Python automation script to export SQLite tables to CSV
├── requirements.md            # Assignment 4 official specifications and rubrics
└── README.md                  # Comprehensive repository documentation
```

---

### 🚀 Key Project Tasks & Deliverables

#### 1. Graph Data Modelling (Task 1)
* **Translation:** Translated the relational Extended Entity-Relationship (EER) model into a Property Graph Model.
* **Blueprint:** Mapped relational tables and foreign keys into Graph Nodes (`:Employee`, `:Department`, `:Campus`, `:Unit`, etc.) and labeled Relationships (`[:WORKS_IN]`, `:LOCATED_AT`, `[:HOLDS_POSITION]`, `[:TEACHES]`, `[:SUBMITTED]`).
* **Visual Blueprint:** Documented in `graphs/workflow.png` and embedded directly into the final report.

#### 2. Graph Database Implementation (Task 2)
* **CSV Pipeline:** Automated extraction of 16 relational tables via `load_csv.py`.
* **Cloud Ingestion:** Ingested into Neo4j AuraDB using cloud-compatible GitHub Raw URLs.
* **Integrity & Indexing:** Enforced 13 unique constraints on primary keys (`staffId`, `deptId`, `campusId`, `unitCode`, etc.) to guarantee zero duplicate nodes and high-speed lookups.
* **Script Location:** Documented in [`cypher_queries/import.txt`](./cypher_queries/import.txt).

#### 3. Graph Database Business Queries (Task 3)
Four practical business query scenarios demonstrating varying levels of complexity:
* **Use Case 1 :** Department Staff Directory & Campus Allocation.
* **Use Case 2 :** Casual Staff Workload & Payroll Analytics.
* **Use Case 3 :** Multi-Hop Unit Offering Delivery & Staff Allocation across campuses.
* **Use Case 4 :** Talent Evaluation, Leadership Appraisal Hierarchy, and Qualification Mapping.
* **Script Location:** Documented in [`cypher_queries/queries.txt`](./cypher_queries/queries.txt).

#### 4. Graph Data Science (GDS) Analytics (Tasks 4 & 5)
* **Centrality Algorithm (Task 4):** Evaluates organizational network prominence and department influence.
* **Similarity Algorithm (Task 5):** Evaluates academic specialization and unit delivery similarity.

---

### 🛠️ Execution Guide

#### 1. Data Ingestion (Task 2)
1. Open the **Query** tab in Neo4j Browser / AuraDB.
2. Run the Cypher scripts sequentially from [`cypher_queries/import.txt`](./cypher_queries/import.txt):
   - Step 1: Create Constraints & Indexes.
   - Step 2: Ingest Nodes.
   - Step 3: Connect Relationships.
3. Verify graph visualization:
   ```cypher
   CALL db.schema.visualization();
   ```

#### 2. Running Business Queries (Task 3)
1. Copy each query block from [`cypher_queries/queries.txt`](./cypher_queries/queries.txt).
2. Execute in Neo4j Browser to generate result tables and visual subgraphs.

---

### 👥 Submission Details
* **Unit:** PRT563 – Advanced Data Management
* **Institution:** Charles Darwin University (CDU)
* **Report Deliverable:** [`Report_development/Advance_data_management_SYD_02_Project_Report.docx`](./Report_development/Advance_data_management_SYD_02_Project_Report.docx)
