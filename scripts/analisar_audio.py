import sys, parselmouth, numpy as np
from parselmouth.praat import call
s=parselmouth.Sound(sys.argv[1])
p=s.to_pitch(time_step=0.01,pitch_floor=60,pitch_ceiling=300)
f=p.selected_array['frequency']; f=f[f>0]
print("F0 median %.1f mean %.1f p10 %.1f p90 %.1f std %.1f"%(np.median(f),f.mean(),np.percentile(f,10),np.percentile(f,90),f.std()))
st=12*np.log2(f/np.median(f)); print("range semitones p5-p95: %.1f"%(np.percentile(st,95)-np.percentile(st,5)))
fm=s.to_formant_burg(max_number_of_formants=5,maximum_formant=5000)
for i in (1,2,3,4):
  v=[call(fm,"Get value at time",i,t,"Hertz","Linear") for t in np.arange(0.5,s.duration,0.02)]
  v=np.array([x for x in v if not np.isnan(x)]); print("F%d median %.0f"%(i,np.median(v)))
h=s.to_harmonicity(); print("HNR %.1f"%call(h,"Get mean",0,0))
pp=call(s,"To PointProcess (periodic, cc)",60,300)
print("jitter %.4f"%call(pp,"Get jitter (local)",0,0,0.0001,0.02,1.3))
print("shimmer %.4f"%call([s,pp],"Get shimmer (local)",0,0,0.0001,0.02,1.3,1.6))
ltas=call(s,"To Ltas",100); 
print("energy 0-1k minus 1-4k dB: %.1f"%(call(ltas,"Get mean",0,1000,"energy")-call(ltas,"Get mean",1000,4000,"energy")))
i=s.to_intensity(); v=i.values[0]; voiced=(v>v.max()-25).mean(); print("active ratio %.2f"%voiced)
