#include<stdio.h>
#include<string.h>
#define DEST_DATE 4
#define MAX
#define INDEX 1
#define VALUE 0
#define DEFAULT_LENGTH 1024 * 6
typedef struct date_index{
	char value[31];
	char index;
	
}date_index;
unsigned long long moveFPLine(FILE *p , int n){
	char tmp[DEFAULT_LENGTH];
	int i;
	for(i=0 ; i<n ; i++)
		fgets(tmp,DEFAULT_LENGTH,p);
	return ftell(p);
}
void getdate(char *c , FILE *p){
	int i;
	for(i=0 ; i<DEST_DATE ; i++)
		fscanf(p,"%s",c);
	
	return;
}
int popPQ(date_index PQ[], int PQ_P){
	
	return PQ[PQ_P].index;
}
void pushPQ(date_index PQ[], int PQ_tail, int PQ_head , char* date , int n_i){
	
	strcpy(PQ[PQ_tail].value , date);
	PQ[PQ_tail].index = n_i;
	int tmpi,i;
	char tmps[31];
	
	if( PQ_tail <= PQ_head ) PQ_tail += (10+1);
	
	for(i = PQ_tail ; i> PQ_head ; i--){
		int ti = i % (10+1);
		int j= (i-1) % (10+1);
		if( strcmp(PQ[ti].value , PQ[j].value) < 0 ){
			//change
			strcpy(tmps,PQ[ti].value);
			strcpy(PQ[ti].value,PQ[j].value);
			strcpy(PQ[j].value,tmps);
			
			tmpi = PQ[ti].index;
			PQ[ti].index = PQ[j].index;
			PQ[j].index = tmpi;
		}
		else{
			break;
		}
	}
}




int main(){
	
	char tmp[DEFAULT_LENGTH];
	char date[31];
	unsigned long long datei[10]={0};
	int times=1,i;
	int debug=1;
	int ck[10+1]={0};
	unsigned long long headLine[10]={0};
	unsigned long long endLine[10]={0};
	int minI=0;
	date_index priorQ[10+1];  // round Q로 구성 시도 해보자 
	int priorQ_tail=0;
	int priorQ_head=0;
	
	
	
	FILE *tp = fopen("ol_cdump_2020-11-30_001.txt","r");
	FILE *fp ;
	
	if(tp == NULL){
		printf("check data");
		return 0;
	}
	fclose(tp);
	
	tp = fopen("temp.txt","w");
	fp = fopen("ol_cdump_2020-11-30_001.txt","r");
	
	
	
	do{
		
		//priorQ 선행 작업 
		for(i=0 ; i<10 ; i++){
			//memset(date,0,sizeof(date));
			//if(ck[i]) break;
			fseek(fp,0,SEEK_SET);
			headLine[i] = moveFPLine(fp,i*times) ;
			endLine[ (i+9)%10 ] = headLine[i]-1; // index underflow 방지
	
			//if( feof(fp) ) ck[i+1] = 1;
			printf("AAAAAA!!!!!!!!!!!");
			
			getdate(date,fp);
			printf("\n%s\n",date);
			pushPQ( priorQ , priorQ_tail++ , priorQ_head , date , i);
			if(priorQ_tail > 10) priorQ_tail %= 10+1;
		}
		endLine[9] = ftell(fp)-1;
		for(i=0 ; i<10 ; i++){
			printf("%d range : %d ~ %d\n",i,headLine[i],endLine[i]);
		}
		
		while(priorQ_tail != priorQ_head){
			
			minI=popPQ(priorQ,priorQ_head++);
			if(priorQ_head > 10) priorQ_head%=10+1;
			
			fseek(fp, headLine[minI] ,SEEK_SET);
			fgets(tmp,DEFAULT_LENGTH,fp);
			/*
			printf("index : %d\n",minI);
			printf("head : %d\n",priorQ_head);
			printf("tail : %d\n",priorQ_tail);
			printf("\n\ntest\n%s\n\n",tmp);
			*/
			fprintf(tp,"%d : %s",debug,tmp);
			if( !feof(fp) && ftell(fp) < endLine[minI] ){
				printf("\n%d %d   %d\n",ftell(fp),endLine[minI],minI);
				printf("\n!!debug %d !!\n\n",debug++);
				headLine[minI] = ftell(fp);
				pushPQ( priorQ , priorQ_tail++ , priorQ_head , date , i);
				if(priorQ_tail > 10) priorQ_tail %= 10+1;	
			}
		}
		times*=10;
	}while(0);
	
	fclose(tp);
	fclose(fp);
	
}
