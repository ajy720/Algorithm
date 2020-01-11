//2016 : 천단위 구분기호

#include <stdio.h>
#include <stdlib.h> 

main(){
	int i,j, n;
	scanf("%d", &n);
	char *num = (char*)malloc(sizeof(char)*(n+67));
	char temp;
	scanf("%s", num);
	
	for(i=n%3;i<strlen(num)&&n>3;i+=4){
		if(i==0) i=3;
		for(j=strlen(num);j>=i;j--){
			temp = num[j];
			num[j]=num[j+1];
			num[j+1]=temp;
		}
		num[i] = ',';
	}
	
	printf("%s", num);
}
