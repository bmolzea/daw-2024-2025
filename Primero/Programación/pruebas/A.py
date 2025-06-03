class A:
    def __init__(self, a: int):
        self.a = a
    
    def b(self)->int:
        return self.a+1

if __name__ == "__main__":
    objeto = A(3)
    print(objeto.b())