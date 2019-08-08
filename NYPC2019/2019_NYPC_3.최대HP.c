#include <stdio.h>

main(){
	
	int h, t, i;
	
	scanf("%d %d", &h, &t);
	
	int log[t][2];
	
	for(i=0;i<t;i++) scanf("%d %d", &log[i][0], &log[i][1]);
	
	for(i=0;i<t;i++){
		switch(log[i][0]){
			case 1:
				h-=log[i][1];
				break;
			case 2:
				h+=log[i][1];
				break;
			case 3:
				h+=log[i][1];
				printf("%d", h);
				return 0;				
		}
	}
}
