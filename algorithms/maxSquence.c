#include<stdio.h>

int main()
{
    int arr[] = {0,-3,6,8,-20,21,8,-9,10,-1,3,6,5};//定义序列
    int max = arr[0];//存储最大值，初始化为arr[0]
    int temp = 0;//用于存储子序列之和
    int size = sizeof(arr) / sizeof(int);//数组大小

    //分别从每个元素开始
    for(int i = 0;i < size; i++)
    {
        temp = 0;
        //不同结尾的子序列
        for(int j = i; j < size; j++)
        {
            temp += arr[j];
            if(temp > max)
            {
                max = temp;
            }
        }
    }
    printf("%d\n",max);
    return 0;
}
