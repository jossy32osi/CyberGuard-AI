# CyberGuard AI - Software Requirements Specification (SRS)

## 1. Introduction

### 1.1 Purpose

This document defines the functional and non-functional requirements for CyberGuard AI, an AI-powered cybersecurity assistant designed to help individuals identify phishing attempts, scam messages, fraudulent websites, and other cyber threats.

### 1.2 Project Scope

CyberGuard AI provides users with an intelligent platform where they can submit suspicious URLs, messages, emails, or screenshots for analysis. The system uses artificial intelligence and cybersecurity techniques to evaluate potential threats, explain risks in simple language, and recommend appropriate actions.

### 1.3 Target Users

- Students
- Job seekers
- Small business owners
- Online shoppers
- Financial service users
- General internet users

---

# 2. Functional Requirements

The system shall:

### FR-001
Allow users to analyze suspicious URLs.

### FR-002
Allow users to submit suspicious text messages.

### FR-003
Analyze email content for phishing indicators.

### FR-004
Allow users to upload screenshots for AI analysis.

### FR-005
Generate a cybersecurity risk score from 0–100.

### FR-006
Explain detected threats in clear, non-technical language.

### FR-007
Provide recommendations on what users should do next.

### FR-008
Generate downloadable security reports.

### FR-009
Maintain a history of previous scans.

### FR-010
Display confidence levels for AI predictions.

---

# 3. Non-Functional Requirements

## Performance

- Response time should be less than 5 seconds for normal analyses.
- The system should support multiple users simultaneously.

## Security

- User data must be encrypted during transmission.
- Uploaded files should be securely processed.
- Personal information should not be permanently stored unless the user chooses to save it.

## Reliability

- The application should be available at least 99% of the time.
- Failed analyses should return meaningful error messages.

## Usability

- The interface should be simple and beginner-friendly.
- Risk explanations should use plain language.
- Navigation should be intuitive.

## Scalability

- The system should allow future integration with additional AI models.
- The architecture should support cloud deployment.

---

# 4. Assumptions

- Users have internet access.
- AI services are available during analysis.
- Users provide accurate input data.

---

# 5. Constraints

- Free AI services may have usage limits.
- Analysis accuracy depends on the quality of submitted data.
- Internet connectivity is required for AI-powered features.

---

# 6. Success Criteria

CyberGuard AI will be considered successful if:

- It accurately identifies phishing attempts.
- It helps users understand cyber threats.
- It reduces the likelihood of users falling victim to scams.
- It provides fast and reliable security analysis.
- It demonstrates the practical use of AI in cybersecurity.