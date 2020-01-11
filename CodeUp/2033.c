//2033 : 사다리 게임

#include <stdio.h>
#include <stdlib.h>

main(){
	int t, k, n, i=0, j, p;
	scanf("%d %d", &k, &n);
	int **line= (int**)malloc(sizeof(int*) * n);
	for(i=0;i<n;i++) *(line+i) = (int*)malloc(sizeof(int)*2);

	for(i=0;i<n;i++) scanf("%d %d", &line[i][0], &line[i][1]);
	
	scanf("%d", &p);
	i=0;
	while(i<n){
		if(line[i][0]==p) p = line[i][1];
		else if(line[i][1]==p) p = line[i][0];
		
		i++;
	}
	
	printf("%d", p);
	
	
}
