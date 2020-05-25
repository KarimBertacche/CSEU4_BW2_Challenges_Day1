var containsDuplicate = function(nums) {
    let dupObj = {};
    for(idx in nums) {
        if(nums[idx] in Object.keys(dupObj)) {
            return console.log(true);
        } else {
            let num = nums[idx]
            dupObj[num] = 1;
        }
    }
    return console.log(false);
}