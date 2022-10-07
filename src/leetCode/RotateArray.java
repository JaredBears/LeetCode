package leetCode;

import java.util.Arrays;

/*
 * Given an array, rotate the array to the right by k steps, where k is 
 * non-negative.
 */

public class RotateArray {

  public static void main(String[] args) {
    int[] test1 = {1,2,3,4,5,6,7};
    int[] result1 = {5,6,7,1,2,3,4};
    int[] test2 = {-1,-100,3,99};
    int[] result2 = {3,99,-1,-100};
    rotate(test1, 3);
    rotate(test2, 2);
    System.out.println(Arrays.equals(test1, result1));
    System.out.println(Arrays.equals(test2, result2));
  }

  static void rotate(int[] arr, int k) {
    if (arr.length <= 1) {
      return;
    }
    k = arr.length - (k % arr.length);
    if (k == 0) {
      return;
    }
    reverseArray(arr, 0, arr.length);
    reverseArray(arr, 0, arr.length - k);
    reverseArray(arr, arr.length - k, arr.length);
  }

  static void reverseArray(int[] arr, int start, int end) {
    int i = start;
    int j = end - 1;

    while (i < j) {
      int swap = arr[i];
      arr[i] = arr[j];
      arr[j] = swap;
      i++;
      j--;
    }
  }

}
