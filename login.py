from flask import Flask, request, jsonify
import mysql.connector
from database_connection import db


def login(data):
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    try:
        connection = db.get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # Query to check user credentials and get user type
        query = """
        SELECT u.ID, u.EMAIL, u.NAME, u.PASSWORD, ut.TYPE
        FROM users u
        JOIN user_types ut ON u.ROLE = ut.ID
        WHERE u.EMAIL = %s
        """
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        print(user)

        if user and user['PASSWORD'] == password:
            user_type = user['TYPE']
            if user_type.lower() == 'admin' or user_type.lower() == 'super_admin':
                return jsonify({'success': True, 'redirect': '/admin', 'user_type': user_type.lower()}), 200
            else:
                return jsonify({'success': True, 'redirect': '/home', 'user_type': 'customer', 'customer_id': user['ID'], 'customer_name': user['NAME']}), 200
        else:
            return jsonify({'error': 'Invalid email or password'}), 401

    except mysql.connector.Error as err:
        print(err)
        return jsonify({'error': f'Database error: {err}'}), 500
