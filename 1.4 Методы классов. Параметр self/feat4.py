class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f'Воспроизведение файла {self.filename}')


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open('filename1')
media2.open('filename2')

media1.play()
media2.play()
