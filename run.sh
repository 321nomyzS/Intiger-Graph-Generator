gcc ./Graph_Generator/graph.c -o output.exe -fopenmp -lm -llapacke -lblas
./output.exe $1 $2 > ../output.txt
python3 ./Graph_Processing/main.py
