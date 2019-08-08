#include <stdio.h>
#include <string.h>

main(){
	int n, flag=0, i, j;
	scanf("%d", &n);
	
	char email[n][200];
	for(i=0;i<n;i++) scanf("%s", email[i]);
	
	int res[n], tmp;
	for(i=0;i<n;i++){
		res[i]=0;
		flag=0;
		tmp=0;
		for(j=0;j<strlen(email[i]);j++) if(email[i][j]=='@'){
			 tmp++;
			 if(j==0||j==strlen(email[i])-1){
			 	 flag=1;
			 	 break;
			 }
		}
		if(tmp==0||tmp>1||flag==1) continue;
		
		tmp=0;
		for(j=0;j<strlen(email[i]);j++){
			if((email[i][j]>='A'&&email[i][j]<='Z')||(email[i][j]>='a'&&email[i][j]<='z')||(email[i][j]>='0'&&email[i][j]<='9')||email[i][j]=='-'||email[i][j]=='.'||email[i][j]=='@');
			else{
				res[i]=0;
				flag=1;
				break;
			}
			tmp++;
		}if(tmp==0) flag = 1;
		if(flag==0) res[i]=1;
	}
	
	for(i=0;i<n;i++){
		if(res[i]==1) printf("Yes\n");
		else printf("No\n");
	}
}
