#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--){
	    int x,y,d;
	    scanf("%d %d %d",&x,&y,&d);
	    if(x>=y){
	        if(x-y > d)
	            printf("NO\n");
	        else printf("YES\n");
	    }
	    else{
	        if(y-x > d)
	            printf("NO\n");
	        else printf("YES\n");
	    }
	}
	return 0;
}
