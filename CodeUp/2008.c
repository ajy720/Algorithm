//2008 : 오름차순? 내림차순? 2

#include <stdio.h>
#include <stdlib.h>

main(){
	int n, i, flag=0, check=0;
	scanf("%d", &n);
	int *num = (int*)malloc(sizeof(int) * n);
	for(i=0;i<n;i++) scanf("%d", &num[i]);
	
	for(i=0;i<n-1;i++){
		if(num[i] < num[i+1]){flag = 1; break;}
		else if(num[i] > num[i+1]){flag = -1;	break;}
		else continue;
	}
	
	if(flag == 0) {printf("섞임"); return;}
		
	for(i=0;i<n-1;i++){
		if(num[i]<num[i+1]){
			if(flag != 1) break;
			check++;
		}
		else if(num[i]>num[i+1]){
			if(flag != -1) break;
			check++;
		}
		else check++;
	}
	
	if(flag == 1 && check == n-1) printf("오름차순");
	else if(flag == -1 && check == n-1) printf("내림차순");
	else printf("섞임");
	
	
}
