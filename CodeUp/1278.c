//1278 : 자릿수 계산

#include <stdio.h>

main(){
	int a, i=0;
	
	scanf("%d", &a);
	
	while(a!=0){
		
		a/=10;
		i++;
	}
	
	printf("%d", i);
} 