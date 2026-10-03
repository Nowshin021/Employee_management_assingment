PRT563- Advanced Data Management

Assignment 4: Group Project Report (40%)

Deliverables: Group Report

Due Date: 16th October 2026 on Friday by 04:59 PM

About

This assessment must be completed within your existing group. Individual work submissions will not be accepted.

Continuing your previous group assessment, you will design and implement a graph database using Neo4j.

Tasks

As your selected company grows, you are asked to consider migrating its current relational database (which you previously designed and implemented in Assessment 2) to a NoSQL database that provides better scalability for a Big Data environment. Specifically, the company has nominated Neo4j as the new database management platform.

Any change or improvement to your existing relational database designs is permitted but must be justified in the final report.

1\. Graph database modelling

Translate the existing EER model into a graph model. Using any software, draw a diagram that shows your Neo4j data model (i.e. the basic structure of your graph). An example is shown below; do not submit your entire graph.

neo4j data model example.png

Source: https://neo4j.com/developer-blog/building-educational-platform-neo4j/

2\. Graph database implementation

Based on the translated graph model above, write Cypher scripts to migrate the relational database into the new Neo4j database fully. These should include Cypher scripts for:

Importing relational data from .csv files into Neo4j database (including scripts for creating nodes and relationships).

Creating index.

3\. Graph database queries

Provide four Cypher query use cases. Each use case must include the description of the query's practical scenario, along with their corresponding Cypher query statements and results. Your queries should demonstrate varying levels of complexity.

4\. Centrality algorithms

Develop and demonstrate one analytics use case using Neo4j's Graph Data Science Library (GDSL) centrality algorithms. Experiment with a wide range of centrality algorithms available from Neo4j's Graph Data Science Library: https://neo4j.com/docs/graph-data-science/current/algorithms/

5\. Similarity algorithms

Develop and demonstrate one analytics use case using Neo4j's Graph Data Science Library (GDSL) similarity algorithms. Experiment with a wide range of similarity algorithms available from Neo4j's Graph Data Science Library: https://neo4j.com/docs/graph-data-science/current/algorithms/

Grading

Please see the grading rubric for detailed marking criteria. Your instructor reserves the right to further differentiate individual grades where necessary.

Submissions

Submit your work no later than the stated due date of this assignment to avoid late submission penalties. Please submit:

One group report per team. The report must be in a Microsoft Word file (.docx) and not exceed 6,000 words (A4, single-spaced, single-column, 11pt font), excluding the title page, table of contents, list of figures, and list of references. There is no minimum length to the report. Do not submit multiple documents.

The report needs to have the following basic structure:

Title page, table of contents, and list of figures

Introduction

(followed by appropriate sections corresponding to each completed task)

...

Discussions and limitations

Conclusion

List of references (if applicable)

Brief descriptions of individual contributions (max. half a page to describe each person's contribution)

In the comment section of your submission, please include 1 URL to a OneDrive / GitHub repository that contains:

The Cypher scripts that address Task 2 Graph database implementation. These scripts should be saved into a plain text file named import.txt

All .csv files required for constructing the graph database in Task 2 Graph database implementation.

All Cypher query scripts that address Task 3 Graph database queries. These scripts should be saved into a plain text file named queries.txt

The report will be checked for plagiarism through SafeAssign. Email submissions will not be accepted.

You may submit any supplementary items to further address the marking rubrics requirement.

Academic integrity and assessment irregularities

Academic integrity is a core value at CDU and must be upheld at all times when completing this assignment. You must not plagiarise the work of others. Please refer to the Students - Breach of Academic Integrity Procedures.

Other assessment irregularities are governed by CDU's Higher Education Assessment Procedures.