# CyberGuard AI - Database Design Document

Version: 1.0

---

# 1. Introduction

## Purpose

This document defines the database architecture for CyberGuard AI. It describes the database structure, entities, relationships, constraints, and future scalability.

The database stores user information, scan results, AI analysis reports, and security logs while maintaining data integrity and protecting user privacy.

---

# 2. Database Objectives

The database must:

* Store user accounts securely.
* Store scan history.
* Store AI analysis results.
* Store generated reports.
* Record security events.
* Support future expansion.
* Ensure data integrity.
* Minimize duplicate data.

---

# 3. Database Management System

## Development

SQLite

Reason:

* Lightweight
* No installation required
* Easy to integrate with FastAPI

## Production

PostgreSQL

Reason:

* High performance
* Excellent security
* ACID compliance
* Cloud-ready
* Suitable for Oracle Cloud deployment

---

# 4. Entity Relationship Diagram (ERD)

```
                +----------------+
                |     USERS      |
                +----------------+
                | user_id (PK)   |
                | full_name      |
                | email          |
                | password_hash  |
                | role           |
                | created_at     |
                +-------+--------+
                        |
                        | 1
                        |
                        | M
                +-------+--------+
                | SCAN_HISTORY   |
                +----------------+
                | scan_id (PK)   |
                | user_id (FK)   |
                | scan_type      |
                | input_data     |
                | risk_score     |
                | threat_level   |
                | created_at     |
                +-------+--------+
                        |
                        | 1
                        |
                        | 1
                +-------+--------+
                | REPORTS        |
                +----------------+
                | report_id (PK) |
                | scan_id (FK)   |
                | summary        |
                | recommendation |
                | ai_confidence  |
                +----------------+

                +----------------+
                | THREAT_LIBRARY |
                +----------------+
                | threat_id (PK) |
                | category       |
                | description    |
                | severity       |
                | updated_at     |
                +----------------+

                +----------------+
                | SECURITY_LOGS  |
                +----------------+
                | log_id (PK)    |
                | event_type     |
                | description    |
                | ip_address     |
                | timestamp      |
                +----------------+
```

---

# 5. Table Descriptions

## USERS

Purpose

Stores registered users.

Columns

* user_id (Primary Key)
* full_name
* email
* password_hash
* role
* created_at

---

## SCAN_HISTORY

Purpose

Stores every cybersecurity scan performed.

Columns

* scan_id
* user_id
* scan_type
* input_data
* risk_score
* threat_level
* created_at

Examples of scan_type

* URL
* Email
* SMS
* Screenshot

---

## REPORTS

Purpose

Stores AI-generated reports.

Columns

* report_id
* scan_id
* summary
* recommendation
* ai_confidence

---

## THREAT_LIBRARY

Purpose

Stores known phishing patterns and threat categories.

Columns

* threat_id
* category
* description
* severity
* updated_at

---

## SECURITY_LOGS

Purpose

Records security-related events.

Columns

* log_id
* event_type
* description
* ip_address
* timestamp

Example events

* Login
* Failed Login
* Scan Started
* Scan Completed
* Report Downloaded

---

# 6. Relationships

USERS → SCAN_HISTORY

Relationship

One user can perform many scans.

Relationship Type

One-to-Many (1:M)

---

SCAN_HISTORY → REPORTS

Relationship

Each completed scan generates one report.

Relationship Type

One-to-One (1:1)

---

# 7. Data Types

Examples

INTEGER

Primary Keys

TEXT

Names

Emails

Descriptions

REAL

AI Confidence

Risk Score

TIMESTAMP

Date and Time

BOOLEAN

True / False Values

---

# 8. Data Integrity Rules

* Email addresses must be unique.
* Passwords are never stored in plain text.
* Foreign keys maintain relationships.
* Deleted users do not automatically delete reports.
* Scan timestamps are generated automatically.

---

# 9. Security Considerations

CyberGuard AI follows secure database practices.

Security measures

* Password hashing using bcrypt
* Parameterized SQL queries
* SQL Injection prevention
* Access control
* Database backups
* Encrypted communication
* Least privilege principle

---

# 10. Backup Strategy

Development

Local backups

Production

* Daily automated backups
* Weekly full backup
* Monthly archive
* Disaster recovery plan

---

# 11. Future Database Enhancements

Version 2

* User preferences
* Notification settings
* Saved searches

Version 3

* Organization accounts
* Team management
* Audit logs
* Threat intelligence feeds

Version 4

* AI model history
* Threat analytics
* Dashboard metrics
* Machine learning feedback

---

# 12. Sample SQL Table

Example USERS table

```sql
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# 13. Summary

The CyberGuard AI database is designed to provide a secure, scalable, and efficient foundation for storing user information, cybersecurity scan results, AI-generated reports, and security logs. The design supports future growth while maintaining performance, reliability, and strong security practices.
