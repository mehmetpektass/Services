import nodemailer, { createTransport } from "nodemailer";


const emailTrasporter = () => {
    return nodemailer.createTransport({
        host: process.env.EMAIL_HOST,
        port: process.env.EMAIL_PORT,
        secure: false, // true for 465, false for other ports
        auth: {
            user: process.env.EMAIL_USER,
            pass: process.env.EMAIL_PASS,
        },
    })
}

export async function sendEmail(req, res) {
    try {
        const { to, subject, text, html } = req.body;

        if (!to || !subject || (!text && !html)) {
            return res.status(400).json({
                success: false,
                message: 'to, subject ve text/html fields are necessary.'
            });
        }

        const transporter = emailTrasporter();

        const mailOptions = {
            from: `${process.env.FROM_SENDER}`,
            to: to,
            subject: subject,
            text: text,
            html: html
        };

        const info = transporter.sendMail(mailOptions);

        res.json({
            success: true,
            message: 'Email was sent successfully',
            messageId: info.messageId
        });

    } catch (error) {
        console.error('Email Sending Error:', error);
        res.status(500).json({
            success: false,
            message: 'Email Sending Error: ' + error.message
        });
    }
}

export async function sendTemplateEmail(req,res) {
    try {
        const { to, templateData} = req.body;
        

    } catch (error) {
        
    }
}
