import java.util.Scanner;

/* Product - Motor */
abstract class Motor {

    String model;
    long power;

    public Motor(String model, long power) {
        this.model = model;
        this.power = power;
    }

    @Override
    public String toString() {
        return "motor={model:" + model + ",power:" + power + "}";
    }
}

class PneumaticMotor extends Motor {
    // write your code here ...

    public PneumaticMotor(String model, long power) {
        super(model, power);
    }

    @Override
    public String toString() {
        return "Pneumatic motor={model:" + model + ",power:" + power + "}";
    }
}

class HydraulicMotor extends Motor {
    // write your code here ...

    public HydraulicMotor(String model, long power) {
        super(model, power);
    }

    @Override
    public String toString() {
        return "Hydraulic motor={model:" + model + ",power:" + power + "}";
    }
}

class ElectricMotor extends Motor {
    // write your code here ...

    public ElectricMotor(String model, long power) {
        super(model, power);
    }

    @Override
    public String toString() {
        return "Electric motor={model:" + model + ",power:" + power + "}";
    }
}

class WarpDrive extends Motor {
    // write your code here ...

    public WarpDrive(String model, long power) {
        super(model, power);
    }

    @Override
    public String toString() {
        return "Warp drive={model:" + model + ",power:" + power + "}";
    }
}

class MotorFactory {

    /**
     * It returns an initialized motor according to the specified type by the first character:
     * 'P' or 'p' - pneumatic, 'H' or 'h' - hydraulic, 'E' or 'e' - electric, 'W' or 'w' - warp.
     */
    public static Motor make(char type, String model, long power) {
        // write your code here ...
        type = Character.toUpperCase(type);
        switch (type) {
            case 'P':
                return new PneumaticMotor(model, power);
            case 'H':
                return new HydraulicMotor(model, power);
            case 'E':
                return new ElectricMotor(model, power);
            case 'W':
                return new WarpDrive(model, power);
            default:
                return null;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        final Scanner scanner = new Scanner(System.in);
        final char type = scanner.next().charAt(0);     
        final String model = scanner.next();
        final long power = scanner.nextLong();
        // write your code here ...
        MotorFactory motorFactory = new MotorFactory();
        Motor motor = motorFactory.make(type, model, power);
        scanner.close();
       System.out.println(motor);
    }
}