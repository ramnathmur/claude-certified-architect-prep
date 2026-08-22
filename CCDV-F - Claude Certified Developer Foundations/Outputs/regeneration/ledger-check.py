F=[3,9,2,12,11,7,5,3,4,12,1,4,9,10,2,11,12,6,5,11,10,7,4,1,3,10,7,2,8,5,8,6,1,8]
O=list("DAFCEABDECABFCBFDAEFBAEADBABEBFEAC")
A=["container","weather","translation bureau","letter carriers","restaurant modes","mechanic noise",
"passport form","hiker pack","theatre set","surgeon nurse","hardware labels","live radio",
"credit check","water main","assembly line","hiring","flat-pack","locum doctor","airport security",
"pro kitchen","policy stack","one bank","subcontract","hotel prefs","baggage allowance","driving test",
"plumber leak","courier address","mailroom","bank vault","key system","architect brief","proofreader","bridge"]
from collections import Counter
ok=True
print(f"chapters: F={len(F)} O={len(O)} A={len(A)}")
if not (len(F)==len(O)==len(A)==34): print("LENGTH MISMATCH"); ok=False
c=Counter(F); over=[f for f,n in c.items() if n>3]
print(f"form uses: {dict(sorted(c.items()))}  sum={sum(c.values())}")
print(f"forms over cap(3): {over or 'none'}");  ok &= not over
missing=[f for f in range(1,13) if f not in c]
print(f"forms unused: {missing or 'none'}")
adjF=[i+1 for i in range(33) if F[i]==F[i+1]]
adjO=[i+1 for i in range(33) if O[i]==O[i+1]]
print(f"adjacent same FORM at ch: {adjF or 'none'}"); ok &= not adjF
print(f"adjacent same OPENING at ch: {adjO or 'none'}"); ok &= not adjO
dupA=[a for a,n in Counter(A).items() if n>1]
print(f"duplicate anchors: {dupA or 'none'}"); ok &= not dupA
oc=Counter(O); print(f"opening spread: {dict(sorted(oc.items()))}")
print("\nLEDGERS VALID" if ok else "\nLEDGERS INVALID")
