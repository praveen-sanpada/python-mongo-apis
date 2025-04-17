# routes/venue_routes.py
from flask import Blueprint, jsonify
from models.venue_model import VenueModel

venue_bp = Blueprint('venue_bp', __name__)

# Define Flask Route to Get Venue by ID
@venue_bp.route("/venues/get_venue/<venue_id>", methods=["GET"])
def get_venue(venue_id):
    venue_model = VenueModel()
    venue_data = venue_model.get_venue_by_id(venue_id)

    if venue_data:
        return jsonify(venue_data), 200  # Return the venue data in JSON format
    else:
        return jsonify({"error": "Venue not found"}), 404

# Define Flask Route to Get Venue's T20 Stats for Specific Inning
@venue_bp.route("/venues/get_t20_sts/<venue_id>/<inning_number>", methods=["GET"])
def get_t20_sts(venue_id, inning_number):
    venue_model = VenueModel()
    t20_inning_data = venue_model.get_t20_sts_by_inning(venue_id, inning_number)
    
    if t20_inning_data:
        return jsonify(t20_inning_data), 200  # Return the t20 inning data in JSON format
    else:
        return jsonify({"error": "Data not found for the specified venue and inning"}), 404
