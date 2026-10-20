class SongNode:
    def __init__(self, song_id, name, artist, duration):
        self.song_id = song_id
        self.name = name
        self.artist = artist
        self.duration = duration
        self.next = None


class Playlist:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.current = None  

    def addSong(self, song_id, name, artist, duration):
        node = SongNode(song_id, name, artist, duration)
        if self.size == 0:            
            self.head = node
            self.tail = node
        else:                       
            self.tail.next = node
            self.tail = node
        self.size = self.size + 1
        return node

    def searchSong(self, song_id):
        node = self.head
        while node is not None:
            if node.song_id == song_id:
                break
            node = node.next
        return node

    def deleteSong(self, song_id):
        prev = None
        cur = self.head
        found = False
        while cur is not None:
            if cur.song_id == song_id:
                found = True
                break
            prev = cur
            cur = cur.next
        if not found:
            return False
        if prev is None:           
            self.head = cur.next
        else:
            prev.next = cur.next
        if cur is self.tail:
            self.tail = prev
        if cur is self.current:
            self.current = prev
        self.size = self.size - 1
        return True

    def displayPlaylist(self):
        if self.size == 0:
            print("Playlist boşdur.")
            return
        parts = []
        node = self.head
        while node is not None:
            parts.append(f"[{node.song_id}] {node.name} - {node.artist} ({node.duration})")
            node = node.next
        parts.append("None")
        print(" -> ".join(parts))

    def countSongs(self):
        return self.size

    def playNextSong(self):
        if self.size == 0:
            print("Playlist boşdur.")
            return None
        if self.current is None or self.current.next is None:
            self.current = self.head      
        else:
            self.current = self.current.next
        print(f"Oynatılır: {self.current.name} - {self.current.artist} ({self.current.duration})")
        return self.current


def main():
    pl = Playlist()
    choice = ""
    while choice != "7":
        print("\n1. mahnı əlavə et\n2. mahnı sil\n3. mahnı axtar\n4. Playlisti göstər\n5. Növbəti mahnını oynat\n6. Mahnıları say\n7. Çıxış")
        choice = input("seçim: ").strip()
        if choice == "1":
            sid = int(input("ID: "))
            if pl.searchSong(sid):
                print("mahnı artıq mövcuddur.")
                continue
            name = input("Mahnı adı: ")
            artist = input("Artist: ")
            duration = input("Mahnı müddəti: ")
            pl.addSong(sid, name, artist, duration)
            print("mahnı əlavə olundu.")
        elif choice == "2":
            sid = int(input("ID: "))
            if pl.deleteSong(sid):
                print("mahnı silindi.")
            else:
                print("mahnı tapılmadı.")
        elif choice == "3":
            s = pl.searchSong(int(input("ID: ")))
            if s is None:
                print("mahnı tapılmadı.")
            else:
                print(f"Tapıldı: {s.name} - {s.artist} ({s.duration})")
        elif choice == "4":
            pl.displayPlaylist()
        elif choice == "5":
            pl.playNextSong()
        elif choice == "6":
            print("Mahnılar:", pl.countSongs())
        elif choice != "7":
            print("yoxdur.")


if __name__ == "__main__":
    main()
