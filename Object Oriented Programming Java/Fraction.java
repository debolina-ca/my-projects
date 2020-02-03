// Module 2 Project - Fraction Calculator
// This project is designed to help you practice building your own object class and testing it with a client class.
// You will be creating two classes, one called Fraction and the other called FractionCalculator.

// Part 1 - Fraction Class
// The Fraction class is an object that holds information about a fraction (numerator and denominator).
// It will have several constructors and both private and public methods implementing the behavior of a fraction.
//Create a new class called "Fraction" and include the following: Fields, Constructors, Methods
public class Fraction {
    //Fields
    private int numerator;
    private int denominator;

    // Constructors
    public Fraction(int numerator, int denominator) {
        if (denominator==0) {
            throw new IllegalArgumentException("denominator cannot be zero");
        }
        if ((numerator>=0 && denominator < 0) || (numerator<0 && denominator<0)) {
            this.numerator = -numerator;
            this.denominator = -denominator;
        } else {
            this.numerator = numerator;
            if (numerator==0) {
                this.denominator = 1;
            } else {
                this.denominator = denominator;
            }
        }
    }
    public Fraction(int numerator) {
        this(numerator, 1);
    }
    public Fraction() {
        this(0, 1);
    }
    // Methods
    public int getNumerator() {
        return numerator;
    }
    public int getDenominator() {
        return denominator;
    }
    public String toString() {
        return numerator + "/" + denominator;
    }
    public double toDouble() {
        return (double)numerator/denominator;
    }
    public Fraction add(Fraction other) {
        int resultNumerator = this.numerator * other.denominator + this.denominator * other.numerator;
        int resultDenominator = this.denominator * other.denominator;
        Fraction result = new Fraction(resultNumerator, resultDenominator);
        return result;
    }
    public Fraction subtract(Fraction other) {
        int resultNumerator = this.numerator * other.denominator - this.denominator * other.numerator;
        int resultDenominator = this.denominator * other.denominator;
        Fraction result = new Fraction(resultNumerator, resultDenominator);
        return result;
    }
    public Fraction multiply(Fraction other) {
        int resultNumerator = this.numerator * other.numerator;
        int resultDenominator = this.denominator * other.denominator;
        Fraction result = new Fraction(resultNumerator, resultDenominator);
        return result;
    }
    public Fraction divide(Fraction other) {
        int resultNumerator = this.numerator * other.denominator;
        int resultDenominator = this.denominator * other.numerator;
        Fraction result = new Fraction(resultNumerator, resultDenominator);
        return result;
    }
    public boolean equals(Object other) {
        boolean result = false;
        double fraction1;
        double fraction2;
        if (other instanceof Fraction) {
            fraction1 = this.numerator/this.denominator;
            fraction2 = ((Fraction) other).numerator/((Fraction) other).denominator;
            if (fraction1 == fraction2) {
                result = true;
            }
        }
        return result;
    }
    public static int gcd(int numerator, int denominator) {
        int remainder;
        while (numerator != 0 && denominator != 0) {
            remainder = numerator % denominator;
            numerator = denominator;
            denominator = remainder;
        }
        return numerator;
    }
    public void toLowestTerms() {
        int divisor = gcd(numerator, denominator);
        numerator /= divisor;
        denominator /= divisor;
    }
}

