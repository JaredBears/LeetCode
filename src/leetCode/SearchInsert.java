package leetCode;

/*
 * Given a sorted array of distinct integers and a target value, return the index if the target is
 * found. If not, return the index where it would be if it were inserted in order.
 * 
 * You must write an algorithm with O(log n) runtime complexity.
 */

public class SearchInsert {
  
  public static void main(String[]args) {
    int[] test = {1,3,5,6};
    
    System.out.println(searchInsert(test, 5) == 2);
    System.out.println(searchInsert(test, 2) == 1);
    System.out.println(searchInsert(test, 7) == 4);
  }
  
  static int searchInsert(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;
    if(nums[nums.length - 1] < target){
        return nums.length;
    }
    while (left < right){
        int mid = left + (right - left) / 2;
        if(nums[mid] < target){
            left = mid + 1;
        } else{
            right = mid;
        }
    }
    
    return left;
  }

}
