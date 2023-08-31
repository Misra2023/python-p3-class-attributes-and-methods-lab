from song import Song  # Import the Song class from your song.py module
import unittest

class TestSong(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize Song objects and class-level variables here
        cls.song1 = Song("99 Problems", "Jay Z", "Rap")
        cls.song2 = Song("Halo", "Beyonce", "Pop")
        cls.song3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        cls.song4 = Song("Sara Smile", "Hall and Oates", "Pop")

    @classmethod
    def tearDownClass(cls):
        # Reset class-level variables after all tests
        Song.count = 0
        Song.genres = set()
        Song.artists = set()
        Song.genre_count = {}
        Song.artist_count = {}

    def setUp(self):
        # Reset class-level variables before each test
        Song.count = 4
        Song.genres = {"Rap", "Pop", "Rock"}
        Song.artists = {"Jay Z", "Beyonce", "Nirvana", "Hall and Oates"}
        Song.genre_count = {"Rap": 1, "Pop": 3, "Rock": 1}
        Song.artist_count = {"Jay Z": 1, "Beyonce": 1, "Nirvana": 1, "Hall and Oates": 2}

    def test_saves_name_artist_genre(self):
        '''instantiates with a name, artist, and genre.'''
        out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
        self.assertEqual(out_of_touch.name, "Out of Touch")
        self.assertEqual(out_of_touch.artist, "Hall and Oates")
        self.assertEqual(out_of_touch.genre, "Pop")

    def test_has_song_count(self):
        '''counts the total number of Song objects.'''
        self.assertEqual(Song.count, 4)
        Song("Another Song", "Another Artist", "Pop")  # Create another song
        self.assertEqual(Song.count, 5)

    def test_has_genres(self):
        '''keeps track of all Song genres.'''
        self.assertIn("Rap", Song.genres)
        self.assertIn("Pop", Song.genres)
        self.assertIn("Rock", Song.genres)

    def test_has_artists(self):
        '''keeps track of all Song artists.'''
        self.assertIn("Jay Z", Song.artists)
        self.assertIn("Beyonce", Song.artists)
        self.assertIn("Hall and Oates", Song.artists)
        
    def test_has_genre_count(self):
        '''keeps count of Songs for each genre.'''
        self.assertEqual(Song.genre_count["Rap"], 1)
        self.assertEqual(Song.genre_count["Pop"], 3)
        self.assertEqual(Song.genre_count["Rock"], 1)

    def test_has_artist_count(self):
        '''keeps count of Songs for each artist.'''
        self.assertEqual(Song.artist_count["Jay Z"], 1)
        self.assertEqual(Song.artist_count["Beyonce"], 1)
        self.assertEqual(Song.artist_count["Nirvana"], 1)
        self.assertEqual(Song.artist_count["Hall and Oates"], 2)

if __name__ == '__main__':
    unittest.main()
