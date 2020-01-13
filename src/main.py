from modules import LucasKanadeTracking as lktrack

imnames = [
	'https://picsum.photos/200/300',
	'https://picsum.photos/200/300',
	'https://picsum.photos/200/300'
]

# 追跡オブジェクトを生成
lktrackObj = lktrack.LucasKanadeTracker(imnames)

# 最初のフレームで特徴点を検出し残りのフレームで追跡
lktrackObj.detect_points()
lktrackObj.draw()
for i in range(len(imnames) - 1):
	lktrackObj.track_points()
	lktrackObj.draw()