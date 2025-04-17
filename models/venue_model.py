# models/venue_model.py
from db import Database

class VenueModel:
    def __init__(self):
        self.db = Database().get_collection("cf_venues")

    def get_venue_by_id(self, venue_id):
        venue = self.db.find_one({"vid": venue_id})
        if venue:
            venue["_id"] = str(venue["_id"])  # Convert ObjectId to string
            return venue
        return None
    
    def get_t20_sts_by_inning(self, venue_id, inning_number):
        # Fetch data where the venue_id is matched and inning data (sts) exists for the specific inning
        venue = self.db.find_one(
            {"vid": venue_id},  # Filter by venue_id
            {"t20.sts." + str(inning_number): 1, "_id": 0}  # Project only the t20.sts for the given inning
        )
        
        # Check if the venue and inning data exists
        if venue and "t20" in venue and "sts" in venue["t20"]:
            inning_data = venue["t20"]["sts"].get(str(inning_number), None)
            if inning_data:
                return inning_data
        return None
        
    def get_random_search(self, venue_id, search_string):
        # Construct the projection as a dictionary
        projection = {search_string: 1, "_id": 0}  # Include only the search string and exclude _id
        
        # Create a filter to check if the field exists
        filter_query = { "vid": venue_id, search_string: {"$exists": True } }
        
        # Fetch data where the venue_id is matched and the field exists
        venue = self.db.find_one(
            filter_query,  # Filter by venue_id and ensure the field exists
            projection  # Project only the desired field
        )
        
        # Check if the venue data exists and access the nested value
        if venue:
            # Use the dynamic search_string to access the specific nested field
            keys = search_string.split(".")
            value = venue
            for key in keys:
                value = value.get(key, {})
            return value
        return None