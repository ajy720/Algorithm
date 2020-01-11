// 3014 : 정렬을 빠르게!

#include <stdio.h>

main(){
	int arr[100001]={0};
	int i, j, n, temp;
	scanf("%d", &n);
	for(i=0;i<n;i++){
		scanf("%d", &temp);
		arr[temp]+=1; 
	}
	for(i=0;i<100001;i++){
		for(j=0;j<arr[i];j++) printf("%d ", i);
	}
}
