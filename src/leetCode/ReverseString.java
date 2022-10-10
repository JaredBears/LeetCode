package leetCode;

/*
 * Write a function that reverses a string. The input string is given as an array of characters s.
 * 
 * You must do this by modifying the input array in-place with O(1) extra memory.
 */

import java.util.Arrays;

public class ReverseString {

  public static void main(String[] args) {
    char[] testOne = {'h', 'e', 'l', 'l', 'o'};
    char[] testTwo = {'H', 'a', 'n', 'n', 'a', 'h'};

    char[] resultOne = {'o', 'l', 'l', 'e', 'h'};
    char[] resultTwo = {'h', 'a', 'n', 'n', 'a', 'H'};

    reverseString(testOne);
    reverseString(testTwo);

    System.out.println(Arrays.equals(testOne, resultOne));
    System.out.println(Arrays.equals(testTwo, resultTwo));
  }

  static void reverseString(char[] s) {
    for (int i = 0, j = s.length - 1; i < j; i++, j--) {
      char temp = s[i];
      s[i] = s[j];
      s[j] = temp;
    }
  }

}
