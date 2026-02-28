class Song:
    # Class attributes
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}  # renamed to match the test

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update stats
        self.__class__.increment_count()
        self.__class__.register_genre(self.genre)
        self.__class__.register_artist(self.artist)
        self.__class__.increment_genre_count(self.genre)
        self.__class__.increment_artist_count(self.artist)

    # Class methods
    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def register_genre(cls, genre):
        cls.genres.add(genre)

    @classmethod
    def register_artist(cls, artist):
        cls.artists.add(artist)

    @classmethod
    def increment_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def increment_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1