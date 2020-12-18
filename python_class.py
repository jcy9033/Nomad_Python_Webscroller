# 객체지향 코드 Class, Object, Instance
# kwargs 는 사전형 {} get 메소드 사용 가능
class Car():
    def __init__(self, **kwargs):
        self.wheels = 4
        self.windows = 4
        self.color = kwargs.get("color", None)
        self.price = kwargs.get("price", "Not yet")

    def __str__(self):
        return f"Car with {self.windows} windows"


class Convertible(Car):

    def __init__(self, **kwargs):
        # 부모의 메소드를 확장시키기 위해서 사용하는 함수
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return f"Car with no roof"


porche = Convertible(color="Yellow", price="$40", time=5)
print(porche.color)
print(porche.time)
