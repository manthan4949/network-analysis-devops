from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///network_analysis.db')

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class PacketAnalysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    packet_data = db.Column(db.Text, nullable=False)
    source_ip = db.Column(db.String(15))
    destination_ip = db.Column(db.String(15))
    protocol = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Network Analysis App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f5f5f5;
            }
            .container {
                max-width: 1000px;
                margin: 0 auto;
                background-color: white;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
                border-bottom: 3px solid #007bff;
                padding-bottom: 10px;
            }
            .info {
                background-color: #e7f3ff;
                border-left: 4px solid #2196F3;
                padding: 12px;
                margin: 20px 0;
            }
            .status {
                display: inline-block;
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                margin-top: 10px;
            }
            ul {
                line-height: 1.8;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Network Analysis App</h1>
            <div class="info">
                <p>This Flask application analyzes network packets and provides detailed insights.</p>
            </div>
            <div class="status">✓ Application is running successfully!</div>
            <h2>Features:</h2>
            <ul>
                <li>Packet capture and analysis</li>
                <li>Network traffic visualization</li>
                <li>Protocol identification</li>
                <li>Traffic statistics</li>
                <li>User authentication</li>
            </ul>
            <h2>API Endpoints:</h2>
            <ul>
                <li>GET / - This welcome page</li>
                <li>GET /api/health - Application health check</li>
            </ul>
        </div>
    </body>
    </html>
    '''

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'network-analysis-app',
        'version': '1.0.0'
    })

@app.route('/api/packets', methods=['GET'])
def get_packets():
    packets = PacketAnalysis.query.limit(10).all()
    return jsonify([
        {
            'id': p.id,
            'source_ip': p.source_ip,
            'destination_ip': p.destination_ip,
            'protocol': p.protocol,
            'timestamp': str(p.timestamp)
        }
        for p in packets
    ])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
