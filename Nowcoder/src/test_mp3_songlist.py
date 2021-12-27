import unittest
import mp3_songlist


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.mp3 = mp3_songlist.MP3SongList
        self.simulate = mp3_songlist.simulate_commands

    def test_mp3(self):
        return

    def test_case_1(self):
        n = 83
        cmds = "UUDUDDDDUDUUDDDDUDD"
        on_display_songs, selected_song = self.simulate(n, cmds)
        answer_on_display = [3, 4, 5, 6]
        answer_selected = 6
        self.assertListEqual(answer_on_display, on_display_songs)
        self.assertEqual(answer_selected, selected_song)

    def test_case_2(self):
        n = 81
        cmds = "DDUUUDUUDDUDUUUUDUDDDDDUDUUDDUUDUDDUUUDUUUUUDDDDUDDDUUUDUUUDDDDDUDDDDDUDDDDDUDDUDDDDU"
        on_display_songs, selected_song = self.simulate(n, cmds)
        answer_on_display = [10, 11, 12, 13]
        answer_selected = 12
        self.assertListEqual(answer_on_display, on_display_songs)
        self.assertEqual(answer_selected, selected_song)

    def test_case_3_less_than_window_size(self):
        n = 2
        cmds = "DUDUDDUUDUDDDDUDUDDDUUDDUDDUDUDUDDDUDUDUUDDUUDDUUUDUDUUUDDUDUDDUUDUDDDDUDUDUUDUDDDDDUU"
        on_display_songs, selected_song = self.simulate(n, cmds)
        answer_on_display = [1, 2]
        answer_selected = 1
        self.assertListEqual(answer_on_display, on_display_songs)
        self.assertEqual(answer_selected, selected_song)


if __name__ == '__main__':
    unittest.main()
