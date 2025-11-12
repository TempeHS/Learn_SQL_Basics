## Guidelines

- Use British English
- Keep Jupyter Notebook and markdown documents syncronised
- Keep requirements.txt updated with any requirements
- Keep .devcontainer/ and .vscode/ updated with any required extensions

## Curriculum dot points

- Apply a web-based database and construct script that executes SQL
  - selecting fields
  - incorporating ‘group by’
  - common SQL queries
  - constraints using WHERE keyword
  - table joins
- interfacing with databases that are based on Structured Query language (SQL) or non-SQL
- Compare Object-Relational Mapping (ORM) to SQL

## Stack

- SQlite3
- SQLAlchemy (only used when teaching ORM)

## High School Student skills

- Intermediate Python

## Sqlite3 VSCode Plugin

- yy0931.vscode-sqlite3-editor

## Outline

SQL Basics Curriculum: Star Wars Database Edition
Course Overview
Duration: 10 lessons × 20 minutes each
Target Audience: High school students with intermediate Python skills
Theme: Star Wars Universe Database
Tools: SQLite3, VSCode SQLite3 plugin, Python sqlite3 module

Lesson 1: Introduction to Databases & SQLite Setup
Duration: 20 minutes

Learning Objectives
Understand what databases are and why we use them
Set up SQLite3 and VSCode plugin
Create your first database and table
Insert basic data

Activities
Concept Introduction (3 min)

- What is a database?
- Relational databases vs other types
- SQLite overview

Hands-on: Create Star Wars Database (10 min)

- Create database/starwars.db
- Create characters table (id, name, species, homeworld)
- Insert 5-8 characters (Luke, Leia, Han, Chewbacca, Obi-Wan, Vader, Yoda, R2-D2)

Practice Exercise (7 min)

- Students add 2-3 more characters of their choice

Deliverables

- lesson1_setup.sql - Table creation and initial inserts

Key SQL Concepts

- CREATE TABLE
- INSERT INTO
- Primary Keys
- Data types: INTEGER, TEXT

---

Lesson 2: Selecting and Filtering Data (SELECT & WHERE)
Duration: 20 minutes

Learning Objectives
Query data using SELECT
Filter results with WHERE clause
Use comparison operators and LIKE

Activities
SELECT Basics (8 min)

- Select all columns vs specific columns
- Selecting with WHERE conditions
- Using operators: =, !=, >, <, >=, <=

Pattern Matching (5 min)

- LIKE with wildcards (%, \_)
- Finding patterns in text

Hands-on Exercises (7 min)

- Find all human characters
- Find characters from Tatooine
- Find characters whose names start with specific letters
- Combine multiple conditions with AND/OR

Deliverables

- lesson2_queries.sql - 8-10 SELECT queries with WHERE clauses

Challenge Problem
Write a query to find all characters whose species contains "oid" and are from a homeworld starting with 'T'

---

Lesson 3: Sorting and Limiting Results
Duration: 20 minutes

Learning Objectives
Sort query results with ORDER BY
Limit results with LIMIT
Combine sorting and filtering

Activities
Sorting Data (8 min)

- ORDER BY ASC and DESC
- Sorting by multiple columns
- Sorting with WHERE

Limiting Results (5 min)

- LIMIT clause
- LIMIT with OFFSET (pagination concept)

Hands-on Exercises (7 min)

- Top 5 tallest characters
- Alphabetically sorted species
- Characters from specific homeworlds, sorted by name
- Create ranked lists

Deliverables

- lesson3_sorting.sql - Queries demonstrating ORDER BY and LIMIT

Challenge Problem
Create a query that shows the 3 shortest characters from each species

---

Lesson 4: Aggregate Functions and GROUP BY
Duration: 20 minutes

Learning Objectives
Use aggregate functions: COUNT, AVG, MAX, MIN
Group data with GROUP BY
Filter groups with HAVING

Activities
Aggregate Functions (8 min)

- Count total characters
- Average height
- Find tallest/shortest characters
- COUNT with DISTINCT

GROUP BY (7 min)

- Count characters by species
- Average height by homeworld
- Characters per affiliation
- HAVING clause for filtering groups

Quick Practice (5 min)

- Write queries using learned concepts

Deliverables

- lesson4_aggregates.sql - Queries with aggregates and grouping

Challenge Problem
Find which species has the tallest average height, but only include species with 2+ members

---

Lesson 5: Multiple Tables and Relationships
Duration: 20 minutes

Learning Objectives
Understand table relationships
Create related tables with foreign keys
Prepare for joins in next lesson

Activities
Database Design Concepts (5 min)

- One-to-many relationships
- Foreign keys
- Why normalize data

Create New Tables (10 min)

- planets table (id, name, climate, population)
- vehicles table (id, name, model, vehicle_class)
- character_vehicles table (character_id, vehicle_id)
- Update characters table to use foreign key for homeworld

Insert Related Data (5 min)

- Add 5-8 planets (Tatooine, Alderaan, Hoth, Naboo, etc.)
- Add 5-8 vehicles (X-wing, Millennium Falcon, TIE Fighter, etc.)
- Link 10+ character-vehicle relationships

Deliverables

- lesson5_schema.sql - Multi-table schema creation
- lesson5_data.sql - INSERT statements for all tables

---

Lesson 6: Table Joins
Duration: 20 minutes

Learning Objectives
Understand JOIN operations
Write INNER JOIN queries
Use LEFT JOIN
Combine joins with WHERE and GROUP BY

Activities
JOIN Concepts (5 min)

- Why we need joins
- INNER vs LEFT JOIN visual explanation

INNER JOIN (8 min)

- Characters with their homeworld details
- Characters with their vehicles
- Multiple joins in one query

LEFT JOIN (7 min)

- Find characters without vehicles
- Find vehicles without pilots
- Understanding NULL values in joins

Deliverables

- lesson6_joins.sql - 10+ queries demonstrating different joins

Challenge Problem
Create a query that shows each planet with character count, including planets with no characters

---

Lesson 7: Updating and Deleting Data
Duration: 20 minutes

Learning Objectives
Update existing records
Delete records safely
Understand importance of WHERE clause

Activities
UPDATE Operations (8 min)

- Update single records
- Update multiple records with WHERE
- The danger of UPDATE without WHERE!
- Update using calculations

DELETE Operations (7 min)

- Delete specific records
- Delete with WHERE (demonstrate danger without it!)
- Cascading deletes concept

Constraints Overview (5 min)

- PRIMARY KEY review
- FOREIGN KEY review
- NOT NULL
- UNIQUE
- CHECK constraints (brief)

Deliverables

- lesson7_modifications.sql - UPDATE and DELETE operations

Challenge Problem
Write a series of UPDATE statements that change character affiliations based on specific conditions

---

Lesson 8: Advanced Queries with Subqueries
Duration: 20 minutes

Learning Objectives
Write subqueries
Use IN, NOT IN, EXISTS
Combine multiple concepts

Activities
Subqueries (10 min)

- Subqueries in WHERE clause
- Subqueries in SELECT clause
- IN and NOT IN with subqueries

EXISTS Operator (7 min)

- EXISTS and NOT EXISTS
- When to use vs JOIN

Complex Practice (3 min)

- Find characters who pilot the same vehicle class as Luke
- Find planets with above-average character count

Deliverables

- lesson8_advanced.sql - Complex queries with subqueries

Challenge Problem
Write a query using only subqueries (no joins) that finds all characters from the same planet as someone who pilots a starfighter

---

Lesson 9: Python Database Integration
Duration: 20 minutes

Learning Objectives
Connect to SQLite from Python
Execute queries programmatically
Use parameterized queries

Activities
Python sqlite3 Module (8 min)

- Connecting to database
- Creating cursors
- Executing queries
- Fetching results (fetchone, fetchall)

Parameterized Queries (8 min)

- SQL injection demonstration
- Using ? placeholders
- Safe query practices

Simple Application (4 min)

- Create functions to query database
- Display results formatted

Deliverables

- lesson9_database.py - Script with database functions and examples

---

Lesson 10: ORM & Non-SQL Overview
Duration: 20 minutes

Learning Objectives
Understand what ORM is and why it's used
Compare SQL to ORM approach
Overview of non-SQL databases
When to use each approach

Activities
ORM Concepts (10 min)

- What is Object-Relational Mapping?
- Advantages and disadvantages
- SQLAlchemy quick introduction
- Side-by-side comparison: Same query in SQL vs SQLAlchemy

Non-SQL Databases Overview (8 min)

- Document databases (MongoDB)
- Key-value stores (Redis)
- Graph databases (Neo4j)
- When to use non-SQL
- Star Wars data in document format example

Discussion (2 min)

- When would you choose SQL over NoSQL?
- What are the trade-offs of using ORM?

Deliverables

- lesson10_comparison.md - Document comparing SQL, ORM, and NoSQL

---

Assessment & Final Project Ideas

Ongoing Assessment

- Code reviews of SQL files
- Query correctness and efficiency
- Challenge problem solutions

Final Project Options (Optional - 1-2 hours)

1. Star Wars Encyclopedia CLI
   - Full CRUD application
   - Advanced search features
2. Database Design Challenge

   - Design additional tables (missions, battles, droids)
   - Implement with constraints
   - Create comprehensive queries

3. Performance Comparison
   - Compare identical operations in SQL vs ORM
   - Written analysis report

Resources for Students

- SQL command cheat sheet
- Python sqlite3 examples
- SQLBolt - Interactive tutorials
- LeetCode SQL problems
- Star Wars API for additional data

Notes for Instructor

- Each lesson builds on previous database state
- Keep database small and manageable (~40-50 records max)
- Emphasize SQL syntax as primary exam focus
- Use VSCode SQLite3 plugin for visual feedback
- Encourage experimentation
- Focus is on practical SQL skills, not complex database theory
