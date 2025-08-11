import express, { json } from "express";
import dotenv from "dotenv";
import {} from "./Controller/emailController.js"

dotenv.config();

const app = express();

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


app.post("/send", )


app.use("*" , (req, res) => {
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
