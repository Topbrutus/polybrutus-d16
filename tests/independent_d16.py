#!/usr/bin/env python3
"""Polybrutus D16 independent exact metric and ideal Laplacian verification.

No import of the D16 or parent point generators. Rebuilds each labelled
squared distance from rational rules and verifies all 210 pairwise entries.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
import hashlib,json
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
report=json.loads((ROOT/"results"/"certificate_d16.json").read_text(encoding="utf8"))
prior=json.loads((ROOT/"prior"/"certificate_d15.json").read_text(encoding="utf8"))
core=[
 (F(0),F(0),F(1)),(F(1,2),F(0),F(1,2)),
 (F(-1,4),F(3,4),F(1,2)),(F(-1,4),F(-3,4),F(1,2)),
 (F(0),F(0),F(-1)),(F(1,2),F(0),F(-1,2)),
 (F(-1,2),F(0),F(-1,2))
]
def squared_distance(i,j):
    if i==j:return F(0)
    if i<7 and j<7:
        a,b,c=(core[i][k]-core[j][k] for k in range(3))
        return 3*a*a+b*b+c*c
    if 7<=i<12 and 7<=j<12:return F(5,2)
    return F(2)

pairs=list(combinations(range(21),2))
exact={(i+1,j+1):squared_distance(i,j) for i,j in pairs}
cert={(int(e["i"]),int(e["j"])):F(e["d2"])
      for e in report["labelled_squared_distances"]}
assert len(exact)==210 and exact==cert
old={(int(e["i"]),int(e["j"])):F(e["d2"])
     for e in prior["labelled_squared_distances"]}
assert len(old)==190 and all(exact[k]==v for k,v in old.items())
assert all(squared_distance(i,20)==F(2) for i in range(20))
hist=Counter(4*squared_distance(i,j) for i,j in pairs)
assert hist==Counter({F(4):6,F(7):2,F(8):179,F(9):3,F(10):10,F(12):6,F(13):2,F(16):2})
assert sum(exact.values(),F(0))==F(1727,4)
D=s.Matrix(21,21,lambda i,j:s.Rational(squared_distance(i,j).numerator,squared_distance(i,j).denominator))
H=s.eye(21)-s.ones(21)/21
B=-H*D*H/2
assert B.rank()==16
D15=D[:20,:20];H15=s.eye(20)-s.ones(20)/20
assert (-H15*D15*H15/2).rank()==15

L=s.zeros(21)
for i,j in pairs:
    w=1/D[i,j]
    L[i,i]+=w;L[j,j]+=w
    L[i,j]-=w;L[j,i]-=w
z=s.Symbol("z");chi=L.charpoly(z).as_expr()
for value,mult in [(s.Rational(21,2),10),(s.Integer(10),4)]:
    assert all(s.simplify(s.diff(chi,z,k).subs(z,value))==0 for k in range(mult))
    assert s.simplify(s.diff(chi,z,mult).subs(z,value))!=0
assert report["affine_rank"]==report["centered_gram_rank"]==16
assert report["parent_distances_preserved"]==190 and report["new_distances"]==20
p=ROOT/"results"/"certificate_d16.json"
print("INDEPENDENT D16 PASS: 210 rational labelled distances, 190 old preserved, Gram rank 16")
print("INDEPENDENT MODEL GRAPH PASS: eigenvalue 21/2 x10; eigenvalue 10 x4")
print("CERTIFICATE_SHA256="+hashlib.sha256(p.read_bytes()).hexdigest())
