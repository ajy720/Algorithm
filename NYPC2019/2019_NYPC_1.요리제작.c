#include <stdio.h>

main(){
	int n, i, cnt=0;
	scanf("%d", &n);
	int *mat, *rest;
	
	rest = malloc(sizeof(int)*n);
	mat = malloc(sizeof(int)*n);
	
	for(i=0;i<n;i++) scanf("%d", &rest[i]);
	
	for(i=0;i<n;i++) scanf("%d", &mat[i]);
	
	while(1){
		for(i=0;i<n;i++){
			rest[i]-=mat[i];
			if(rest[i]<0){
				printf("%d", cnt);
				return 0;
			}
		}
		cnt++;
	}
}
