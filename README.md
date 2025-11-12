# Learn SQL Basics - Star Wars Database Edition 🚀

Welcome to the SQL Basics course! This hands-on curriculum will teach you essential SQL skills using a Star Wars-themed database. By the end of this course, you'll be able to create, query, and manage relational databases with confidence.

## 📚 Quick Access: All Lessons

| Lesson | Topic                                         | Jupyter Notebook                                                    | Markdown                                                 | PDF                                             | Solutions                                                                                          |
| ------ | --------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **1**  | Introduction to Databases & SQLite Setup      | [📓 Notebook](jupyter_notebook_lessons/lesson1_setup.ipynb)         | [📝 Markdown](markdown_lessons/lesson1_instructions.md)  | [📄 PDF](pdf_lessons/lesson1_instructions.pdf)  | [📓 ipynb](solutions/lesson1_setup.ipynb)<br>[📝 sql](solutions/lesson1_setup.sql)                 |
| **2**  | Selecting and Filtering Data (SELECT & WHERE) | [📓 Notebook](jupyter_notebook_lessons/lesson2_queries.ipynb)       | [📝 Markdown](markdown_lessons/lesson2_instructions.md)  | [📄 PDF](pdf_lessons/lesson2_instructions.pdf)  | [📓 ipynb](solutions/lesson2_queries.ipynb)<br>[📝 sql](solutions/lesson2_queries.sql)             |
| **3**  | Sorting and Limiting Results                  | [📓 Notebook](jupyter_notebook_lessons/lesson3_sorting.ipynb)       | [📝 Markdown](markdown_lessons/lesson3_instructions.md)  | [📄 PDF](pdf_lessons/lesson3_instructions.pdf)  | [📓 ipynb](solutions/lesson3_sorting.ipynb)<br>[📝 sql](solutions/lesson3_sorting.sql)             |
| **4**  | Aggregate Functions and GROUP BY              | [📓 Notebook](jupyter_notebook_lessons/lesson4_aggregates.ipynb)    | [📝 Markdown](markdown_lessons/lesson4_instructions.md)  | [📄 PDF](pdf_lessons/lesson4_instructions.pdf)  | [📓 ipynb](solutions/lesson4_aggregates.ipynb)<br>[📝 sql](solutions/lesson4_aggregates.sql)       |
| **5**  | Multiple Tables and Relationships             | [📓 Notebook](jupyter_notebook_lessons/lesson5_schema.ipynb)        | [📝 Markdown](markdown_lessons/lesson5_instructions.md)  | [📄 PDF](pdf_lessons/lesson5_instructions.pdf)  | [📓 ipynb](solutions/lesson5_schema.ipynb)<br>[📝 sql](solutions/lesson5_schema.sql)               |
| **6**  | Table Joins                                   | [📓 Notebook](jupyter_notebook_lessons/lesson6_joins.ipynb)         | [📝 Markdown](markdown_lessons/lesson6_instructions.md)  | [📄 PDF](pdf_lessons/lesson6_instructions.pdf)  | [📓 ipynb](solutions/lesson6_joins.ipynb)<br>[📝 sql](solutions/lesson6_joins.sql)                 |
| **7**  | Updating and Deleting Data                    | [📓 Notebook](jupyter_notebook_lessons/lesson7_modifications.ipynb) | [📝 Markdown](markdown_lessons/lesson7_instructions.md)  | [📄 PDF](pdf_lessons/lesson7_instructions.pdf)  | [📓 ipynb](solutions/lesson7_modifications.ipynb)<br>[📝 sql](solutions/lesson7_modifications.sql) |
| **8**  | Advanced Queries with Subqueries              | [📓 Notebook](jupyter_notebook_lessons/lesson8_advanced.ipynb)      | [📝 Markdown](markdown_lessons/lesson8_instructions.md)  | [📄 PDF](pdf_lessons/lesson8_instructions.pdf)  | [📓 ipynb](solutions/lesson8_advanced.ipynb)<br>[📝 sql](solutions/lesson8_advanced.sql)           |
| **9**  | Python Database Integration                   | [📓 Notebook](jupyter_notebook_lessons/lesson9_database.ipynb)      | [📝 Markdown](markdown_lessons/lesson9_instructions.md)  | [📄 PDF](pdf_lessons/lesson9_instructions.pdf)  | [📓 ipynb](solutions/lesson9_database.ipynb)<br>[🐍 py](solutions/lesson9_database.py)             |
| **10** | ORM & Non-SQL Overview                        | [📓 Notebook](jupyter_notebook_lessons/lesson10_comparison.ipynb)   | [📝 Markdown](markdown_lessons/lesson10_instructions.md) | [📄 PDF](pdf_lessons/lesson10_instructions.pdf) | [📓 ipynb](solutions/lesson10_comparison.ipynb)<br>[📝 md](solutions/lesson10_comparison.md)       |

**Choose Your Format:**

- 📓 **Jupyter Notebooks** - Interactive, run code directly (Recommended)
- 📝 **Markdown** - Easy to read, copy code to separate files
- 📄 **PDF** - Print-friendly, perfect for offline study

## 📖 Lesson Structure

Each lesson follows this format:

- **Learning Objectives** - What you'll master
- **Activities** - Step-by-step exercises
- **Deliverables** - Files you'll create
- **Challenge Problem** - Test your skills

### Lesson Breakdown

#### **Lesson 1: Introduction to Databases & SQLite Setup**

_Duration: 20 minutes_

Create your first database and insert Star Wars characters.

**Key Concepts:** CREATE TABLE, INSERT INTO, Primary Keys  
**Activities:**

- Database concepts (3 min)
- Create `starwars.db` in the `database` folder and `characters` table (10 min)
- Insert 5-8 characters (7 min)

**Deliverables:** `lesson1_setup.sql`

---

#### **Lesson 2: Selecting and Filtering Data (SELECT & WHERE)**

_Duration: 20 minutes_

Query data and filter results with conditions.

**Key Concepts:** SELECT, WHERE, Comparison Operators, LIKE  
**Activities:**

- SELECT basics and WHERE clause (8 min)
- Comparison operators (=, !=, >, <) (5 min)
- Pattern matching with LIKE (7 min)

**Deliverables:** `lesson2_queries.sql`

---

#### **Lesson 3: Sorting and Limiting Results**

_Duration: 20 minutes_

Control query output with sorting and limits.

**Key Concepts:** ORDER BY, LIMIT, OFFSET  
**Activities:**

- ORDER BY ASC/DESC (8 min)
- LIMIT and pagination (5 min)
- Combined queries (7 min)

**Deliverables:** `lesson3_sorting.sql`

---

#### **Lesson 4: Aggregate Functions and GROUP BY**

_Duration: 20 minutes_

Perform calculations on grouped data.

**Key Concepts:** COUNT, AVG, MAX, MIN, GROUP BY, HAVING  
**Activities:**

- Aggregate functions (8 min)
- GROUP BY clause (7 min)
- HAVING for filtering groups (5 min)

**Deliverables:** `lesson4_aggregates.sql`

---

#### **Lesson 5: Multiple Tables and Relationships**

_Duration: 20 minutes_

Design a multi-table database with foreign keys.

**Key Concepts:** Foreign Keys, One-to-Many Relationships  
**Activities:**

- Relationship concepts (5 min)
- Create `planets` and `vehicles` tables (10 min)
- Insert related data (5 min)

**Deliverables:** `lesson5_schema.sql`, `lesson5_data.sql`

---

#### **Lesson 6: Table Joins**

_Duration: 20 minutes_

Combine data from multiple tables using joins.

**Key Concepts:** INNER JOIN, LEFT JOIN  
**Activities:**

- JOIN concepts and syntax (5 min)
- INNER JOIN practice (8 min)
- LEFT JOIN and NULL handling (7 min)

**Deliverables:** `lesson6_joins.sql`

---

#### **Lesson 7: Updating and Deleting Data**

_Duration: 20 minutes_

Modify and remove data safely.

**Key Concepts:** UPDATE, DELETE, WHERE (critical!)  
**Activities:**

- UPDATE operations (8 min)
- DELETE operations (7 min)
- Safety practices and constraints (5 min)

**Deliverables:** `lesson7_modifications.sql`

---

#### **Lesson 8: Advanced Queries with Subqueries**

_Duration: 20 minutes_

Write complex nested queries.

**Key Concepts:** Subqueries, IN, NOT IN, EXISTS  
**Activities:**

- Subqueries in WHERE (10 min)
- IN and EXISTS operators (7 min)
- Practice complex queries (3 min)

**Deliverables:** `lesson8_advanced.sql`

---

#### **Lesson 9: Python Database Integration**

_Duration: 20 minutes_

Connect to SQLite from Python and execute queries.

**Key Concepts:** Python sqlite3 module, Parameterized queries  
**Activities:**

- Connection and cursor basics (8 min)
- Execute queries and fetch results (8 min)
- Parameterized queries (SQL injection prevention) (4 min)

**Deliverables:** `lesson9_database.py`

---

#### **Lesson 10: ORM & Non-SQL Overview**

_Duration: 20 minutes_

Compare SQL, ORM, and NoSQL approaches.

**Key Concepts:** SQLAlchemy basics, NoSQL concepts  
**Activities:**

- ORM introduction and comparison (10 min)
- NoSQL database types (8 min)
- When to use each approach (2 min)

**Deliverables:** `lesson10_comparison.md`

---

## 📂 Project Structure

```
Learn_SQL_Basics/
├── README.md                    # This file
├── QUICKSTART_PDF.md            # Quick guide for PDF conversion
├── notes.md                     # Curriculum planning notes
├── TEACHING_NOTES.md            # Instructor guidance
├── requirements.txt             # Python dependencies
│
├── database/
│   └── starwars.db              # Your database (created in Lesson 1)
│
├── jupyter_notebook_lessons/    # 📓 Interactive Jupyter Notebooks
│   └── lesson*.ipynb
│
├── markdown_lessons/            # 📝 Markdown Instructions
│   └── lesson*_instructions.md
│
├── pdf_lessons/                 # 📄 PDF Documents (for printing)
│   └── lesson*_instructions.pdf
│
├── solutions/                   # ✅ Answer Keys
│   ├── *.ipynb                  # Jupyter notebook solutions
│   ├── *.sql                    # SQL script solutions
│   ├── *.py                     # Python script solutions
│   └── *.md                     # Written explanations
│
└── utils/                       # 🔧 Utility Scripts
    ├── md_to_pdf.py             # Markdown to PDF converter
    ├── install_dependencies.sh  # Dependency installer
    ├── convert_lessons.sh       # Quick conversion script
    └── README.md                # Utils documentation
```

## 📖 Lesson Formats

Each lesson is available in **three formats** to suit different learning styles:

### 📓 Jupyter Notebooks (Recommended)

**Location:** `jupyter_notebook_lessons/`

- **Interactive coding environment**
- Run SQL and Python code directly
- Instant feedback and results
- Best for hands-on learning

**How to use:**

1. Navigate to `jupyter_notebook_lessons/`
2. Open `lesson1_setup.ipynb`
3. Follow instructions and run cells as you go

### 📝 Markdown Instructions

**Location:** `markdown_lessons/`

- **Step-by-step written guides**
- Easy to read in VSCode or GitHub
- Great for reference
- Can copy SQL code to separate files

**How to use:**

1. Navigate to `markdown_lessons/`
2. Open `lesson1_instructions.md`
3. Read and follow along
4. Create your own `.sql` files in a `lessons/` folder

### 📄 PDF Documents

**Location:** `pdf_lessons/`

- **Print-friendly format**
- Professional formatting
- Perfect for offline study
- Easy to annotate

**How to use:**

1. Navigate to `pdf_lessons/`
2. Download or open `lesson1_instructions.pdf`
3. Print or view on tablet/second screen

## ✅ Solutions

**Location:** `solutions/`

Complete solutions are provided for instructors and self-checking:

- **Jupyter Notebooks** - Interactive solutions with explanations
- **SQL Files** - Complete SQL scripts
- **Python Files** - Working Python code
- **Markdown Files** - Written explanations

**🚨 Academic Honesty:** Attempt each lesson yourself before checking solutions!

### How to Use Solutions

1. **Complete the lesson first** - Give it your best effort
2. **Check your work** - Compare with solution after attempting
3. **Learn from differences** - Understand why the solution works
4. **Ask questions** - If solution doesn't make sense, ask instructor

### Solution Files Available

- `lesson1_setup.ipynb` / `lesson1_setup.sql`
- `lesson2_queries.ipynb` / `lesson2_queries.sql`
- `lesson3_sorting.ipynb` / `lesson3_sorting.sql`
- `lesson4_aggregates.ipynb` / `lesson4_aggregates.sql`
- `lesson5_schema.ipynb` / `lesson5_schema.sql` / `lesson5_data.sql`
- `lesson6_joins.ipynb` / `lesson6_joins.sql`
- `lesson7_modifications.ipynb` / `lesson7_modifications.sql`
- `lesson8_advanced.ipynb` / `lesson8_advanced.sql`
- `lesson9_database.ipynb` / `lesson9_database.py`
- `lesson10_comparison.ipynb` / `lesson10_comparison.md`

## 🎯 Learning Tips

1. **Type everything yourself** - Don't copy/paste. Muscle memory helps learning.
2. **Experiment freely** - The Codespace resets, so try variations without fear.
3. **Read error messages** - They're your friends! They tell you what went wrong.
4. **Use the VSCode plugin** - Visualize your database structure and results.
5. **Complete challenge problems** - They prepare you for exam-style questions.
6. **Build incrementally** - Each lesson builds on the previous one.
7. **Save your work** - Commit changes to preserve your progress.

## � Generating PDFs

Want to create your own PDFs from markdown files or update existing PDFs?

### Quick Start

```bash
bash utils/convert_lessons.sh
```

This will automatically:

- Install required dependencies (if needed)
- Convert all markdown lessons to PDF
- Save PDFs to `pdf_lessons/` directory

### Manual Conversion

**Install dependencies:**

```bash
bash utils/install_dependencies.sh
```

**Convert all lessons:**

```bash
python3 utils/md_to_pdf.py --directory markdown_lessons --output-dir pdf_lessons
```

**Convert single lesson:**

```bash
python3 utils/md_to_pdf.py --file markdown_lessons/lesson1_instructions.md --output-dir pdf_lessons
```

For more details, see [`utils/README.md`](utils/README.md) or [`QUICKSTART_PDF.md`](QUICKSTART_PDF.md)

## �💡 How to Use SQL Files

### Running SQL Queries in VSCode

**Method 1: Using the SQLite3 Editor Plugin**

1. Right-click on `database/starwars.db` (once created) → "Open with SQLite3 Editor"
2. Open your `.sql` file in the editor
3. Select the SQL code you want to run
4. Right-click → "Run Selected Query"
5. View results in the Output panel

**Method 2: Quick Execute**

- Open any `.sql` file
- Use keyboard shortcut (varies by OS)
- Results appear instantly

### Tips

- The VSCode plugin is already installed and configured
- You can execute multiple queries at once
- Results display in a clean, tabular format

## 🔍 Assessment

### Ongoing Evaluation

- ✅ SQL file completeness and correctness
- ✅ Python script functionality
- ✅ Challenge problem solutions
- ✅ Code organization and comments

### Optional Final Project

Choose one capstone project:

1. **Star Wars Encyclopedia CLI** - Full CRUD application with advanced features
2. **Database Design Challenge** - Expand the database with new tables
3. **SQL vs ORM Performance Study** - Benchmark and analyze different approaches

## 📚 Additional Resources

### Online Practice

- [SQLBolt](https://sqlbolt.com/) - Interactive SQL tutorials
- [LeetCode Database Problems](https://leetcode.com/problemset/database/) - Practice SQL challenges
- [DB Fiddle](https://www.db-fiddle.com/) - Online SQL playground

### Documentation

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python sqlite3 Module](https://docs.python.org/3/library/sqlite3.html)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

### Star Wars Data

- [SWAPI - The Star Wars API](https://swapi.dev/) - For additional data ideas

## 🤝 Getting Help

1. **Read error messages carefully** - They usually explain the problem
2. **Check your SQL syntax** - Typos are common
3. **Review previous lessons** - The solution might be in earlier material
4. **Use the resources folder** - Quick reference materials available
5. **Ask your instructor** - We're here to help!
6. **Check the solutions folder** - After attempting problems yourself

## 📝 Curriculum Alignment

This course covers all required curriculum points:

✅ Apply a web-based database and construct scripts that execute SQL  
✅ Selecting fields  
✅ Incorporating GROUP BY  
✅ Common SQL queries  
✅ Constraints using WHERE keyword  
✅ Table joins  
✅ Interfacing with SQL and non-SQL databases  
✅ Compare Object-Relational Mapping (ORM) to SQL

## 🎓 Exam Preparation

**Focus Areas for Assessment:**

- SQL syntax (primary focus)
- SELECT queries with WHERE, ORDER BY, LIMIT
- Aggregate functions and GROUP BY
- Table joins (INNER, LEFT, RIGHT)
- Subqueries
- UPDATE and DELETE operations
- Database design concepts

**Less Emphasis:**

- ORM (conceptual understanding only)
- NoSQL (awareness level)
- Python integration (practical skill, not exam focus)

## ⭐ May the Force Be With You!

Ready to begin your SQL journey? Start with **Lesson 1** in the `lessons/` folder!

---

**Course maintained by:** TempeHS  
**Version:** 1.0  
**Last Updated:** November 2025
