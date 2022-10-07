package leetCode;

import java.util.Arrays;

/*
 * Given an integer array nums sorted in non-decreasing order, return an 
 * array of the squares of each number sorted in non-decreasing order.
 */

public class SquaresOfSortedArray {

  public static void main(String[] args) {
    int[] test1 = {-4,-1,0,3,10};
    int[] result1 = {0,1,9,16,100};
    int[] test2 = {-7,-3,2,3,11};
    int[] result2 = {4,9,9,49,121};
    
    System.out.println(Arrays.equals(sortedSquares(test1), result1));
    System.out.println(Arrays.equals(sortedSquares(test2), result2));

  }
  
  static int[] sortedSquares(int[] nums) {
    for(int i = 0; i < nums.length; i++){
        nums[i] *= nums[i];
    }
    Arrays.sort(nums);
    return nums;
}

}
