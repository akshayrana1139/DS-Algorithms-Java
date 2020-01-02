/*
Question: Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0,

*/


public class Main {
  
  public static void main(String[] args) {
    int M = 4;
    int N = 3;
    // Filling array to use
    int[][] arr = new int[3][3];
    for(int i = 0; i<M; i++){
      for(int j = 0; j<N; j++){
         arr[i][j] = //random filling including 0
      }
    }

    List<int> row = new ArrayList<int>();
    List<int> col = new ArrayList<int>();
    
    // Traversing array to find zeros.. cant make the row/col zero right now, so just storing them.
    for(int i = 0; i<M; i++){
      for(int j = 0; j<N; j++){
         if(arr[i][j] == 0){
            row.add(i);
            col.add(j);
         }
      }
    }

    // Traverse those rows and columns to make them zero.. 
    // if row = 3, for(j:0->N), arr[3][j] = 0
    


