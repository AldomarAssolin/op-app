from flask import Blueprint, jsonify

bp_health = Blueprint('health', __name__)

@bp_health.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK"}), 200