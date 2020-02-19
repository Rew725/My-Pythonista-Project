from scene import *
from GameMenu import *
A = Action

class Othello (Scene):
	'''
	リバーシのゲームの処理をするクラス
	'''
	# black=1 white=2
	placing_piece=[]
	can_placing_piece=[]
	turn = 1
	
	
	def setup(self):
		#アプリ起動時
		self.background_color = "white"
		self.new_game()
		self.pause_button = SpriteNode('iob:ios7_pause_32', position=(32, self.size.h-32), parent=self)
		self.show_start_menu()

	def new_game(self):
		# 変数、配列の初期化
		global placing_piece, turn
		turn = 1
		placing_piece=[
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]]
		placing_piece[3][4]=2
		placing_piece[4][3]=2
		placing_piece[3][3]=1
		placing_piece[4][4]=1	

	def count_piece(self,color):
		#石の数を数える
		global placing_piece
		count=0
		for i in range(8):
			for j in range(8):
				if placing_piece[i][j] == color:
					count+=1
		return count

	def count_can_put(self,turn):
		#おける石の数を数える
		global can_placing_piece,placing_piece
		can_placing_piece=[
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]]
		put = 0
		for i in range(8):
			for j in range(8):
				if placing_piece[i][j] == 0:
					if self.can_put(i,j,turn):
						can_placing_piece[i][j] = 1
						put+=1
		return put
			
	def get_win_color(self):
		# 勝敗を求める
		count_black = self.count_piece(1)
		count_white = self.count_piece(2)
		if count_black == count_white:
			return "DRAW ({},{})".format(count_black,count_white)
		elif count_black > count_white:
			return "BLACK WIN!! ({},{})".format(count_black,count_white)
		else:
			return "WHITE WIN!! ({},{})".format(count_black,count_white)

	def can_put(self,x,y,turn):
		# 置こうとした石が置けるかどうか
		global placing_piece
		enemy=0
		if turn ==1:
			enemy=2
		else:
			enemy=1
		go_x=[-1,0,1]
		go_y=[-1,0,1]
		for i in go_x:
			for j in go_y:
				if i == j == 0:
					continue
				if x+i<0 or 8<= x+i or y+j<0 or 8<=y+j:
					continue				
				if placing_piece[x+i][y+j]==enemy:
					hogex=x+i
					hogey=y+j
				else:
					continue
				while 0<=hogex<8 and 0<=hogey<8 and placing_piece[hogex][hogey] == enemy:
					hogex+=i
					hogey+=j
				if hogex<0 or 8<= hogex or hogey<0 or 8<=hogey:
					continue
				if placing_piece[hogex][hogey] == turn:
					return True
		return False

	def reverse(self,x,y,turn):
		# 石の反転処理
		global placing_piece
		enemy=0
		if turn ==1:
			enemy = 2
		else:
			enemy = 1
		go_x=[-1,0,1]
		go_y=[-1,0,1]
		for i in go_x:
			for j in go_y:
				if i == j == 0:
					continue
				if x+i<0 or 8<= x+i or y+j<0 or 8<=y+j:
					continue				
				if placing_piece[x+i][y+j]==enemy:
					hogex=x+i
					hogey=y+j
				else:
					continue
				while 0<=hogex<8 and 0<=hogey<8 and placing_piece[hogex][hogey] == enemy:
					hogex+=i
					hogey+=j
				if hogex<0 or 8<= hogex or hogey<0 or 8<=hogey:
					continue
				if placing_piece[hogex][hogey] == turn:
					hogex -= i
					hogey -= j
					while placing_piece[hogex][hogey]==enemy:
						placing_piece[hogex][hogey] = turn
						hogex-=i
						hogey-=j

	def did_change_size(self):
		self.pause_button.position = (32,self.size[1]-32)
	
	def draw(self):
		global placing_piece,turn,can_placing_piece
		a=min(self.size[0]-100,self.size[1]-100) / 8
		mi=min(self.size[0],self.size[1])
		background(1, 1, 1)
		fill(1,1,1)
		stroke("black")
		stroke_weight(2)
		#drawing field
		aa=(max(self.size[0],self.size[1])-min(self.size[0],self.size[1])) / 2
		for i in range(9):
			b = a * i
			if mi == self.size[0]:
				line(b+50,aa+50,b+50,self.size[1]-aa-50)		
				line(50,b+aa+50,self.size[0]-50,b+aa+50)
			if mi == self.size[1]:
				line(aa+50,b+50,self.size[0]-aa-50,b+50)		
				line(b+aa+50,50,b+aa+50,self.size[1]-50)
		for i in range(8):
			for j in range(8):
				if placing_piece[i][j] == 1:
					fill(0,0,0)
					if mi == self.size[0]:
						ellipse(a*i+50,a*j+aa+50,a,a)

					if mi == self.size[1]:
						ellipse(a*i+50+aa,a*j+50,a,a)
											
				if placing_piece[i][j] == 2:
					fill(1,1,1)
					if mi == self.size[0]:
						ellipse(a*i+50,a*j+aa+50,a,a)

					if mi == self.size[1]:
						ellipse(a*i+50+aa,a*j+50,a,a)
						
		# draw text
		T=["","黒","白"]
		tint(0,0,0,1)
		if mi == self.size[0]:
			text('{}の番'.format(T[turn]), font_name='Hiragino Maru Gothic ProN', font_size=32.0, x=self.size[0]/3, y=self.size[1]-32, alignment=5)
			text('(黒,白)=({},{})'.format(self.count_piece(1),self.count_piece(2)), font_name='Hiragino Maru Gothic ProN', font_size=32.0, x=self.size[0]/3*2, y=self.size[1]-32, alignment=5)

		if mi == self.size[1]:
			text('{}の番'.format(T[turn]), font_name='Hiragino Maru Gothic ProN', font_size=32.0, x=self.size[0]/3, y=self.size[1]-32, alignment=5)
			text('(黒,白)=({},{})'.format(self.count_piece(1),self.count_piece(2)), font_name='Hiragino Maru Gothic ProN', font_size=32.0, x=self.size[0]/3*2, y=self.size[1]-32, alignment=5)
		
		self.count_can_put(turn)
		for i in range(8):
			for j in range(8):
				if can_placing_piece[i][j] == 1:
					if turn ==1:
						fill("lightblue")
					if turn == 2:
						fill("pink")
					no_stroke()
					if mi == self.size[0]:
						ellipse(a*i+50,a*j+aa+50,a,a)

					if mi == self.size[1]:
						ellipse(a*i+50+aa,a*j+50,a,a)

	def show_start_menu(self):
		self.paused = True
		self.menu = Game_Menu('othello', '', ['Play','End'])
		self.present_modal_scene(self.menu)

	def show_pause_menu(self):
		self.paused = True
		self.menu = Game_Menu('othello', 'pause', ['Continue','New Game','End'])
		self.present_modal_scene(self.menu)

	def show_result_menu(self,win_color):
		self.paused = True
		self.menu = Game_Menu('othello', '{}'.format(win_color), ['New Game','End'])
		self.present_modal_scene(self.menu)
			
	def menu_button_selected(self, title):
			self.dismiss_modal_scene()
			self.menu = None
			self.paused = False
			if title in ('New Game', 'Play'):
				self.new_game()
			elif title in ('End'):
				self.view.close()
		
	def touch_ended(self, touch):
		global turn
		global placing_piece
		x,y=touch.location
		if x < 48 and y > self.size.h - 48:
			self.show_pause_menu()
		a=min(self.size[0]-100,self.size[1]-100) / 8		
		mi=min(self.size[0],self.size[1])
		aa=(max(self.size[0],self.size[1])-min(self.size[0],self.size[1])) / 2
		if mi == self.size[0]:
			x=int((touch.location[0]-50)/a)
			y=int((touch.location[1]-aa-50)/a)
			if not(0<=x<8 and 0<=y<8):
				return
			if turn == 1 and placing_piece[x][y]==0 and self.can_put(x,y,turn):
				self.reverse(x,y,turn)
				placing_piece[x][y]=1
				turn = 2
			if turn == 2                                                                                                                                                                    and placing_piece[x][y]==0  and self.can_put(x,y,turn):
				self.reverse(x,y,turn)
				placing_piece[x][y]=2
				turn = 1
		if mi == self.size[1]:
			x=int((touch.location[0]-aa-50)/a)
			y=int((touch.location[1]-50)/a)
			if not(0<=x<8 and 0<=y<8):
				return
			if turn == 1 and placing_piece[x][y]==0 and self.can_put(x,y,turn):
				self.reverse(x,y,turn)
				placing_piece[x][y]=1
				turn = 2
			if turn == 2 and placing_piece[x][y]==0 and self.can_put(x,y,turn):
				self.reverse(x,y,turn)
				placing_piece[x][y]=2
				turn = 1
		if self.count_can_put(1) == 0 and self.count_can_put(2) == 0:
			self.show_result_menu(self.get_win_color())
		else:
			if self.count_can_put(turn) == 0:
				if turn == 1:
					turn = 2
				elif turn == 2:
					turn = 1
		
if __name__ == '__main__':
	run(Othello(), show_fps=False)
