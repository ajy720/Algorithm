//2608 : 동아리 회장 선거

#include <stdio.h>
#include <math.h>

main(){
	int n, i, temp, c;
	char str[8]={0};
	scanf("%d", &n);
	
	for(i=0;i<pow(2,n);i++){
		temp = i;
		c=0;
		while(temp!=0||c<n){
			if(temp%2==0) str[n-1-c]='O';
			else str[n-1-c]='X';
			temp/=2;
			c++;
		}printf("%s\n",str);
	}
}
