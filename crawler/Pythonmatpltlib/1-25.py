from  matplotlib import pyplot as plt
import random

x=range(0,120)
y=[random.randint(20,35) for  i in range(120)]
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

_xtick_labels=["10点{}分".format(i) for i in range(60)]
_xtick_labels=["11点{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=90)#rotation旋转角度


plt.show()