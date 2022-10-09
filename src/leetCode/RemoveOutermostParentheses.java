package leetCode;

/*
 * A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid
 * parentheses strings, and + represents string concatenation.
 * 
 * For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings. A valid
 * parentheses string s is primitive if it is nonempty, and there does not exist a way to split it
 * into s = A + B, with A and B nonempty valid parentheses strings.
 * 
 * Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk,
 * where Pi are primitive valid parentheses strings.
 * 
 * Return s after removing the outermost parentheses of every primitive string in the primitive
 * decomposition of s.
 */

public class RemoveOutermostParentheses {

  public static void main(String[] args) {
    System.out.println(removeOuterParentheses("(()())(())").equals("()()()"));
    System.out.println(removeOuterParentheses("(()())(())(()(()))").equals("()()()()(())"));
    System.out.println(removeOuterParentheses("()()").equals(""));
  }
  
  static String removeOuterParentheses(String s) {
    StringBuilder sb = new StringBuilder();
    int opened = 0;
    for(char c : s.toCharArray()){
        if(c == '(' && opened++ > 0){ //removes the first opened
            sb.append(c);
        } else if(c == ')' && opened-- > 1){ //removes the last closed
            sb.append(c);
        }
    }
    return sb.toString();
  }

}
