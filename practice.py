import googlemaps

def distance(firstLocation, secondLocation):
    """Uses google maps API to return distance"""
    gmaps = googlemaps.Client(key="PUT KEY Here")
    matrix = gmaps.distance_matrix(firstLocation, secondLocation)
    #any better way to write this?????
    time_in_seconds = matrix['rows'][0]['elements'][0]['duration']['value']
    minutes = time_in_seconds//60
    return minutes

print(distance("New York", "Pittsburgh"))