"""
Emooc 1.0

developers = ('Ye Zhanyuan', 'Li Yuanhan', 'Liu Xuting', 'Shen Tingwei') 
UIUC, Berkeley = developers[0], developers[1:]
Built with Azure, OpenCV, and Matplotlib
Created at Cal Hacks 6.0
"""

from face_detect import analyze_image
from camera_capture import capture_image
import matplotlib.pyplot as plt

'''Ask for input'''
total_time = int(input("total time in seconds: "))
assert total_time >= 15, "Time need to be at least 15 seconds"
assert total_time <= 40, "For this demo, time shouldn't exist 40 seconds due to the limitation of Azure free account"

'''Image capture'''
capture_image(total_time, 2)
x, y = analyze_image()

'''Plot the result'''
plt.plot(x, y)
plt.xlabel('Time Elapsed (/10s)')
plt.ylabel('Difficulty Level')
plt.title('The Difficult Level of the Course')
plt.savefig('result.png')
plt.show()
