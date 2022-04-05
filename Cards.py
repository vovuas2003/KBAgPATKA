import random
all_cards=[]
cards=[]
for m in 'ABCD':
    for n in '123456789':
        all_cards.append(n+m)
while len(all_cards)!=0:
    x=all_cards.pop(random.randint(0,len(all_cards)-1))
    cards.append(x)
deck=[]
ii_deck=[]
for i in range(6):
    deck.append(cards.pop())
    ii_deck.append(cards.pop())
mast_koz=chr(random.randint(ord('A'),ord('D')))
print('TBOu KAPTbl:',*deck,'KO3blPb:',mast_koz)
count=0
def xog_ii_defend():
    global ii_deck
    global card
    global mast_koz
    output=-1
    mast=card[1]
    nom=int(card[0])
    ii_deck.sort()
    for i in range(len(ii_deck)):
        x=ii_deck[i]
        if x[1]==mast and int(x[0])>nom:
            output=i
            break
    if output==-1:
        if mast==mast_koz:
            return output
        else:
            for i in range(len(ii_deck)):
                x=ii_deck[i]
                if x[1]==mast_koz:
                    output=i
                    break
            return output
    else:
        return output
def xog_ii_attack():
    global ii_deck
    global mast_koz
    ii_deck.sort()
    output=-1
    for i in range(len(ii_deck)):
        card=ii_deck[i]
        if card[1]!=mast_koz:
            output=i
            break
    if output==-1:
        return 0
    else:
        return output
while True:
    if len(cards)==0:
        if len(deck)==0 and len(ii_deck)==0:
            print('Hu4b9')
            break
        elif len(deck)==0:
            print('Tbl BblurPAJl!')
            break
        elif len(ii_deck)==0:
            print('Tbl nPourPaJl!')
            break
    print('KAPT OCTAJlOCb:',len(cards))
    print('KAPT Y nPOTuBHuKA:',len(ii_deck))
    count=count+1
    if count%2==1:
        kon=[]
        print('Bbl XoguTe')
        print('TBOu KAPTbl:',*deck,'KO3blPb:',mast_koz)
        print('HOMEPA:',end='      ')
        if len(deck)<=10:
            for i in range(1,len(deck)+1):
                print(i,end='  ')
        else:
            for i in range(1,10):
                print(i,end='  ')
            for i in range(10,len(deck)+1):
                print(i,end=' ')
        print()
        print('Bbl6EPuTE HOMEP KAPTbl:',end=' ')
        n=int(input())
        while n<1 or n>len(deck):
            print('OLLlu6KA! BBEguTE KOPPEKTHblu HOMEP:',end=' ')
            n=int(input())
        card=deck.pop(n-1)
        kon.append(card)
        print('KOH:',*kon)
        print('KAPTA:',card)
        local_numbers=[]
        local_numbers.append(int(card[0]))
        if xog_ii_defend()==-1:
            print('nPOTuBHuK B39lJl KAPTY')
            ii_deck.append(card)
            count=count-1
        else:
            n_card_def=xog_ii_defend()
            card_def=ii_deck.pop(n_card_def)
            if int(card_def[0]) not in local_numbers:
                local_numbers.append(int(card_def[0]))
            kon.append(card_def)
            print('nPOTuBHuK nO6uJl KAPTY:',card_def)
            print('KOH:',*kon)
            while len(kon)<12 and len(deck)!=0 and len(ii_deck)!=0:
                print('0=6uTA uJlu gOKJlAgblBAuTE KAPTbl HOMuHAJlOM:', *sorted(local_numbers))
                print('TBOu KAPTbl:',*deck,'KO3blPb:',mast_koz)
                print('HOMEPA:',end='      ')
                if len(deck)<=10:
                    for i in range(1,len(deck)+1):
                        print(i,end='  ')
                else:
                    for i in range(1,10):
                        print(i,end='  ')
                    for i in range(10,len(deck)+1):
                        print(i,end=' ')
                print()
                print('Bbl6EPuTE HOMEP KAPTbl:',end=' ')
                n=int(input())
                if n==0:
                    print('6uTA!')
                    break
                else:
                    while n<1 or n>len(deck):
                        print('OLLlu6KA! BBEguTE KOPPEKTHblu HOMEP:',end=' ')
                        n=int(input())
                    prov=int(deck[n-1][0])
                    if prov not in local_numbers:
                        print('HA KOHY HET TAKOrO HOMuHAJlA!')
                    else:
                        card=deck.pop(n-1)
                        kon.append(card)
                        print('KOH:',*kon)
                        print('KAPTA:',card)
                        if xog_ii_defend()==-1:
                            print('nPOTuBHuK B39lJl KOH')
                            ii_deck=ii_deck+kon
                            count=count-1
                            break
                        else:
                            n_card_def=xog_ii_defend()
                            card_def=ii_deck.pop(n_card_def)
                            if int(card_def[0]) not in local_numbers:
                                local_numbers.append(int(card_def[0]))
                            kon.append(card_def)
                            print('nPOTuBHuK nO6uJl KAPTY:',card_def)
                            print('KOH:',*kon)
    else:
        kon=[]
        print('Bbl 6bETECb')
        n_card_attack=xog_ii_attack()
        card=ii_deck.pop(n_card_attack)
        kon.append(card)
        print('KOH:',*kon)
        print('KAPTA:',card)
        while True:
            print('TBOu KAPTbl:',*deck,'KO3blPb:',mast_koz)
            print('HOMEPA:',end='      ')
            if len(deck)<=10:
                for i in range(1,len(deck)+1):
                    print(i,end='  ')
            else:
                for i in range(1,10):
                    print(i,end='  ')
                for i in range(10,len(deck)+1):
                    print(i,end=' ')
            print()
            print('Bbl6EPuTE HOMEP KAPTbl uJIu 0=B39Tb KAPTY:',end=' ')
            n=int(input())
            if n==0:
                print('BbI B39JIu KAPTY')
                deck.append(card)
                count=count-1
                break
            else:
                while n<1 or n>len(deck):
                    print('OLLlu6KA! BBEguTE KOPPEKTHblu HOMEP:',end=' ')
                    n=int(input())
                card_4el=deck.pop(n-1)
                if card[1]==mast_koz and card_4el[1]!=mast_koz:
                    print('HeJIb39 TAK no6uTb!')
                    deck.append(card_4el)
                elif card[1]==card_4el[1]==mast_koz:
                    if int(card[0])>int(card_4el[0]):
                        print('HeJIb39 TAK no6uTb!')
                        deck.append(card_4el)
                    else:
                        print('6uTa!')
                        break
                elif card[1]!=mast_koz and card_4el[1]==mast_koz:
                    print('6uTa!')
                    break
                else:
                    if card[1]!=card_4el[1]:
                        print('HeJIb39 TAK no6uTb!')
                        deck.append(card_4el)
                    else:
                        if int(card[0])>int(card_4el[0]):
                            print('HeJIb39 TAK no6uTb!')
                            deck.append(card_4el)
                        else:
                            print('6uTa!')
                            break
    if count%2==1:
        while len(cards)!=0 and len(deck)<6:
            deck.append(cards.pop())
        while len(cards)!=0 and len(ii_deck)<6:
            ii_deck.append(cards.pop())
    else:
        while len(cards)!=0 and len(ii_deck)<6:
            ii_deck.append(cards.pop())
        while len(cards)!=0 and len(deck)<6:
            deck.append(cards.pop())
print('Enter - 3AKPblTb cmd',end='')
input()
