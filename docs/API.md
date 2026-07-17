# CyberGuard AI - REST API Documentation

Version: 1.0

---

# 1. Introduction

## Purpose

This document defines the REST API for CyberGuard AI. The API enables secure communication between the frontend, backend, AI engine, and database.

The API follows RESTful design principles using JSON for requests and responses.

Base URL (Development)

```
http://localhost:8000/api/v1
```

Base URL (Production)

```
https://cyberguard-ai.com/api/v1
```

---

# 2. Authentication

CyberGuard AI uses JSON Web Tokens (JWT) for authentication.

Workflow

1. User logs in.
2. Server validates credentials.
3. JWT Access Token is generated.
4. Client stores the token securely.
5. Token is sent with protected API requests.

Example Header

```
Authorization: Bearer <JWT_TOKEN>
```

---

# 3. API Endpoints

## Health Check

### GET

```
/health
```

Purpose

Check whether the API is running.

Response

```json
{
    "status": "online",
    "version": "1.0",
    "message": "CyberGuard AI API is running."
}
```

Status Codes

200 OK

---

# User Authentication

## Register User

### POST

```
/auth/register
```

Request

```json
{
    "full_name": "Joshua Osiogo",
    "email": "example@email.com",
    "password": "StrongPassword123!"
}
```

Response

```json
{
    "message": "User registered successfully."
}
```

Status Codes

201 Created

400 Bad Request

409 Email Already Exists

---

## Login

### POST

```
/auth/login
```

Request

```json
{
    "email": "example@email.com",
    "password": "StrongPassword123!"
}
```

Response

```json
{
    "access_token": "JWT_TOKEN",
    "token_type": "Bearer"
}
```

Status Codes

200 OK

401 Unauthorized

---

# URL Analysis

## POST

```
/scan/url
```

Purpose

Analyze a suspicious URL.

Request

```json
{
    "url": "https://example.com"
}
```

Response

```json
{
    "risk_score": 87,
    "threat_level": "High",
    "prediction": "Likely Phishing",
    "confidence": 95,
    "recommendation": "Do not enter personal information."
}
```

Status Codes

200

400

500

---

# Email Analysis

## POST

```
/scan/email
```

Request

```json
{
    "subject": "Account Verification",
    "body": "Click here immediately..."
}
```

Response

```json
{
    "risk_score": 92,
    "threat_level": "Critical",
    "confidence": 97,
    "analysis": "Suspicious phishing language detected."
}
```

---

# SMS Analysis

## POST

```
/scan/text
```

Request

```json
{
    "message": "Your bank account has been suspended."
}
```

Response

```json
{
    "risk_score": 81,
    "threat_level": "High",
    "analysis": "Message resembles common banking scams."
}
```

---

# Screenshot Analysis

## POST

```
/scan/image
```

Content-Type

```
multipart/form-data
```

Request

Upload Image

Response

```json
{
    "risk_score": 90,
    "analysis": "Screenshot contains phishing indicators."
}
```

---

# Scan History

## GET

```
/history
```

Purpose

Retrieve previous scans.

Response

```json
[
    {
        "scan_id": 1,
        "scan_type": "URL",
        "risk_score": 84,
        "date": "2026-07-16"
    }
]
```

---

# Report Generation

## GET

```
/report/{report_id}
```

Purpose

Retrieve a generated report.

Response

```json
{
    "report_id": 12,
    "summary": "Potential phishing website.",
    "recommendation": "Avoid interacting with the site."
}
```

---

# Dashboard Statistics

## GET

```
/dashboard
```

Purpose

Retrieve user dashboard statistics.

Response

```json
{
    "total_scans": 105,
    "safe": 71,
    "suspicious": 23,
    "dangerous": 11
}
```

---

# 4. Standard HTTP Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 201  | Created               |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 409  | Conflict              |
| 422  | Validation Error      |
| 429  | Too Many Requests     |
| 500  | Internal Server Error |

---

# 5. Error Response Format

Example

```json
{
    "error": true,
    "message": "Invalid URL format.",
    "code": 400
}
```

---

# 6. Security Features

The API implements:

* HTTPS encryption
* JWT Authentication
* Password hashing with bcrypt
* Input validation
* Rate limiting
* SQL Injection prevention
* Cross-Site Scripting (XSS) protection
* Cross-Origin Resource Sharing (CORS) configuration
* Secure file upload validation
* Request logging

---

# 7. API Versioning

Current Version

```
v1
```

Future Versions

```
v2
```

```
v3
```

New features will be added without breaking existing client applications.

---

# 8. Future API Enhancements

Planned additions include:

* Browser extension endpoints
* Mobile application endpoints
* Threat intelligence feeds
* OCR document analysis
* Voice scam analysis
* AI chatbot integration
* Multi-language support
* Enterprise administration API

---

# 9. Testing Strategy

API testing will include:

* Unit testing
* Integration testing
* Authentication testing
* Performance testing
* Load testing
* Security testing
* Input validation testing
* File upload testing

---

# 10. Summary

The CyberGuard AI REST API provides a secure, scalable, and well-structured interface for communication between the application's frontend, backend, AI engine, and database. The design follows RESTful principles, supports future expansion, and incorporates cybersecurity best practices to protect user data and ensure reliable threat analysis.
