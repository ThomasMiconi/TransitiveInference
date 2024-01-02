import numpy as np
import matplotlib.pyplot as plt
import scipy


ALPHA = 1.0
NBEPISODES = 1000
ONLYUPDATEONERROR = False # True # False
TANH = False # True

plt.figure(figsize=(4,3))

corrzperplot = []

for numplot, REINSTATE in enumerate([False, True]):
    valsperepisode = []
    for numepisode in range(NBEPISODES):

        vals = 2.0 * np.random.rand(8) - 1.0
        for numtrial in range(20):
          pos1 = np.random.randint(7)
          pos2 = pos1 + 1
          response = vals[pos2] - vals[pos1]
          correct = True if response < 0 else False # vals1 should be > vals2
          incr =  ALPHA * (1 if response > 0 else -1) * (-1 if correct else 1)
          if correct and ONLYUPDATEONERROR:
              incr = 0
            
          vals[pos1] += incr
          vals[pos2] -= incr
          if REINSTATE:
              if pos1>0:
                vals[pos1-1] += .5 * incr
              if pos2<7:
                vals[pos2+1] -= .5 * incr
        valsperepisode.append(vals)
    valsperepisode = np.array(valsperepisode)
    if TANH:
      valsperepisode = np.tanh(valsperepisode)
    mycolor = ['b','r'][numplot]

    corrz =  np.corrcoef(valsperepisode, np.arange(8))[NBEPISODES][:NBEPISODES] # Correlation of each final set of vals (across all episodes) with arange(8); note that we must exclude tha last val which is just corr of arange(8) with itself
    corrzperplot.append(corrz)
    print("Mean/std of corrz b/w vals and arange(8) (reinstate="+str(REINSTATE)+"):", np.mean(corrz), np.std(corrz))
    meanz = np.mean(valsperepisode, axis=0)
    stdz = np.std(valsperepisode, axis=0)
    
    plt.fill_between(np.arange(8), meanz-stdz, meanz+stdz, color=mycolor, alpha=.3)
    plt.plot(meanz, color=mycolor, label=('REINSTATE' if REINSTATE else 'NO-REINSTATE'))


plt.xticks(np.arange(8), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
plt.legend()


print("Mann-Whitney U-test (2-sided) on the groups of correlations from both plots (without/with reinstate):",
        scipy.stats.mannwhitneyu(corrzperplot[0], corrzperplot[1]))
#        scipy.stats.mannwhitneyu(corrzperplot[0], corrzperplot[0]))

plt.show()
plt.savefig('toymodel.png', dpi=300)


