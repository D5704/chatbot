from flask import render_template, current_app

from flask import request, jsonify
from app import app
from app.nlp_utils import process_user_message
from app.faq import get_faq_answer
from app.bank_transactions import process_transaction

@app.route('/')
def index():
    print("Chemin des templates :", current_app.template_folder)  # Affiche le chemin des templates
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = process_user_message(user_message)
    return jsonify({'response': response})

@app.route('/upload', methods=['POST'])
def upload():
    # Gestion des fichiers uploadés
    pass
