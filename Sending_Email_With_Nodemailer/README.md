# 📧 Email Service API

## Description  
A professional Node.js email service with templating support, built with Express and Nodemailer. Features automatic email type detection and responsive HTML templates for various use cases.

<br>

## Features

### 1. Email Service with Smart Templates 📧🎨
* **📤 Dual Email Support:** Simple text emails & templated HTML emails
* **🎨 Smart Templates:** Automatic email type detection (question, info, urgent, business)
* **📱 Responsive Design:** Mobile-friendly HTML email templates with Turkish localization
* **⚡ Express.js Framework:** Fast and lightweight REST API implementation
* **🔒 Secure Configuration:** Environment-based authentication and settings

<br>

## Core Technologies
### Frameworks & Libraries
* **Node.js 16+:** JavaScript runtime for building scalable network applications
* **Express.js:** Minimal and flexible web application framework
* **Nodemailer:** Module for sending emails from Node.js applications
* **dotenv:** Zero-dependency module that loads environment variables
* **HTML/CSS:** Responsive email template design with inline styling

<br>

## Installation & Setup

**Prerequisites**:
- Node.js 16+
- Email service account (Gmail, Outlook, etc.)
- App password for email authentication

```
git clone https://github.com/mehmetpektass/Services.git
cd Sending_Email_With_Nodemailer
```
```
pip install -r requirements.txt
```

<br>

## Environment Configuration
Create an .env file in the root directory:

```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-app-password
FROM_SENDER="Your Name <your-email@gmail.com>"
PORT=4000
```

<br>

## API Endpoints

### GET "/"
- Returns API documentation and example payloads.

### POST "/send"
- Send simple text/HTML emails.

#### Request Body:

```
{
  "to": "recipient@example.com",
  "subject": "Email Subject",
  "text": "Plain text content",
  "html": "<p>HTML content</p>"
}
````

### POST "/send-template"
- Send templated emails with automatic styling.

#### Request Body:

```
{
  "to": "recipient@example.com",
  "templateData": {
    "title": "Meeting Request",
    "message": "Should we schedule a project meeting?",
    "recipientName": "Ahmet",
    "type": "question",
    "actionUrl": "https://calendar.com",
    "actionText": "Schedule Meeting"
  }
}
```

<br>
<br>

## Contribution Guidelines 🚀

##### Pull requests are welcome. If you'd like to contribute, please:
- Fork the repository
- Create a feature branch
- Submit a pull request with a clear description of changes
- Ensure code follows existing style patterns
- Update documentation as needed
