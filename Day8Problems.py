import math


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        temp = ""
        if self.a == 0:
            temp = str(self.b) + "i"
        else:
            temp = str(self.a)
            if self.b > 0:
                temp += " + " + str(self.b) + "i"
            elif self.b < 0:
                temp += " - " + str(self.b * -1) + "i"

        return temp

    def add(self, other):
        temp_a = self.a + other.a
        temp_b = self.b + other.b
        return Complex(temp_a, temp_b)

    def negate(self):
        neg_a = self.a * -1
        neg_b = self.b * -1
        return Complex(neg_a, neg_b)

    def subtract(self, other):
        #sub_a = self.a - other.a
        #sub_b = self.b - other.b
        temp_other = other.negate()
        return self.add(temp_other)

    def multiply(self, other):
        real_a = self.a * other.a
        complex_a = self.a * other.b
        complex_b = self.b * other.a
        real_b = self.b * other.b

        real = real_a - real_b
        complex = complex_a + complex_b
        return Complex(real, complex)

    def conjugate(self):
        temp_b = self.b * -1
        return Complex(self.a, temp_b)

    def inverse(self):
        square_sum = math.pow(self.a, 2) + math.pow(self.b, 2)
        temp_a = self.a / square_sum
        temp_b = self.b / square_sum
        return Complex(temp_a, temp_b)

    def divide(self, other):
        square_sum_other = math.pow(other.a, 2) + math.pow(other.b, 2)
        denominator_a = self.a * other.a + self.b * other.b
        denominator_b = self.b * other.a - self.a * other.b
        temp_a = denominator_a / square_sum_other
        temp_b = denominator_b / square_sum_other
        return Complex(temp_a, temp_b)

    def __mul__(self, other):
        return self.multiply(other)

    def __sub__(self, other):
        return self.subtract(other)

c1 = Complex(1, -1)
print(c1)

c2 = Complex(-1, 1)
print(c2)

c3 = Complex(1, 1)
print(c2)

c4 = Complex(-1, -1)
print(c4)

c5 = Complex(-2, 0)
print(c5)

c6 = Complex(2, 0)
print(c6)

c7 = Complex(0, 7)
print(c7)

c8 = Complex(0, -7)
print(c8)

# Question 2
c1 = Complex(4, 3)
c2 = Complex(3, -5)
result = c1.add(c2)
print(result)

# Question 3
c1 = Complex(-4, 3)
result = c1.negate()
print(result)

# Question 4
c1 = Complex(4, 3)
c2 = Complex(3, -5)
result = c1.subtract(c2)
print(result)

# Question 5
c1 = Complex(4, 3)
c2 = Complex(3, -5)
result = c1.multiply(c2)
print(result)

# Question 6
c1 = Complex(-4, 3)
result = c1.conjugate()
print(result)

c1 = Complex(-4, 3)
result = c1.inverse()
print(result)

c1 = Complex(4, 3)
c2 = Complex(3, -5)
print(c1 * c2)

c1 = Complex(4, 3)
c2 = Complex(3, -5)
print(c1 - c2)