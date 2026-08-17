import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We want to replace everything from "24": [ to the closing } of typingData
start_marker = '    "24": ['
end_marker = '  const levels = Object.keys(typingData);'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Could not find markers")
    exit(1)

new_data = """    "24": [
      {"kanji": "ドラゴン (Dragon)", "romaji": "doragon(dragon)", "img": "dragon"},
      {"kanji": "フェニックス (<ruby>不死鳥<rt>ふしちょう</rt></ruby>)", "romaji": "fenikkusu(fusityou)", "img": "phoenix,bird"},
      {"kanji": "ユニコーン (<ruby>一角獣<rt>いっかくじゅう</rt></ruby>)", "romaji": "yuniko-n(ikkakujuu)", "img": "unicorn"},
      {"kanji": "クラーケン (<ruby>海<rt>うみ</rt></ruby>の<ruby>怪物<rt>かいぶつ</rt></ruby>)", "romaji": "kura-ken(uminokaibutu)", "img": "kraken,monster"},
      {"kanji": "ペガサス (<ruby>天馬<rt>てんま</rt></ruby>)", "romaji": "pegasasu(tenma)", "img": "pegasus"},
      {"kanji": "ネッシー (ネス<ruby>湖<rt>こ</rt></ruby>の<ruby>謎<rt>なぞ</rt></ruby>)", "romaji": "nesshi-(nesukononazo)", "img": "lochnessmonster"},
      {"kanji": "ビッグフット (Bigfoot)", "romaji": "biggufutto(bigfoot)", "img": "bigfoot,sasquatch"},
      {"kanji": "チュパカブラ", "romaji": "tyupakabura", "img": "chupacabra"},
      {"kanji": "ケルベロス (<ruby>地獄<rt>じごく</rt></ruby>の<ruby>番犬<rt>ばんけん</rt></ruby>)", "romaji": "keruberosu(zigokunobanken)", "img": "cerberus"},
      {"kanji": "ツチノコ<ruby>発見<rt>はっけん</rt></ruby>！？", "romaji": "tutinokohakken!?", "img": "cryptid,snake"}
    ],
    "25": [
      {"kanji": "レベル25：<ruby>究極<rt>きゅうきょく</rt></ruby>の<ruby>試練<rt>しれん</rt></ruby>！！", "romaji": "reberu25:kyuukyokunosiren!!", "img": "challenge,boss"},
      {"kanji": "1, 2, 3... ボスと<ruby>戦<rt>たたか</rt></ruby>う<ruby>準備<rt>じゅんび</rt></ruby>はいいか？", "romaji": "1, 2, 3... bosutotatakaujunbihaiika?", "img": "boss,fight"},
      {"kanji": "<ruby>動物<rt>どうぶつ</rt></ruby> vs <ruby>植物<rt>しょくぶつ</rt></ruby> vs <ruby>恐竜<rt>きょうりゅう</rt></ruby> vs UMA！", "romaji": "doubutu vs syokubutu vs kyouryuu vs uma!", "img": "evolution"},
      {"kanji": "<ruby>生命<rt>せいめい</rt></ruby>の<ruby>誕生<rt>たんじょう</rt></ruby>：46<ruby>億年<rt>おくねん</rt></ruby>の<ruby>歴史<rt>れきし</rt></ruby>", "romaji": "seimeinotanjou:46okunennorekisi", "img": "history,earth"},
      {"kanji": "function <ruby>進化<rt>しんか</rt></ruby>() { return \"スーパー！\"; }", "romaji": "function sinka() { return \"su-pa-!\"; }", "img": "biology,science"},
      {"kanji": "【<ruby>究極<rt>きゅうきょく</rt></ruby>】すべての<ruby>命<rt>いのち</rt></ruby>は<ruby>海<rt>うみ</rt></ruby>から<ruby>始<rt>はじ</rt></ruby>まった", "romaji": "[kyuukyoku]subetenoinotihaumikarahazimatta", "img": "ocean,origin"},
      {"kanji": "~~~~~~DNAの<ruby>二重<rt>にじゅう</rt></ruby>らせん~~~~~~", "romaji": "~~~~~~dnanonizyuurasen~~~~~~", "img": "dna,helix"},
      {"kanji": "http://www.<ruby>究極生物<rt>きゅうきょくせいぶつ</rt></ruby>タイピング.com/", "romaji": "http://www.kyuukyokuseibututaipingu.com/", "img": "internet,network"},
      {"kanji": "$<ruby>地球<rt>ちきゅう</rt></ruby>$ - <ruby>生命<rt>せいめい</rt></ruby>あふれる<ruby>青<rt>あお</rt></ruby>い<ruby>星<rt>ほし</rt></ruby>", "romaji": "$tikyuu$ - seimeiafureruaoihosi", "img": "earth,planet"},
      {"kanji": "<ruby>祝<rt>しゅく</rt></ruby>★<ruby>全<rt>ぜん</rt></ruby>250<ruby>問完全制覇<rt>もんかんぜんせいは</rt></ruby>！<ruby>真<rt>しん</rt></ruby>の<ruby>生物王<rt>せいぶつおう</rt></ruby>だ！！！", "romaji": "syuku*zen250monkanzenseiha!sinnoseibutuouda!!!", "img": "champion,king"}
    ]
  };

"""

new_content = content[:start_idx] + new_data + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Fixed successfully")
