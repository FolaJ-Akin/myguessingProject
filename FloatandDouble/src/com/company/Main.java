package com.company;

public class Main {

    public static void main(String[] args) {
	// Precision refers to the format and the amount of space occpiced by the type.
        // single precision occupies 32 bits (so width 32)
        // Double precision occupies 64 bits ( so width is 64)
        float myMinFloatValue = Float.MIN_VALUE;
        float myMaxFloatValue = Float.MAX_VALUE;
        System.out.println("Float minimum value =" + myMinFloatValue);
        System.out.println("Float maximum value =" + myMaxFloatValue);

        double myMinDoubleValue = Double.MIN_VALUE;
        double myMaxDoubleValue = Double.MAX_VALUE;
        System.out.println("Double minimum value =" + myMinDoubleValue);
        System.out.println("Double maximum value =" + myMaxDoubleValue);

        int myIntValue = 5/3; // ans=2 because it can't have reminders; it rounds down
        float myFloatValue = 5f/ 3f;//f to declare variable
        double myDoubleValue = 5.00/ 3.00; //double is the default - 16 decimal places
        System.out.println("MyIntValue= " + myIntValue);
        System.out.println("MyFloatValue= " + myFloatValue);
        System.out.println("MyDoubleValue= " + myDoubleValue);

        int KilogramValue = 5;
        double PoundConv = KilogramValue / 0.45359237;
        System.out.println(KilogramValue + " kilograms converted to pounds is " + PoundConv);

    }
}
