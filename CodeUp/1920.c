//1920 : (재귀함수) 2진수 변환

#include <stdio.h>

void binary(int a){
	if(a==0) return;
	binary(a/2);
	printf("%d", a%2);
}

main(){
	int a;
	scanf("%d", &a);
	
	if(a==0){
		printf("0");
		return 0;
	}
	
	binary(a);
}