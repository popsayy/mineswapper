import random

class Minesweeper:
    def __init__(self, lebar, tinggi, ranjau):
        self.lebar = lebar
        self.tinggi = tinggi
        self.ranjau = ranjau
        self.papan = [[' ' for _ in range(lebar)] for _ in range(tinggi)]
        self.terlihat = [[' ' for _ in range(lebar)] for _ in range(tinggi)]
        self.permainan_selesai = False
        self.tempatkan_ranjau()
        self.hitung_angka()

    def tempatkan_ranjau(self):
        posisi_ranjau = random.sample(range(self.lebar * self.tinggi), self.ranjau)
        for pos in posisi_ranjau:
            x = pos % self.lebar
            y = pos // self.lebar
            self.papan[y][x] = '*'

    def hitung_angka(self):
        for y in range(self.tinggi):
            for x in range(self.lebar):
                if self.papan[y][x] == '*':
                    continue
                self.papan[y][x] = str(self.hitung_ranjau_sekitar(x, y))

    def hitung_ranjau_sekitar(self, x, y):
        jumlah = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.lebar and 0 <= ny < self.tinggi:
                    if self.papan[ny][nx] == '*':
                        jumlah += 1
        return jumlah

    def ungkap(self, x, y):
        if self.papan[y][x] == '*':
            self.permainan_selesai = True
            return
        self.terlihat[y][x] = self.papan[y][x]
        if self.papan[y][x] == '0':
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.lebar and 0 <= ny < self.tinggi:
                        if self.terlihat[ny][nx] == ' ':
                            self.ungkap(nx, ny)

    def tampilkan(self):
        print("  " + " ".join(str(x) for x in range(self.lebar)))
        for y in range(self.tinggi):
            print(str(y) + " " + " ".join(self.terlihat[y]))

    def main(self):
        while not self.permainan_selesai:
            self.tampilkan()
            try:
                x, y = map(int, input("Masukkan koordinat (x y): ").split())
                if 0 <= x < self.lebar and 0 <= y < self.tinggi:
                    self.ungkap(x, y)
                else:
                    print("Koordinat di luar batas. Coba lagi.")
            except ValueError:
                print("Input tidak valid. Harap masukkan dua angka yang dipisahkan oleh spasi.")
        print("Permainan Selesai! Anda terkena ranjau.")
        self.tampilkan()

if __name__ == "__main__":
    lebar = 10
    tinggi = 10
    ranjau = 10
    permainan = Minesweeper(lebar, tinggi, ranjau)
    permainan.main()