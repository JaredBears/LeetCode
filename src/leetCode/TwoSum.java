package leetCode;

import java.util.*;

public class TwoSum {
    public static void main(String[] args) {
        int[] nums = new int[] {3,3};
        int target = 6;
        System.out.println(Arrays.toString(twoSum(nums, target)));
    }

    public static int[] twoSum(int[] nums, int target) {
        int[] solution = new int[2];
        for(int i = 0; i < nums.length; i++) {
            for(int k = 0; k < nums.length; k++) {
                if(i != k) {
                    if(nums[i] + nums[k] == target) {
                        solution[1] = i;
                        solution[0] = k;
                    }
                }
            }
        }
        return solution;
    }
}
