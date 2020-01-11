//3002 : 기억력 테스트 3

#include <stdio.h>
#include <stdlib.h>

main(){
	int n, m;
	scanf("%d", &n);
	
	int i,j, *str, *test;
	str = (int*)malloc(sizeof(int)*n);
	
	for(i=0;i<n;i++) scanf("%d", (str+i));
	
	scanf("%d", &m);
	test = (int*)malloc(sizeof(int)*m);
	for(i=0;i<m;i++) scanf("%d", (test+i));
	
	int h, l, mid;
	
	for(i=0;i<m;i++){
		l=0;
		h=n;
		
		while(1){
			
			mid = (int)(l+h)/2;
			
			if(str[mid] == test[i]){
				printf("%d ", mid+1);
				break;
			}
			
			else if(str[mid] > test[i]) h = mid;
			else l = mid+1;
			
			if(h<=l){
				printf("-1 ");
				break;
			}
		}
	}	
	
	
}
