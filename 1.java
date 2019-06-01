class Solution {
	public int[] twoSum(int[] nums, int target) {
		Hashmap<Integer, Integer> m = new Hashmap<Integer, Integer> ();
		int[] res = new int[2];
		for (i=0;i<nums.length;++i) {
			m.put(nums[i],i);
		}
		for (i=0;i<nums.length;++!) {
			t=target-nums[i];
			if (m.containsKey(t) && m.get(t) != i) {
				res[0] = i;
				res[1] = m.get(t);
				break;
			}
		}
		return res;
	}
}