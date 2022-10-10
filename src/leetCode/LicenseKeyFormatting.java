package leetCode;

import java.util.Stack;

/*
 * You are given a license key represented as a string s that consists of only alphanumeric
 * characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given
 * an integer k. We want to reformat the string s such that each group contains exactly k
 * characters, except for the first group, which could be shorter than k but still must contain at
 * least one character. Furthermore, there must be a dash inserted between two groups, and you
 * should convert all lowercase letters to uppercase. Return the reformatted license key.
 */

public class LicenseKeyFormatting {

  public static void main(String[] args) {
    System.out.println(licenseKeyFormatting("5F3Z-2e-9-w", 4).equals("5F3Z-2E9W"));
    System.out.println(licenseKeyFormatting("2-5g-3-j", 2).equals("2-5G-3J"));
    

  }

  static String licenseKeyFormatting(String s, int k) {
    char[] array = s.toCharArray();
    Stack<Character> stack = new Stack<Character>();
    StringBuilder sb = new StringBuilder();
    for (char c : array) {
      if (c != '-') {
        stack.add(Character.toUpperCase(c));
      }

    }
    for (int i = 1; i <= array.length; i++) {
      if (!stack.isEmpty())
        sb.insert(0, stack.pop());
      if (i % k == 0 && !stack.isEmpty()) {
        sb.insert(0, '-');
      }
    }

    return sb.toString();
  }
}
