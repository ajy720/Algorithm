//1173 : 30분전

#include <stdio.h>

main(){
	int h, m;
	
	scanf("%d %d", &h, &m);
	
	if(m>=30){
		printf("%d %d", h, m-30);
		return 0;
	}
	else{
		if(h>0){
			printf("%d %d", h-1, m+30);
			return 0;
		}
		else{
			printf("23 %d", m+30);
			return 0;
		}
	}
	
} 
