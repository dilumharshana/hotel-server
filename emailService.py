from flask import Flask, request, jsonify
from flask_mail import Mail, Message

mail = Mail()


def send_email():
    data = request.json
    recipient = data.get('recipient')
    subject = data.get('subject')
    body = data.get('body')

    if not all([recipient, subject, body]):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        print(body)
        msg = Message(subject, recipients=[recipient], body=body)
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
