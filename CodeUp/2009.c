//2009 : 아메리카노

#include <stdio.h>

main(){
	int k, n, cf=0;
	
	scanf("%d %d", &k, &n);
	
	while(k>=n){
		cf += k/n;
		k = k%n+k/n;
	}
	
	printf("%d", cf);
}
