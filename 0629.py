import random
print("数当てゲームを始めます")
print("答えの数の範囲は1~50です")

answer = random.randrange(start=1, stop=100)
guess = int(input("貴殿が予想する数字:"))
tries = 1

while(guess != answer):
  # 予想が外れている限り、whileの中身を繰り返して実行する
  if(guess > answer):
    print("予想した数は答えより大きいです")
  else:
    print("予想した数は答えより小さいです")

  tries = tries + 1
  guess = int(input("貴殿が予想する数字:"))
# whileが終了したので予想が当たった
print("正解です。答えは{}".format(answer))
print("貴殿のの試行回数は{}です".format(tries)) 
