//1411 : 빠진 카드
#include <stdio.h>
#include <stdlib.h>

main(){
	int i, n, temp;
	
	scanf("%d", &n);
	int list[51]={0};
		
	for(i=0;i<n-1;i++){
		scanf("%d", &temp);
		list[temp-1]=1;
	}
	
	for(i=0;i<n;i++){
		if(list[i]==0){
			printf("%d", i+1);
			return 0;
		}
	}
	
} 