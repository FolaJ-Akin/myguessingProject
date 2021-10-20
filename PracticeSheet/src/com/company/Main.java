package com.company;

public class Main {

    public static void main(String[] args) {

        byte myByteValue = 82;
        short myShortValue = 22222;
        int myIntegerValue = 7473723;
        long myLongValue = 50000l + 10l *(myByteValue+myShortValue+myIntegerValue);
       // long myLongValue = (long) 50000 + 10*(myByteValue+myShortValue+myIntegerValue);
        System.out.println(myByteValue);
        System.out.println(myShortValue);
        System.out.println(myIntegerValue);
        System.out.println(myLongValue);
    }
}
