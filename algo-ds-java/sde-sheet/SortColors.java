public class SortColors {
    public static void sortColors(int[] nums) {
        int low = 0;
        int hi = nums.length - 1;
        int mid = 0;
        int temp;

        while (mid <= hi) {
            switch (nums[mid]) {
                case 0: {
                    temp = nums[low];
                    nums[low] = nums[mid];
                    nums[mid] = temp;
                    low++;
                    mid++;
                    break;
                }
                case 1:
                    mid++;
                    break;

                case 2: {
                    temp = nums[mid];
                    nums[mid] = nums[hi];
                    nums[hi] = temp;
                    hi--;
                    break;
                }
            }
        }
    }


    public static void main(String[] args) {
        int[] nums = new int[]{2, 0, 2, 1, 1, 0};
        System.out.println(nums.length);
        sortColors(nums);


        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }
    }
}

