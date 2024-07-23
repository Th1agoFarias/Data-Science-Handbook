#%%
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Apply seaborn theme
sns.set_theme(style="whitegrid")

# %%
fig = plt.figure()
ax = plt.axes()

x = np.linspace(0,10,1000)
ax.plot(x,np.sin(x))
# %%
plt.plot(x, np.sin(x))
plt.plot(x, np.sin(x));

# %%
plt.plot(x, np.sin(x - 0), color='blue')        # specify color by name
plt.plot(x, np.sin(x - 1), color='g')           # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')        # Grayscale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44')     # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 to 1
plt.plot(x, np.sin(x - 5), color='chartreuse'); # all HTML color names supported
# %%
plt.plot(x,x +0, '-g')
plt.plot(x,x +1, '--c')
plt.plot(x,x +2, '-.g')
plt.plot(x,x +3, '-g');
# %%
plt.plot(x, np.sin(x))

plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5);
# %%
plt.plot(x, np.sin(x))
plt.xlim(10, 0)
plt.ylim(1.2, -1.2);
# %%
plt.plot(x, np.sin(x))
plt.axis('tight');
# %%
plt.plot(x, np.sin(x))
plt.axis('equal');
# %%
plt.plot(x, np.sin(x))
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)");
# %%
plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')
plt.axis('equal')
plt.legend();
# %%
ax = plt.axes()
ax.plot(x, np.sin(x))
ax.set(xlim=(0,10), ylim=(-2,2),
       xlabel = 'X', ylabel='sin(x)',
       title='A simple Plot')
# %%
