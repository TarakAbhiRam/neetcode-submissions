class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int maxi=0;
        int j=0;
        vector<int> ans;
        if(k==1)return nums;
        for(int i=0;i<k;i++){
            maxi=max(maxi,nums[i]);
        }
        ans.push_back(maxi);
        for(int i=k;i<nums.size();i++){
            if(nums[j]!=maxi){
                j++;
                if(nums[i]>=maxi){
                    maxi=nums[i];
                }
            }
            else{
                j++;
                maxi=INT_MIN;
                for(int kk=j;kk<=i;kk++){
                    maxi=max(maxi,nums[kk]);
                }
            }
            ans.push_back(maxi);
        }
        return ans;
    }
};
