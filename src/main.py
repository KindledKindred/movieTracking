import matplotlib.pyplot as plt
from modules import LucasKanadeTracking as lktrack
import cv2

imnames = [
	'https://dl.dropboxusercontent.com/s/qprc4fgzafwc3gt/20200114_133503_001%20%28edited-Pixlr%29.jpg',
	'https://dl.dropboxusercontent.com/s/qjfmp2ucuckelqf/20200114_133503_002%20%28edited-Pixlr%29.jpg',
	'https://dl.dropboxusercontent.com/s/gmrexcfll4jc9nr/20200114_133503_003%20%28edited-Pixlr%29.jpg',
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