import express, { json } from "express";
import dotenv from "dotenv";
import nodemailer from "nodemailer";
import {sendEmail, sendTemplateEmail}  from "./Controller/emailController.js";

dotenv.config();

const app = express();
const port = process.env.PORT || 4000;

app.use(express.json());

app.get("/", (req, res) => {
    res.json({
        message: "Email Service API",
        endpoints: {
            "POST /send": "Send a simple email.",
            "POST /send-template": "Send an email with template.",
            "GET /test-connection": "Test the email connection."
        },
        example: {
            template: {
                to: 'someone@example.com',
                templateData: {
                    title: 'Project Situation',
                    message: 'Should we adjust a meeting for the project?',
                    recipientName: 'Ahmet',
                    type: 'question',
                    actionUrl: 'https://calendar.com',
                    actionText: 'Adjust a Meeting'
                }
            }
        }
    })
})


app.post("/send", sendEmail);
app.post("/send-template", sendTemplateEmail);


app.use((req, res) => {
    res.status(404).json({
        success: false,
        message: "Invalid endpoint. Check the main (/) page.",
    })
})

app.use((error, req, res, next) => {
    console.log("Server Error", error);
    res.status(500).json({
        success: false,
        message: "Server Error!",
    })
})


app.listen(port, async () => {
    console.log(`\n🚀 Email Service's Started: http://localhost:${port}`);
    console.log(`📧 Email: ${process.env.FROM_SENDER}`);

    try {
        const transporter = nodemailer.createTransport({
            host: process.env.EMAIL_HOST,
            port: process.env.EMAIL_PORT,
            secure: false,
            auth: {
                user: process.env.EMAIL_USER,
                pass: process.env.EMAIL_PASS
            }
        })

        await transporter.verify();
        console.log("Email Connection Completed")

    } catch (error) {
        console.log("Email Connection Error", error.message)
    }
})