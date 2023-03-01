import streamlit as st
from PIL import Image

st.title('*eMOtion*')
st.markdown("---")
pagelist = ["トップページ","あなたの番です","ヴァイオレットエヴァーガーデン","思い出のマーニー","そしてバトンは渡された","天使にラブ・ソングを","パイレーツオブカリビアン_呪われた海賊たち","パイレーツオブカリビアン_デッドマンチェスト","パイレーツオブカリビアン_ワールドエンド","ハウルの動く城"]
selector=st.sidebar.selectbox( "映画選択",pagelist)
kai={"あなたの番です":'図1より、全体的にポジティブなツイートが多い。感情スコア0.25付近のポジティブなツイートが最も多く、感情スコア0.00や0.5や1.0のツイートも多い。  \n図2をより、放送開始時間に一番ツイートが多くなっている。映画のジャンルがサスペンスものなので最初の事件が起こるまでのシーンはみんなゆっくりとtwitterを見ながら映画を見ていて事件が起きた後は推理をしようと映画を集中して見ているため、最初以外はツイート数が減っていると思われる。',
     "ヴァイオレットエヴァーガーデン":'※元のデータに欠損があるためグラフが映画終盤付近のみが描画されている。  \n図1全より、全体的にポジティブな感想が多く、感情スコア0.00～1.00までの間で特別大きくなっている値はなく平坦な形状である。  \n図2より、23:15あたりはツイート数が2500件以下なのに対し、23:35にかけての20分間でツイート数が20000件近くまで急増している。また、感情の部分に注目すると、ネガティブ寄りの感情であり緑色の部分が減少し、上から二番目にポジティブな感情である茶色い部分やポジティブ寄りな感情の紫色の部分も増加している。これはラストシーンを見ていた人々が「この映画面白かった」などのポジティブなツイートが集中したと思われる。',
     "思い出のマーニー":'図1より、感情スコア1.00が最も多く、0.50もかなり多い。また、感情スコア-1.00～-0.01の部分はかなり少なく、逆にポジティブな感情は先ほど挙げたもの以外も他の映画に比べて全体的に高い.  \n図2は最もポジティブな感情の色であるピンク色が大部分をしめていてネガティブな感情を示す緑、橙、青の部分の面積はかなり小さい。ツイート数は23:00あたりの部分が最も多くなっていて、ここがクライマックスシーンなため、最も盛り上がっているシーンだと思われ、感情部分に注目してもここは特にピンク色の面積が大きくなっている。',
     "そしてバトンは渡された":'図1より、他の映画では感情スコア0.00が多くなりやすい傾向にあるが、この映画では特に感情スコア0.00が多い。次点で感情スコア0.75付近が最も多い。また、ポジティブな感情はネガティブな感情に比べて比較的多い 。  \n図2より、ポジティブな感情の色であるピンク色と三番目にネガティブな感情の色である緑色が多く含まれている。これは、最初の方のシーンはまだ映画に見入る前なのでツイートする余裕があり、最後の方のシーンでツイート数が増えたのは、ラストシーンを見た後の謎が明かされたシーンの考察や感想を書いているからだと思われる。',
     "天使にラブ・ソングを":'図1より、グラフが大幅に右側に偏っているため全体的に明るくとてもポジティブな作品だということが分かる。  \n図2より、放送開始時間からポジティブなツイートが多いことから期待された作品だと分かる。中盤や終盤のクライマックスシーンでも圧倒的にポジティブなツイートが多いのは本映画がコメディ多めのミュージカル作品であるため、クライマックスは盛大なシーンであると思われるためである。 ',
     "パイレーツオブカリビアン_呪われた海賊たち":'図1より、感情スコア0.00のツイートが多く他のツイートは右側に多少の偏りがある。これは初上映から20年がたち内容を知っている視聴者が多いため、感情の起伏が少ないのだと思われる。  \n図2より、全体的にツイート数が多く感情スコアにバラつきがみられる。これは、本映画ではストーリー性がところどころ変化し少し複雑であるため、考察ツイートが多くなり感情スコアばらついたためだと思われる。 ',
     "パイレーツオブカリビアン_デッドマンチェスト":'図1より若干ポジティブな方に偏りがあるがほぼ左右対称の形である。  \n図2は他の映画に比べてネガティブな感情が多い。これは、シリーズもの故に一作品目の方が面白かったなどの感想が含まれているからだと考えられる。最後の方のシーンは他の映画同様に大きく盛り上がっがその比率はネガティブな感情とポジティブな感情が同等のツイート数なので、賛否両論気味の映画と思われる。',
     "パイレーツオブカリビアン_ワールドエンド":'図1より、他の映画と同様に感情スコア0.00が最も多い傾向にある。他の感情に関しては特別多い値はなく、ややポジティブな感情に偏っている。これに関して、この映画はシリーズ三部作の完結編で情報量が多く展開が早い。そのため、観てる人によって印象に残る場面に違いがあるので、多様な感情の分布になったと考えられる。  \n図2より、比較的ネガティブな感情が多い。これはデッドマンチェストと同様にシリーズもの故に過去の作品を見た人が、「過去の作品の方が面白かった」というようなツイートをする人がいるためであると考えられる。',
     "ハウルの動く城":'図1より、感情スコア0.00のツイートが多く他ツイートは右側に大きな偏りがある。本映画にはストーリーやキャラクター性、作画などの表部分に着目する視聴者と都市伝説や裏設定に着目する視聴者に分けることができると思われる。前者は感想などにより高い感情スコアを出し後者は考察などにより標準的な感情スコアを出すと思われる。  \n図2より、クライマックスよりも映画終了後の23:30付近でツイート数が急増している。これは、本映画は認知度が高く情報共有が盛んなためだと思われる。'}
if selector=="トップページ":
        st.markdown("Twitter API v2 を使い、金曜ロードショー放送時間の関連したツイートを取得。それを極性辞書を用いた自然言語処理で感情スコアを付与し、可視化・解釈をおこなった。")
        st.subheader('  \n映画タイトルを左側から選んでください')
        
elif selector==pagelist[1]:
        st.title(pagelist[1])
        st.markdown("晴れて結婚した菜奈と翔太は、親しくなったマンションの住人たちを招いて、豪華客船でウェディングパーティーを開くことにした。しかし、船の中でひとり、またひとりと殺されてしまう。逃げ場のない船の上で、菜奈と翔太は連続殺人の謎を解こうとするのだが……")
        st.markdown("引用元:https://natalie.mu/eiga/film/186925")
        img = Image.open('あなたの番です2.png',)
        st.header("図1:ヒストグラム")
        st.image("あなたの番です2.png", use_column_width=True,width=10)
        st.markdown('横軸が感情を-1から1で表したもの縦軸はツイート数')    
        imgg = Image.open('あなたの番です.png',)
        st.header("図2:積み上げ面プロット")
        st.image("あなたの番です.png", use_column_width=True,width=30)
        st.markdown('数字が大きい程ポジティブ(青(0)＜橙(1)＜緑(2)＜赤(3)＜紫(4)＜茶(5)＜桃(6)),横軸は時間、縦軸はツイート数')
        
        st.subheader('グラフの解釈')
        st.write(kai[selector])
        st.subheader('こんな方におすすめ')
        st.write('ミステリーものが好きな方や考察をしながら映画を見たい人ドラマ版をすでに見ている人')
        st.write('・謎解き　　・ミステリー')
       

elif selector==pagelist[2]:
        st.title(pagelist[2])
        st.markdown("4年間にわたる東西南北による大陸戦争が終結。その戦場で「武器」と称されて戦うことしか知らなかった少女・ヴァイオレット・エヴァーガーデンは、激化する戦場で両腕を失い、自在に動く義手を着けることを余儀なくされる。退院したヴァイオレットは、ホッジンズの下で、自動手記人形としてC.H郵便社で働きはじめる。ヴァイオレットにはかつて戦場で誰よりも大切な人・ギルベルト少佐がいた。最後に聞かされた「愛してる」という言葉が理解できなかったヴァイオレットは、仕事と日常を通じて人と触れ合いながら、その言葉の意味を探していく")
        st.markdown("引用元:https://ja.wikipedia.org/wiki/%E3%83%B4%E3%82%A1%E3%82%A4%E3%82%AA%E3%83%AC%E3%83%83%E3%83%88%E3%83%BB%E3%82%A8%E3%83%B4%E3%82%A1%E3%83%BC%E3%82%AC%E3%83%BC%E3%83%87%E3%83%B3")
        img = Image.open('ヴァイオレット.png',)
        st.header("図1:ヒストグラム")
        st.image("ヴァイオレット.png", use_column_width=True,width=10)
        st.markdown('横軸が感情を-1から1で表したもの縦軸はツイート数')
        imgg = Image.open('ヴァイオレット2.png',)
        st.header("図2:積み上げ面プロット")
        st.image("ヴァイオレット2.png", use_column_width=True,width=30)
        st.markdown('数字が大きい程ポジティブ(青(0)＜橙(1)＜緑(2)＜赤(3)＜紫(4)＜茶(5)＜桃(6)),横軸は時間、縦軸はツイート数')
        
        st.subheader('グラフの解釈')
        st.write(kai[selector])
        st.subheader('こんな方におすすめ')
        st.write('本映画はテレビシリーズの続編となっている。自然と涙がこぼれるようなストーリーであり、手書きのやわらかで繊細な作画がとても魅力的な作品。疲れて涙を流したい人や退屈しのぎにアニメを見たい方にとてもおすすめの作品。')
        st.write('・ファンタジー　　・アニメｰション　　・群像劇')
elif selector==pagelist[3]:
        st.title(pagelist[3])
        st.markdown("12歳の少女・佐々木杏奈は持病の喘息を持っており、夏休みの間義母・頼子の親戚夫婦の家で療養することになります。一見大人しく頼子の言うことを聞いている杏奈でしたが、実は表には出さない距離感を秘めていました。そんな杏奈は親戚夫婦の家でもぎこちなく生活をすることになるのですが、近所に暮らす少女・信子と喧嘩をしてしまいとっさに逃げ出します。こうして逃げた先で見つけたのが、“湿っ地屋敷”。浮かんでいたボートで屋敷にたどり着いた杏奈は、金髪で青い目をした少女・マーニーと出会い親しくなります。そして、この出会いが杏奈にとって秘められた自身のルーツを辿るきっかけとなっていくのでしたーー。")
        st.markdown("引用元:https://eigahitottobi.com/article/187598/")
        img = Image.open('思い出のマーニー.png',)
        st.header("図1:ヒストグラム")
        st.image("思い出のマーニー.png", use_column_width=True,width=10)
        st.markdown('横軸が感情を-1から1で表したもの縦軸はツイート数')
        imgg = Image.open('思い出のマーニー2.png',)
        st.header("図2:積み上げ面プロット")
        st.image("思い出のマーニー2.png", use_column_width=True,width=30)
        st.markdown('数字が大きい程ポジティブ(青(0)＜橙(1)＜緑(2)＜赤(3)＜紫(4)＜茶(5)＜桃(6)),横軸は時間、縦軸はツイート数')
        
        st.subheader('グラフの解釈')
        st.write(kai[selector])
        st.subheader('こんな方におすすめ')
        st.write('ジブリ映画が好きな人や田舎の雰囲気を味わいたい人')
        st.write('・ファンタジー　　・アニメｰション　　・子供向け')
elif selector==pagelist[4]:
        st.title(pagelist[4])
        st.markdown("血の繋がらない親に育てられた森宮優子は、料理上手な義理の父とふたりで暮らし、将来や友人関係に悩んでいた。その一方で、夫を何度も変えて来た梨花は、愛娘を置いて姿を消した。ある日、優子に届いた一通の手紙をきっかけに、ふたりの物語が交差していく。")
        st.markdown("引用元:https://natalie.mu/eiga/film/187116")
        img = Image.open('バトン.png',)
        st.header("図1:ヒストグラム")
        st.image("バトン.png", use_column_width=True,width=10)
        st.markdown('横軸が感情を-1から1で表したもの縦軸はツイート数')  
        imgg = Image.open('バトン2.png',)
        st.header("図2:積み上げ面プロット")
        st.image("バトン2.png", use_column_width=True,width=30)
        st.markdown('数字が大きい程ポジティブ(青(0)＜橙(1)＜緑(2)＜赤(3)＜紫(4)＜茶(5)＜桃(6)),横軸は時間、縦軸はツイート数')

        st.subheader('グラフの解釈')
        st.write(kai[selector])
        st.subheader('こんな方におすすめ')
        st.write('本映画は、主人公である優子の未来を守った親たちの愛情深いリレーの物語である。泣けて心が温まるような感動作を見たい方におすすめの作品。')
        st.write('・ドラマ')
elif selector==pagelist[5]:
        st.title(pagelist[5])
        st.markdown("ナイトクラブで歌手をしているデロリス（ウーピー・ゴールドバーグ）は、大物マフィアのボスであるヴィンス（ハーヴェイ・カイテル）の愛人であった。しかし、ヴィンスが裏切り者を殺すところを見てしまったため、マフィアから追われる身となってしまう。重要参考人として警察に保護されたデロリスは、ヴィンスの裁判が始まるまで修道院でかくまわれることに。自由奔放なデロリスは、尼僧として格式高い修道院で生活することとなる。始めはそんな堅苦しい生活に我慢ならないデロリスであったが、歌手だった経験を活かして、下手くそな聖歌隊を鍛え上げていく。そして、保守的な修道院長と対立しながらも、派手で自由な聖歌にアレンジし、修道院のシスターたちと音楽を通して友情を育んでいくのであった。しかし、マフィアがデロリスの居場所を遂に突き止めて……。")
        st.markdown("引用元:https://filmaga.filmarks.com/articles/52132/")
        img = Image.open('天使にラブ・ソングを.png',)
        st.header("図1:ヒストグラム")
        st.image("天使にラブ・ソングを.png", use_column_width=True,width=10)
        st.markdown('横軸が感情を-1から1で表したもの縦軸はツイート数')  
        imgg = Image.open('天使にラブ・ソングを2.png',)
        st.header("図2:積み上げ面プロット")
        st.image("天使にラブ・ソングを2.png", use_column_width=True,width=30)
        st.markdown('数字が大きい程ポジティブ(青(0)＜橙(1)＜緑(2)＜赤(3)＜紫(4)＜茶(5)＜桃(6)),横軸は時間、縦軸はツイート数')

        st.subheader('グラフの解釈')
        st.write(kai[selector])
        st.subheader('こんな方におすすめ')
        st.write('本映画は、明るい歌やパフォーマンスで見ているだけで笑顔になるだけではなく感動もできる作品である。笑えて心あたたまる映画を見たい方におすすめの作品である。')
        st.write('・コメディ　　・音楽')
elif selector==pagelist[6]:
        st.title(pagelist[6])
        st.markdown("18世紀のカリブ海ポート・ロイヤル。バルボッサが率いる海賊船ブラックパール号が町を襲い、総督の娘・エリザベスがさらわれてしまう。バルボッサの目的は、エリザベスが身につける黄金の金貨。その金貨は、バルボッサ自らの呪いを解くことができる黄金の金貨だったのだ。エリザベスに恋心を抱いていたウィル・ターナーは自由を愛する一匹狼の海賊・ジャック・スパロウと手を組み、エリザベスを救うため、海に出ていく。")
        st.markdown("引用元:https://filmaga.filmarks.com/articles/213249/")
        img = Image.open('パイレーツオブカリビアン_呪われた海賊たち.png',)
        st.header("図1:ヒストグラム")
        st.image("パイレーツオブカリビアン_呪われた海賊たち.png", use_column_width=True,width=10) 
        st.markdown('横軸が感情を-1から1で表したもの縦軸はツイート数')  
        imgg = Image.open('パイレーツオブカリビアン_呪われた海賊たち2.png',)
        st.header("図2:積み上げ面プロット")
        st.image("パイレーツオブカリビアン_呪われた海賊たち2.png", use_column_width=True,width=30)
        st.markdown('数字が大きい程ポジティブ(青(0)＜橙(1)＜緑(2)＜赤(3)＜紫(4)＜茶(5)＜桃(6)),横軸は時間、縦軸はツイート数')

        st.subheader('グラフの解釈')
        st.write(kai[selector])
        st.subheader('こんな方におすすめ')
        st.write('冒険ものの映画が好きな人や、パイレーツオブカリビアンシリーズが好きな人、別作品を見たことのある人')
        st.write('・アクション　　・アドベンチャー　　・ファンタジー')
elif selector==pagelist[7]:
        st.title(pagelist[7])
        st.markdown("ブラックパール号をとりもどしたキャプテン・ジャック・スパロウの前にあらわれたのは、海の悪霊デイヴィ・ジョーンズの使い、ビル・ターナーだった。ジャックがジョーンズとかわした「血の契約」の実行のときがきたというのだ。このままでは、ジャックはジョーンズの幽霊船の奴隷となってしまう。ジョーンズの心臓がおさめられているという「死者の宝箱（デッドマンズ・チェスト）」をさがすため、ウィルやエリザベスたちもまきこんで、あらたな航海がはじまる。")
        st.markdown("引用元:https://pictbook.info/ehon-list/isbn-9784062786027/")
        img = Image.open('パイレーツオブカリビアン_デッドマンズチェスト.png',)
        st.header("図1:ヒストグラム")
        st.image("パイレーツオブカリビアン_デッドマンズチェスト.png", use_column_width=True,width=10)
        st.markdown('横軸が感情を-1から1で表したもの縦軸はツイート数')
        imgg = Image.open('パイレーツオブカリビアン_デッドマンズチェスト2.png',)
        st.header("図2:積み上げ面プロット")
        st.image("パイレーツオブカリビアン_デッドマンズチェスト2.png", use_column_width=True,width=30)
        st.markdown('数字が大きい程ポジティブ(青(0)＜橙(1)＜緑(2)＜赤(3)＜紫(4)＜茶(5)＜桃(6)),横軸は時間、縦軸はツイート数')

        st.subheader('グラフの解釈')
        st.write(kai[selector])
        st.subheader('こんな方におすすめ')
        st.write('冒険ものの映画が好きな人や、パイレーツオブカリビアンシリーズが好きな人、別作品を見たことのある人')
        st.write('・アクション　　・アドベンチャー　　・ファンタジー')
elif selector==pagelist[8]:
        st.title(pagelist[8])
        st.markdown("「デイヴィ・ジョーンズの心臓」を手に入れ世界征服を目論むベケット卿によって、七つの海を駆け巡る海賊の時代が終ろうとしていた。ベケット卿に対抗するには、9人の伝説の海賊を集める必要があったが、その9人目は、現在「デイヴィ・ジョーンズの墓場」に囚われているジャック・スパロウだった。エリザベスとウィルはジャックを奪還するため、海賊バルボッサも加わり、海賊史上最大の戦いに身を投じていく。")
        st.markdown("引用元:https://filmaga.filmarks.com/articles/216178/")
        img = Image.open('パイレーツオブカリビアン_エンドワールド.png',)
        st.header("図1:ヒストグラム")
        st.image("パイレーツオブカリビアン_エンドワールド.png", use_column_width=True,width=10)
        st.markdown('横軸が感情を-1から1で表したもの縦軸はツイート数')
        imgg = Image.open('パイレーツオブカリビアン_エンドワールド2.png',)
        st.header("図2:積み上げ面プロット")
        st.image("パイレーツオブカリビアン_エンドワールド2.png", use_column_width=True,width=30)
        st.markdown('数字が大きい程ポジティブ(青(0)＜橙(1)＜緑(2)＜赤(3)＜紫(4)＜茶(5)＜桃(6)),横軸は時間、縦軸はツイート数')

        st.subheader('グラフの解釈')
        st.write(kai[selector])
        st.subheader('こんな方におすすめ')
        st.write('冒険ものの映画が好きな人や、パイレーツオブカリビアンシリーズが好きな人、別作品を見たことのある人')
        st.write('・アクション　　・アドベンチャー　　・ファンタジー')
elif selector==pagelist[9]:
        st.title(pagelist[9])
        st.markdown("しがない帽子屋のソフィーは、ある日兵士にナンパされていたところを魔法使いのハウルに助けられます。しかしハウルを追っていた荒地の魔女のとばっちりで、彼女の容姿は90歳のおばあさんになってしまいました。帽子屋としてとどまることができないと感じたソフィーは、すぐに家を出ていきます。不思議なカカシに導かれ、たどり着いたのはハウルが住む動く城でした。そこでソフィーはそこの掃除係として住み込むことになります。城を動かす火の悪魔カルシファーやハウルの弟子のマルクル、かかしのカブとの奇妙な毎日が始まるのでした。")
        st.markdown("引用元:https://ciatr.jp/topics/45959")
        img = Image.open('ハウル.png',)
        st.header("図1:ヒストグラム")
        st.image("ハウル.png", use_column_width=True,width=10)
        st.markdown('横軸が感情を-1から1で表したもの縦軸はツイート数')
        imgg = Image.open('ハウル2.png',)
        st.header("図2:積み上げ面プロット")
        st.image("ハウル2.png", use_column_width=True,width=30)
        st.markdown('数字が大きい程ポジティブ(青(0)＜橙(1)＜緑(2)＜赤(3)＜紫(4)＜茶(5)＜桃(6)),横軸は時間、縦軸はツイート数')
        st.subheader('グラフの解釈')
        st.write(kai[selector])
        st.subheader('こんな方におすすめ')
        st.write('本映画は、キャラクターや背景の作画がとてもきれいであったり、謎が多く難解な作品ですが見れば見るほど新しい発見があり何回見ても飽きない作品である。近代ヨーロッパのような世界観が好きな方や考察が好きな方におすすめの作品。')
        st.write('・ファンタジー　　・アニメｰション　　・子供向け')
