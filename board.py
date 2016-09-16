from copy import deepcopy

class ChessBoard:

    def __init__( self, num_squares ):
        self.n = num_squares
        self.b = []
        for r in range(num_squares):
            self.b.append(['0']*num_squares)

    def set(self, spaces, row = 0, col = 0, value = '0'):
        self.b[row][col] = value
        #print('{}Placed queen at {},{}'.format(spaces, row, col))

    def get(self, row = 0, col = 0):
        return self.b[row][col]

    def fill_row( self, row, fill_value='1' ):
        #Fill all columns in the specified row
        #print('Filling row: {}'.format(row))
        for c in range(self.n):
            if self.b[row][c] == '0': self.b[row][c] = fill_value
        #self.print()

    def fill_column( self, col, fill_value='1' ):
        #Fill all rows in the specified col
        #print('Filling col: {}'.format(col))
        for r in range(self.n):
            if self.b[r][col] == '0': self.b[r][col] = fill_value 
        #self.print()

    def fill_diagonal( self, row=0, col=0, fill_value='1' ):
        #Fill all diagonal cells above row and to left of col
        r=row-1
        c=col-1

        while (r>=0) and (c>=0):
           if self.b[r][c] == '0': self.b[r][c]= fill_value  
           r = r-1
           c = c-1

        #Fill all diagonal cells above row and to the right of col
        r=row-1
        c=col+1

        while (r>=0) and (c<self.n):
           if self.b[r][c] == '0': self.b[r][c]= fill_value  
           r = r-1
           c = c+1

        #Fill all diagonal cells below row and to the left of col
        r=row+1
        c=col-1

        while (r<self.n) and (c>=0):
           if self.b[r][c] == '0': self.b[r][c]= fill_value  
           r = r+1
           c = c-1

        #Fill all diagonal cells to below row and right of col
        r=row+1
        c=col+1

        while (r<self.n) and (c<self.n):
           if self.b[r][c] == '0': self.b[r][c]= fill_value  
           r = r+1
           c = c+1

        #self.print()

    def block_path( self, spaces, block_row=0, block_col=0):
        self.fill_row(block_row)
        self.fill_column(block_col)
        self.fill_diagonal(row=block_row, col=block_col)
        #print(self, spaces)

    def unblock_path( self, block_row=0, block_col=0 ):
        self.fill_row(block_row, fill_value='0')
        self.fill_column(block_col, fill_value='0')
        self.fill_diagonal(row=block_row, col=block_col, fill_value='0')

    def print( self, spaces="", debug=True ):
        for row in range(self.n):
            mod_row = ''.join(self.b[row])
            mod_row = mod_row.replace('2', 'Q')
            if debug == False: mod_row = mod_row.replace('1', '-') 
            print(spaces + mod_row) 

    def convert_board_to_hex( self ):
        hex_string = ""
        for row in range(self.n):
            s = ''.join(self.b[row]).replace('1','0').replace('2','1')
            h = hex(int(s,2)).replace('0x','')
            if len(h) < 2: h = '0' + h
            hex_string = hex_string + h
        return hex_string

    def rotate_board_270( self ):
        new_board = ChessBoard(self.n)
        new_board.b = []
        for c in range(self.n):
            row = []
            for r in range(self.n-1,-1,-1):
                row.append(self.b[r][c])
            new_board.b.append(row)
        return new_board

    def rotate_board_180( self ):
        new_board = ChessBoard(self.n)
        new_board.b = []
        for r in range(self.n-1, -1, -1):
            row = self.b[r][::-1]
            new_board.b.append(row)
        return new_board

    def rotate_board_90( self ):
        new_board = ChessBoard(self.n)
        new_board.b = []
        for c in range(self.n-1, -1, -1):
            row = []
            for r in range(self.n):
                row.append(self.b[r][c])
            new_board.b.append(row)
        return new_board

    def reflect_horizontal( self ):
        new_board = ChessBoard(self.n)
        for r in range(self.n):
            new_board.b[self.n-1-r] = self.b[r]
        return new_board

    def reflect_vertical( self ):
        new_board = ChessBoard(self.n)
        for c in range(self.n):
            row = []
            for r in range(self.n):
                row.append(self.b[r][c])
            new_board.b[self.n-1-c] = row
        return new_board
