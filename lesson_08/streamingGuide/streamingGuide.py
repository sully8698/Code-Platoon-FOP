class Movie:
    def __init__(self, title, genre, director, year):
        self._title = title
        self._genre = genre
        self._director= director
        self._year = year

    def get_title(self):
        return self._title
        
    def get_genre(self):
        return self._genre
        
    def get_director(self):
        return self._director
        
    def get_year(self):
        return self._year
    
class StreamingService:
    def __init__(self, name):
        self._name = name
        self._catalog = {}
    
    def get_name(self):
        return self._name
    
    def get_catalog(self):
        return self._catalog

    def add_movie(self, movie_object):
        self._catalog[movie_object.get_title()] = movie_object
    
    def delete_movie(self, movie_title):
        self._catalog.pop(movie_title)

class StreamingGuide:
    def __init__(self):
        self._streaming_services = [] 
    
    def add_streaming_service(self, streaming_service_object):
        self._streaming_services.append(streaming_service_object)

    def get_streaming_services(self):
        return self._streaming_services

    def delete_streaming_service(self, streaming_service_name):
        for value in self._streaming_services:
            if value.get_name() == streaming_service_name:
                self._streaming_services.remove(value)
    
    def where_to_watch_movie(self, movie_title):
        date = ''
        list = []
        for service in self._streaming_services:
            streamer = service.get_catalog()
            
            # print(service.get_name())
            # print(streamer[movie_title].get_year())
            
            if movie_title in streamer:
                check = f'{movie_title} ({streamer[movie_title].get_year()}'
                if check not in list:
                    list.append(check)
                    list.append(service.get_name())
                    # list.append(movie_title)
                    # list.append(streamer[movie_title].get_year())
                else:
                    list.append(service.get_name())
        
        if len(list) > 0:
            return list
        else:
            return "None"


    
movie_1 = Movie('Rocks', 'Drama', 'Some guy', 2020)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

stream_service_1 = StreamingService('Netflix')
stream_service_1.add_movie(movie_1)
stream_service_1.add_movie(movie_2)

stream_service_2 = StreamingService('Hulu')
stream_service_2.add_movie(movie_3)
stream_service_2.add_movie(movie_1)

stream_guide = StreamingGuide()
stream_guide.add_streaming_service(stream_service_1)
stream_guide.add_streaming_service(stream_service_2)

print(stream_guide.where_to_watch_movie('Rocks'))






