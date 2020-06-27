s = input()
s_r = s[::-1]
ans = "No"
if s == s_r:
    ss = s[:int((len(s) - 1) / 2)]
    ss_r = ss[::-1]
    if ss == ss_r:
        sss = s[int((len(s) + 3) / 2) - 1:]
        sss_r = sss[::-1]
        if sss == sss_r:
            ans = "Yes"
print(ans)
