##### 암호 #####
from sys import stdin, exit
secret_code = stdin.readline().strip()
s_len, dp = len(secret_code), [0] * len(secret_code)
if secret_code[0] == '0': print(0), exit(0)
elif s_len > 1:
  if (int(secret_code[0]) == 2 and 0 < int(secret_code[1]) < 7) \
    or (int(secret_code[0]) == 1 and int(secret_code[1]) != 0):
    dp[0], dp[1] = 1, 2
  elif int(secret_code[0]) > 2 and int(secret_code[1]) == 0:
    print(0), exit(0)
  else: dp[0], dp[1] = 1, 1
else: print(1), exit()
for i in range(2, s_len):
  check = int(secret_code[i - 1])
  if int(secret_code[i]) == 0:
    if check > 2 or check == 0: print(0), exit(0)
    else: dp[i] = dp[i - 2] % 1000000
  elif (check == 2 and 0 < int(secret_code[i]) < 7) or (check == 1 and int(secret_code[i]) != 0):
    dp[i] = dp[i - 2] + dp[i - 1]
  else: dp[i] = dp[i - 1] % 1000000
print(dp[-1])