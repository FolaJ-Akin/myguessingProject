package com.company;

public class Main {

    public static void main(String[] args) {

        int myvalue = 10000;
        // int vs integer. Integer is a wrapper class, it gives us a way to preform operations on an int
        // all 8
        int myMinIntValue = Integer.MIN_VALUE;
        int myMaxIntValue = Integer.MAX_VALUE;
        System.out.println("Integer Minimum Value = " + myMinIntValue);
        System.out.println("Integer Maximum Value = " + myMaxIntValue);
        System.out.println("Busted max Value = " + (myMaxIntValue + 1)); // you get an Overflow, skips to the minimum number
        System.out.println("Busted MIN value = " + (myMinIntValue - 1)); // you get an underflow, skips to the maximum number
        int myMAXintTest = 2_147_483_647; // you can use '_' to separate out integer values

        byte myMINByteValue = Byte.MIN_VALUE;
        byte myMAXbyteValue = Byte.MAX_VALUE;
        System.out.println("Byte Minimum Value = " + myMINByteValue); // Byte is made of 8 bits
        System.out.println("Byte Maximum Value = " + myMAXbyteValue);

       short myMINShortValue = Short.MIN_VALUE;
       short myMAXShortValue = Short.MAX_VALUE;
        System.out.println("Short Minimum Value = " + myMINShortValue); // short has 16 bits
        System.out.println("Short Maximum Value = " + myMAXShortValue);

        long myLongValue = 100L; // L after the number to denote long n.o with 64 bits; double of an integer bit - 32 bits
        long myMINLongValue = Long.MIN_VALUE;
        long myMAXLongValue = Long.MAX_VALUE;
        System.out.println("Long Minimum Value = " + myMINLongValue); // does have underflow
        System.out.println("Long Maximum Value = " + myMAXLongValue); // does have overflow
        // Casting

        byte myNewByteValue =(byte) (myMINByteValue / 2);
        short myNewShortValue = (short) (myMINShortValue / 2 );
        System.out.println(myNewByteValue);
        System.out.println(myNewShortValue);
    }
}
