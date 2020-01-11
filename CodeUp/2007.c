//2007 : 오름차순? 내림차순? 1

#include <stdio.h>
#include <stdlib.h>

main(){
	int n, i, flag=0;
	scanf("%d", &n);
	int *num = (int*)malloc(sizeof(int) * n);
	for(i=0;i<n;i++) scanf("%d", &num[i]);
	
	for(i=0;i<n-1;i++){
		if(num[i]<num[i+1]) flag++;
		else if(num[i]>num[i+1]) flag--;
	}
	
	if(flag==n-1) printf("오름차순");
	else if(flag==-n+1) printf("내림차순");
	else printf("섞임"); 
}
