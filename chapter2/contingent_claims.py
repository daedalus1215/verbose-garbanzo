import numpy as np

s1 = np.arange(20)
print(s1)
K = 10
C1 = np.maximum(s1-K, 0)
print(C1)

# plotting configuration
from pylab import mpl, plt

# plt.style.use('seaborn-v0_8')
mpl.rcParams['savefig.dpi']=300
mpl.rcParams['font.family'] = 'serif'


plt.figure(figsize=(10, 6))
plt.plot(s1, C1, lw=3.0, label='$C_1 = \max(S_1 - K, 0)$')
plt.legend(loc=0)
plt.xlabel('$S_1$')
plt.ylabel('$C_1$')

plt.show()

