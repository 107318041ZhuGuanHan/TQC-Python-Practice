playing_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']
five_cards = []

for i in range(1, 6):

    card = input("請輸入第%d張撲克牌數字/英文: " % i)

    if card in playing_cards[:-4]: # card若是在play_cards的前面9個就表示是數字 -> 從最前面~倒數第4個之前
        five_cards.append(int(card)) # -> 可以直接強制型轉

    elif card in playing_cards[-4:]: # card若是在play_cards的最後4個就表示是英文字 -> 從倒數第四個開始~最後面一個

        if card == 'A': # -> 要下判斷轉數字 -> 一個一個來
            five_cards.append(1) # 直接 append(數字) 就好了，不用想太多

        elif card == 'J':
            five_cards.append(11)

        elif card == 'Q':
            five_cards.append(12)

        elif card == 'K':
            five_cards.append(13)

total = sum(five_cards)
print("5張牌的數值總和 = " + str(total))

# 參考答案的思路較為簡單，先把判斷英文字改成數字寫在前面(把英文都剔除)，然後再直接append(int())


