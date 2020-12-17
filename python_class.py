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


porche = Car(color="Yellow", price="$40")
kia = Car()

print(kia.color, kia.price)
print(porche.color, porche.price)
