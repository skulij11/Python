
def process_du(st):
    li = st.splitlines()
    li = sorted(li, key=lambda x: int(x.split()[0]), reverse = True)
    re = []
    for i in li:
        s, fp = i.split(maxsplit=1)
        d = fp.split('/')[-1]
        re.append(d)
    return re

print(process_du("""228136 ./Example preim 312
202099  ./Library
561775  ./Submission-arXiv v1
100294  ./B-inv-proposition
799927  ./CodeSage/SageRuns
826594  ./CodeSage
569863  ./Submission-FPSAC2012/Final submission
315957  ./Submission-FPSAC2012/Sample
1210768 ./Submission-FPSAC2012/Galley
6670    ./Submission-FPSAC2012/Original submission/auto
572082  ./Submission-FPSAC2012/Original submission
2737508 ./Submission-FPSAC2012
1298628 ./CodeHaskell/s
4513852 ./CodeHaskell
9759720 ."""))
