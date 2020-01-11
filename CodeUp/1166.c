//1166 : 윤년 판별

#include <stdio.h>

main(){
	int year;
	
	scanf("%d", &year);
	
	if(year%4==0&&year%100!=0||year%400==0) printf("yes");
	else printf("no");
} 