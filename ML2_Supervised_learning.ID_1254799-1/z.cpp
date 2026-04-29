#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>

using namespace std;

typedef vector<vector<char> > Board;

Board createBoard() {
    return Board(3, vector<char>(3, '.'));
}

void printBoard(const Board& board) {
    system("cls");
    cout << "  1 2 3" << endl;
    for (int r = 0; r < 3; r++) {
        cout << (r + 1) << " ";
        for (int c = 0; c < 3; c++) {
            cout << board[r][c];
            if (c < 2) cout << "|";
        }
        cout << endl;
        if (r < 2) cout << "  -----" << endl;
    }
    cout << endl;
}

bool checkWinner(const Board& board, char player) {
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == player && board[i][1] == player && board[i][2] == player)
            return true;
        if (board[0][i] == player && board[1][i] == player && board[2][i] == player)
            return true;
    }
    if (board[0][0] == player && board[1][1] == player && board[2][2] == player)
        return true;
    if (board[0][2] == player && board[1][1] == player && board[2][0] == player)
        return true;
    return false;
}

bool isDraw(const Board& board) {
    for (int r = 0; r < 3; r++)
        for (int c = 0; c < 3; c++)
            if (board[r][c] == '.') return false;
    return true;
}

bool getMove(Board& board, char player) {
    int row, col;
    while (true) {
        cout << "Player " << player << ", enter row and col (1-3): ";
        if (!(cin >> row >> col)) {
            cin.clear();
            cin.ignore(1000, '\n');
            cout << "Invalid input. Try again." << endl;
            continue;
        }
        row--; col--;
        if (row < 0 || row > 2 || col < 0 || col > 2) {
            cout << "Out of range. Try again." << endl;
            continue;
        }
        if (board[row][col] != '.') {
            cout << "Cell is taken. Try again." << endl;
            continue;
        }
        board[row][col] = player;
        return true;
    }
}

void play() {
    while (true) {
        Board board = createBoard();
        char players[2] = {'X', 'O'};
        int turn = 0;

        while (true) {
            printBoard(board);
            char player = players[turn % 2];
            getMove(board, player);

            if (checkWinner(board, player)) {
                printBoard(board);
                cout << "Player " << player << " wins!" << endl;
                break;
            }
            if (isDraw(board)) {
                printBoard(board);
                cout << "Draw!" << endl;
                break;
            }
            turn++;
        }

        cout << "Play again? (y/n): ";
        char again;
        cin >> again;
        if (again != 'y' && again != 'Y') {
            cout << "Goodbye!" << endl;
            break;
        }
    }
}

int main() {
    play();
    return 0;
}