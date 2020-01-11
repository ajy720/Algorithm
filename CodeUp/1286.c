//1286 : 최댓값, 최솟값

#include <stdio.h>

main(){
	int max, min, a[5], i;
	
	for(i=0;i<5;i++) scanf("%d", &a[i]);
	max = a[0];
	min = a[0];
	
	for(i=1;i<5;i++){
		if(a[i]>=max) max = a[i]; 
		if(a[i]<=min) min = a[i];
	}
	
	printf("%d\n%d", max, min);
	
}