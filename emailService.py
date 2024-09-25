from flask import Flask, request, jsonify
from flask_mail import Mail, Message

mail = Mail()


def send_email(email, subject, message):
    recipient = email
    subject = subject
    body = message

    if not all([recipient, subject, body]):
        return jsonify({'error': 'Missing required fields'}), 400

    print(recipient)
    print(subject)
    print(body)
    try:
        print(body)
        msg = Message(subject, recipients=[recipient], body=body)
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        print(e)
        return False
