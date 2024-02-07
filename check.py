class rect:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
        self.area=self.l*self.b
        self.peri=2*(self.l+self.b)


utsav=rect(50,80)

print(utsav.area)
print(utsav.peri)
