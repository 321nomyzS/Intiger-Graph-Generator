#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#include <lapacke.h>

//gcc -o program.out program.c -llapacke -lblas -lm
int triangle;

void decimalToBinary(long long num, int* binaryArray, int size) {
    int index = size - 1;
	
    for(int i=0; i<size; i++){
    	binaryArray[i] = 0;
    }
    while (num > 0) {
        binaryArray[index] = num % 2;
        num /= 2;
        index--;
    }
}

double** generateMatrix(int* binaryArray, int size) {
    double** matrix = (double**)malloc(size * sizeof(double*));
    for (int i = 0; i < size; i++) {
        matrix[i] = (double*)malloc(size * sizeof(double));
    }
    for (int i = 0; i < size; i++){
    	matrix[i][i] = 0.0f;
    }
    int k = 0;
    for (int i = 0; i < size; i++) {
        for (int j = i + 1; j < size; j++) {
            matrix[i][j] = (double)binaryArray[k];
            matrix[j][i] = (double)binaryArray[k];
            k++;
        }
    }

    return matrix;
}

void printMatrix(double** matrix, int size) {
    printf("Macierz:\n");
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            printf("%lf ", (int)matrix[i][j]);
        }
        printf("\n");
    }
}

double* transforMatrixToLine(double** matrix, int size){
    double* resultLine = (double*)malloc(size*size * sizeof(double));
    
    int k = 0;
    for(int i = 0; i < size; i++)
    {
        for(int j = 0; j < size; j++)
        {
            resultLine[k++] = matrix[i][j];
        }
    }

    return resultLine;
}

void checkEigenvalues(long long matrixNumber, int size){
    int* binaryArray = (int*)malloc(triangle * sizeof(int));
	decimalToBinary(matrixNumber, binaryArray, triangle);

    double** matrix = generateMatrix(binaryArray, size);
	double* matrixLine = transforMatrixToLine(matrix, size);

    double wr[size], wi[size], vl[size*size], vr[size*size];
    int lda = size, ldvl = size, ldvr = size, info;
    info = LAPACKE_dgeev(LAPACK_ROW_MAJOR, 'N', 'N', size, matrixLine, lda, wr, wi, vl, ldvl, vr, ldvr);

    for (int i = 0; i < size; i++) {free(matrix[i]);}
	free(matrix);
	free(binaryArray);
    free(matrixLine);
    
    for(int i = 0; i < size; i++)
    {
        if(wi[i] != 0) // wartość własna ma część urojoną, więc nie jest całkowita
        {
            return;
        }
        else
        {
            int val = (int)wr[i]; // rzutowanie wartości własnej na int
            double diff = wr[i] - val; // różnica między wartością rzeczywistą a całkowitą

            if(diff > 0.0001 || diff < -0.0001) // różnica jest większa niż margines błędu
            {
                return;
            }
        }
    }
    
    printf("%ld | ", matrixNumber);
    for(int i = 0; i < size; i++){
        printf("%d ", (int)wr[i]);
    }
    printf("\n");
}

int main(int argc, char *argv[]) {
	int N = atoi(argv[1]);	
	int numThreads = atoi(argv[2]);
	
	triangle = N * (N - 1) / 2;
	long long number_of_iterations = pow(2, triangle);
	long long chunkSize = number_of_iterations / numThreads;

	#pragma omp parallel num_threads(numThreads)
	{
		int threadID = omp_get_thread_num();
        	long long start = (long long)threadID * chunkSize;
        	long long end = start + chunkSize;
		for (long long i = start; i < end; i++) {
            checkEigenvalues(i, N);
		}
	}
}