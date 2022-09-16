#include <stdio.h>
#include <limits.h>
#include<stdlib.h>
int main(void) {
	// your code goes here
	int t;
	scanf("%d",&t);
	while(t--){
	    int x1,y1,x2,y2;
	    scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
	    int a = abs(x1-x2);
	    int b=abs(y1-y2);
	    if(a > b)
	    printf("%d\n",a);
	    else printf("%d\n",b);
	}
	return 0;
}
