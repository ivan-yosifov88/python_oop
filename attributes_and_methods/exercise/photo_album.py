class PhotoAlbum:

    MAX_PAGE_COUNT = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[]  * row for row in range(self.pages)]


    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(int(photos_count /4))

    @staticmethod
    def is_page_space(photos):
        return photos < PhotoAlbum.MAX_PAGE_COUNT

    def add_photo(self, label):
        for i in range(len(self.photos)):
            if self.is_page_space(len(self.photos[i])):
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {self.photos[i].index(label) +1 }"
        return "No more free spots"

    def display(self):
        line_with_dashes = f"{'-' * 11}\n"
        result = line_with_dashes
        for line in self.photos:
            line_list = ["[]"] * len(line)
            result += f"{' '.join(line_list)}\n"
            result += line_with_dashes
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
