class NQueens {
  private int N; // Board size (N x N)
  private int[] queens; // Stores column positions of queens
  private boolean[] column, diag1, diag2; //Attack constraints

  public NQueens(int n) {
    N = n;
    queens = new int[N];
    column = new boolean[N];
    diag1 = new boolean[2 * N - 1];
    diag2 = new boolean[2 * N - 1];
  }
  // Function to solve N-Queens
  public void solve() {
    placeQueen(0);
  }
  // Backtracking function to place queens
  private void placeQueen(int row) {
    if (row == N) {
      printSolution();
      return;
    }
    for (int col = 0; col < N; col++) {
      if (!column[col] && !diag1[row - col + N - 1] && !diag2[row + col]) {
        // Place Queen
        queens[row] = col;
        column[col] = diag1[row - col + N - 1] = diag2[row + col] = true;
        placeQueen(row + 1); // Recurse for next row
        // Backtrack: Remove Queen
        column[col] = diag1[row - col + N - 1] = diag2[row + col] = false;
      }
    }
  }

  // Function to print board
  private void printSolution() {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        System.out.print((queens[i] == j ?
        "Q " : ". "));
      }
      System.out.println();
    }
    System.out.println();
  }
    // Main method to run the program
    public static void main(String[] args) {
    int n = 4; // Change N for different board sizes
    NQueens q = new NQueens(n);
    q.solve();
  }
}