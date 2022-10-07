package leetCode;

public class BinarySearch {
  
  /*
   * Given an array of integers nums which is sorted in ascending order, 
   * and an integer target, write a function to search target in nums. 
   * If target exists, then return its index. Otherwise, return -1.
   *
   * You must write an algorithm with O(log n) runtime complexity.
   */

  public static void main(String[] args) {
    int[] nums1 = {-1,0,3,5,9,12};
    int[] nums2 = {-1,0,3,5,9,12};
    System.out.println(search(nums1, 9) == 4); 
    System.out.println(search(nums2, 2) == -1); 

  }

  static int search(int[] nums, int target) {
    return search(nums, target, 0, nums.length - 1);
  }

  static int search(int[] nums, int target, int low, int high) {
    if (low > high) {
      return -1;
    }
    int midIndex = low + (high - low) / 2;
    int mid = nums[midIndex];
    if (mid == target) {
      return midIndex;
    } else if (mid > target) {
      return search(nums, target, low, midIndex - 1);
    } else {
      return search(nums, target, midIndex + 1, high);
    }
  }
}
