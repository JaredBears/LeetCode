class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var answer: [Int] = []
        for i in (0..<nums.count){
            for j in (i+1..<nums.count){
                if nums[i] + nums[j] == target{
                    answer = [i, j]
                    break
                }
            }
        }
        return answer
    }
}
