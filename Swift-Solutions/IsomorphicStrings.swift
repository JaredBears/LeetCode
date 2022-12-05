class Solution {
    func isIsomorphic(_ s: String, _ t: String) -> Bool {
        var map = [Character: Character]()
        for i in (0..<s.count){
            if map[s[i]] == nil{
                map[s[i]] = t[i]
            }
            else if map[s[i]] != t[i]{
                return false
            }
        }
        return true
    }
}

extension StringProtocol {
    subscript(offset: Int) -> Character {
        self[index(startIndex, offsetBy: offset)]
    }
}
