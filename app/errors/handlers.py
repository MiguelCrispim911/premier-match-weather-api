from flask import jsonify
from werkzeug.exceptions import HTTPException


def register_error_handlers(app):
	@app.errorhandler(HTTPException)
	def handle_http_exception(error):
		response = {
			"error": {
				"code": error.code,
				"name": error.name,
				"message": error.description,
			}
		}
		return jsonify(response), error.code

	@app.errorhandler(Exception)
	def handle_unexpected_exception(error):
		response = {
			"error": {
				"code": 500,
				"name": "Internal Server Error",
				"message": "An unexpected error occurred.",
			}
		}
		return jsonify(response), 500
