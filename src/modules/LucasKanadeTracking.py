import cv2
import numpy as np
from modules import imread_web

lucasKanade_params = dict(
  winSize = (15,15),
  maxLevel = 2,
  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
)

subpix_params = dict(
  zeroZone = (-1, -1),
  winSize = (10, 10),
  criteria = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, 20, 0.03)
)

feature_params = dict(
  maxCorners = 500,
  qualityLevel = 0.01,
  minDistance = 10
)

class LucasKanadeTracker(object):
	"""
		ピラミッド型Lucas-Kanade法でオプティカルフローを計算するクラス
	"""

	def __init__(self, imnames):
		""" 画像のリストを用いて初期化 """
		self.imnames = imnames
		self.features = []
		self.tracks = []
		self.current_frame = 0


	def detect_points(self):
		""" 現在のフレームの「追跡に適する特徴点」をサブピクセル精度で検出 """
		# 画像を読み込みグレースケール画像を作成
		self.image = imread_web.imread_web(self.imnames[self.current_frame])
		self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

		# 特徴点を検出
		features = cv2.goodFeaturesToTrack(self.gray, **feature_params)

		# コーナー点の座標を改善
		cv2.cornerSubPix(self.gray, features, **subpix_params)
		self.features = features
		self.tracks = [[p] for p in features.reshape((-1, 2))]
		self.prev_gray = self.gray

	
	def track_points(self):
		""" 検出した特徴点を追跡 """
		if self.features != []:
		  self.step() # 次のフレームへ

	  	# 画像を読み込みグレースケール画像を作成
		self.image = cv2.imread(self.imnames[self.current_frame])
		self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

	  	# 入力フォーマットに合うように変換
		tmp = np.float32(self.features).reshape(-1, 1, 2)

	  	# オプティカルフローを計算
		features, status, track_error = cv2.clacOptionalFlowPyrLK(
	  		self.prev_gray,
	  		self.gray,
	  		tmp,
	  		None,
			**lucasKanade_params
		)

		# 消失した点を削除
		self.features = [p for (st, p) in zip(status, features) if st]

		# 消失した点の追跡を消去
		features = np.array(features).reshape((-1, 2))
		for i, f in enumerate(features):
			self.tracks[i].append(f)
		ndx = [i for (i, st) in enumerate(status) if not st]
		ndx.reverse() # 後ろから削除
		for i in ndx:
			self.tracks.pop(i)

		self.prev_gray = self.gray

  
	def step(self, frameNum = None):
		""" 他のフレームへ．引数がなければ次のフレームへ """
		if frameNum is None:
			self.current_frame = (self.current_frame + 1) % len(self.imnames)
		else:
			self.current_frame = frameNum % len(self.imnames)


	def draw(self):
		""" 現在の画像に点を描画 """

		# 緑の縁で特徴点を描画
		for point in self.features:
			cv2.circle(
				self.image,
				(int(point[0][0]), int(point[0][1])),
				3,
				(0, 255, 0),
				-1
			)

			cv2.imshow('LucasKanadeTrack', self.image)
			cv2.waitKey()
