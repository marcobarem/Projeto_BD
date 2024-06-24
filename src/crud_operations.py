# src/crud_operations.py
def insert_track(collection, track):
    collection.insert_one(track)

def query_tracks(collection, year=None, min_popularity=None):
    query = {}
    if year:
        query['year'] = year
    if min_popularity:
        query['popularity'] = {"$gt": min_popularity}
    projection = {"_id": 0, "title": 1, "artist_name": 1, "popularity": 1, "year": 1}
    results = collection.find(query, projection)
    return list(results)

def update_track(collection, track_id, new_popularity):
    query = {"track_id": track_id}
    update = {"$set": {"popularity": new_popularity}}
    collection.update_one(query, update)

def delete_track(collection, track_id):
    query = {"track_id": track_id}
    collection.delete_one(query)
