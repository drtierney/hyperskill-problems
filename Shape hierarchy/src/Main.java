abstract class Shape {

    abstract double getPerimeter();

    abstract double getArea();
}

class Triangle extends Shape {
    double a;
    double b;
    double c;

    public Triangle(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    @Override
    double getPerimeter() {
        return a + b + c;
    }

    @Override
    double getArea() {
        double d = (a + b + c) / 2.0;
        return Math.sqrt(d*(d-a)*(d-b)*(d-c));
    }
}

class Rectangle extends Shape {
    double a;
    double b;

    public Rectangle(double a, double b) {
        this.a = a;
        this.b = b;
    }

    @Override
    double getPerimeter() {
        return (a * 2) + (b * 2);
    }

    @Override
    double getArea() {
        return a * b;
    }
}

class Circle extends Shape {
    double a;

    public Circle(double a) {
        this.a = a;
    }

    @Override
    double getPerimeter() {
        return 2 * a * Math.PI;
    }

    @Override
    double getArea() {
        return Math.PI * a * a;
    }
}