import matplotlib.pyplot as plt
from modules import LucasKanadeTracking as lktrack
import cv2

imnames = [
	'https://dl.dropboxusercontent.com/s/jp5nspxniujs8e8/image_mosicing01.png',
	'https://dl.dropboxusercontent.com/s/5z99l7uptqvbicu/image_mosicing02.png',
	'https://dl.dropboxusercontent.com/s/t1zwoq23ko627d6/image_mosicing03.png',
]

# 追跡オブジェクトを生成
lktrackObj = lktrack.LucasKanadeTracker(imnames)

for im, ft in lktrackObj.track():
	print('tracking %d features' % len(ft))

	plt.figure()
	plt.imshow(im)
	for p in ft:
		plt.plot(p[0], p[1], 'bo')
	for t in lktrackObj.tracks:
		plt.plot([p[0] for p in t], [p[1] for p in t])
	plt.axis('off')
	plt.show()