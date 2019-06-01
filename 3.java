class Solution {
	public int lengthOfLongestSubstring(String s) {
		int start = 0;
		int end = 0;
		int res = 0;
		int len = s.length();
		Map<Character, Integer> newMap = new HashMap<> ();

		for (end = 0; end < len; end++) {
			if (newMap.containsKey(s.charAt(end))) {
				start=Math.max(start,newMap.get(s.charAt(end))+1);
			}
			newMap.put(s.charAt(end),end);
            res=Math.max(res, end-start+1);
            //System.out.print("start: "+start+"end "+end);
            //System.out.println("res "+res);
		}
		return res;
	}
}