//1907 : 우박수 길이(3n+1)(small)

#include <stdio.h>

main(){
	int i, j, n, c, leng=1, short_num=1, a, b;
	
	scanf("%d %d", &a, &b);
	
	for(i=b;i>=a;i--){
		n=i;
		c=1;
		while(n!=1){
			c++;
			if(n%2==0) n/=2;
			else n = n*3+1;
		}
		if(leng <= c){
			leng = c;
			short_num = i;
		}
	}
	
	printf("%d %d", short_num, leng);

} 