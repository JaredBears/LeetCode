/*
* Given an array of integers temperatures represents the daily temperatures,
* return an array answer such that answer[i] is the number of days you have to
* wait after the ith day to get a warmer temperature. If there is no future day
* for which this is possible, keep answer[i] == 0 instead.
*/

package leetCode;

import java.util.Arrays;
import java.util.Stack;

public class DailyTemperatures {

  public static void main(String[] args) {
    int[] testArray = {73, 74, 75, 71, 69, 72, 76, 73};
    int[] testArrayTwo = {30,40,50,60};
    int[] testArrayThree = {30,60,90};
    System.out.println(Arrays.toString(dailyTemperatures(testArray)));
    System.out.println(Arrays.toString(dailyTemperatures(testArrayTwo)));
    System.out.println(Arrays.toString(dailyTemperatures(testArrayThree)));
  }

  static int[] dailyTemperatures(int[] temperatures) {
    int[] answer = new int[temperatures.length];
    Stack<Integer> stack = new Stack<Integer>();

    for (int i = 0; i < temperatures.length; i++) {
      while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
        int prev = stack.pop();
        answer[prev] = i - prev;
      }
      stack.add(i);
    }
    return answer;
  }

}
