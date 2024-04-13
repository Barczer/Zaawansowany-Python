class Playlist():

    def __init__(self, playlist):
        self.playlist = playlist if isinstance(playlist, list) else []

    def __str__(self):
        return f"Twoja lista to: {self.playlist}"

    def __add__(self, other):
        self.playlist.append(other)

    def __radd__(self, other):
        self.playlist.append(other)

    def __getitem__(self, item):
        return self.playlist[item]

    def __setitem__(self, key, value):
        self.playlist[key] = value


p1 = Playlist(['aaa1', 'aaa2', 'aaa3', 'aaa4'])

print(p1)
p1 + 'bbb1'
print(p1)
print(p1.__getitem__(0))
p1.__setitem__(0, 'vvv1')
print(p1)