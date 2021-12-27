import functools


def main():
    while True:
        try:
            execute_once()
        except Exception as e:
            break


def execute_once():
    n_total_songs = int(input())
    commands = input()
    on_display_songs, selected_song = simulate_commands(n_total_songs, commands)
    str_on_display = functools.reduce(lambda n1, n2: str(n1) + ' ' + str(n2),
                                      on_display_songs)
    print(str_on_display)
    print(str(selected_song))


def simulate_commands(n_total_songs, commands):
    MP3 = MP3SongList(n_total_songs)
    for c in commands:
        if c == 'U':
            MP3.press_up()
        elif c == 'D':
            MP3.press_down()
    on_display, selected = MP3.get_current_state()
    return on_display, selected


class MP3SongList:
    N_MAX_ON_DISPLAY = 4

    def __init__(self, n_total_songs):
        self.n_total_songs = n_total_songs
        self.selected = 0
        self.window_start_offset = 0

    def press_up(self):
        if self.selected == 0:
            self.selected = self.n_total_songs - 1
            self.window_start_offset = max(0, self.n_total_songs - self.N_MAX_ON_DISPLAY)
        else:
            self.selected -= 1
            if self.window_start_offset > self.selected:
                assert self.window_start_offset - self.selected == 1
                self.window_start_offset -= 1

    def press_down(self):
        if self.selected == self.n_total_songs - 1:
            self.selected = 0
            self.window_start_offset = 0
        else:
            self.selected += 1
            if self.window_start_offset + self.N_MAX_ON_DISPLAY <= self.selected:
                assert self.window_start_offset + self.N_MAX_ON_DISPLAY == self.selected
                self.window_start_offset += 1

    def get_current_state(self):
        on_display = [i + 1 for i in range(self.window_start_offset,
                                           min(self.window_start_offset + self.N_MAX_ON_DISPLAY,
                                               self.n_total_songs))]
        selected = self.selected + 1
        return on_display, selected


if __name__ == '__main__':
    main()
