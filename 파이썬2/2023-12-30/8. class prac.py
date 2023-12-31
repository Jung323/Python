class Watch:
    def What(self):
        self.time = input('시간을 입력하세요: ')
        self.hour = self.time.split(':')[0]
        self.minute = self.time.split(':')[1]
        self.second = self.time.split(':')[2]

    def see(self):
        print(f'계산된 시간은 {self.hour}시 {self.minute}분 {self.second}초입니다.')

watch = Watch()
watch.What()
watch.see()

