label scene_lora_01:

    a "baiklah"

    a "aku akan menunggunya"

    scene bg bighouse with fade

    show lora biasa with dissolve

    l "aku pulang"

    a "selamat datang"

    show lora tanya  with dissolve

    l "loh [player],kukira kamu sibuk ngerjain komik"

    a "sudah selesai kok"

    show lora senang with dissolve

    l "syukurlah"

    menu:
        "Lora bisa aku minta pendapat sebentar \?":
            jump scene_lora_01_01
        "Lora bisakah kita berbincang nanti malam":
            jump scene_lora_01_02

label scene_lora_01_01:

    show lora tanya with dissolve

    l "maaf [player] aku harus segera menggarap pr ku"

    jump scene_lora_02

label scene_lora_01_02:

    show lora biasa with dissolve

    l "nanti malam?"

    a "iya bila kau tak sibuk. . ."

    l "kalau tak salah aku mempunyai PR bahasa inggris"

label scene_lora_02:

    a "apa kau butuh bantuan?"

    l "ehh tapi.."

    a "komikku sudah selesai kok. komikku juga berbahasa inggris"

    show lora senang with dissolve

    l "ohh baik"

    #hide lora biasa

label scene_lora_03:

    scene bg kamar_a_sore with fade

    a "iya siapa?"

    l "ini aku, apa kau jadi?"

    a "baik , sebentar aku ganti baju"

    scene bg lorong_2 with fade

    show lora biasa with dissolve

    a "omong-omong Lora"

    l "iya?"

    a "kita mau kerjakan dimana?"

    l "di kamarku"

    scene bg kamar_lora with fade

    show lora biasa with dissolve

    a "*Sudah kuduga*"

    a "aku belum pernah masuk kamar perempuan sebelumnya"

    l "ohh, tak apa"

    l "lagian ini bukan kamar asli ku"

    l "aku hanya menambahkan buku atau poster"

    a "syukurlah"

    l "kenapa kamu gugup gitu?"

    a "ahh tak apa"

    a "mungkin ini bisa buat refrensi komik"

    show lora tanya with dissolve

    l "hmm"

    a "ada apa?"

    show lora senang with dissolve

    l "kapan-kapan aku liat komikmu ya"

    menu:
        "Ya tentu saja":
            jump scene_lora_04
        "Tidak maaf aku malu":
            jump scene_lora_04
label scene_lora_04:

    #show lora senang

    l "asyik"

    l "oh iya ayo kita kerjakan ini dulu"

    a "b-b-baik"

    #show lora smug?

    l "heeh jangan gitu dong"

    l "apa karena ada adegan dewasa?"

    a "tentu saja tidak"

    #show lora senang

    l "bercanda kok... hehe"

    #hide lora senang

    scene bg black with fade

    "Sesudah mengerjakan pr nya aku kembali menuju kamar"

    "aku mendengar suara seseorang"

    scene bg kamar_a with fade

    # show morune biasa bawa buku with dissolve

    m "aku berangkat"

    k "mau kemana?"

    m "ke perpustakaan..."

    k "ini larut malam loh"

    m "tak apa"

    # hide morune with dissolve

    a "apa yang morune mau lakukan"

    menu:
        "Menghentikannya":
            jump scene_lora_05
        "Mengikutinya":
            jump scene_lora_05

label scene_lora_05:

    #hide morune biasa

    scene bg lorong with fade

    show kyoko nanya with dissolve

    k "kau juga mau kemana [player]"

    a "aku akan mengikutinya"

    show kyoko biasa 2 with dissolve

    k "jangan pulang malam-malam"

    a "baik!"

    #hide kyoko biasa
    scene bg rumah_malam with fade

    a "kemana dia pergi tadi?"

    menu:
        "Kiri":
            jump scene_lora_05_01
        "Kanan":
            jump scene_lora_05_02

label scene_lora_05_01:

    a "aku akan belok kiri saja.."

    scene bg black with fade

    ## play tap tap

    jump scene_lora_06

label scene_lora_05_02:

    a "aku akan lewat kanan saja"

    ". . . . . ."

    a "tak ada siapa-siapa"

    a "aku akan kembali belok kiri."

    scene bg black with fade

    ## play tap tap



label scene_lora_06:

    scene bg gang_kecil with fade

    show morune bad marah with dissolve

    gk "hey kau!?"

    a "siapa?"

    gk "kau siapa memasuki wilayahku?"

    a "namaku [player] , aku mencari seseorang"

    show morune bad kaget with dissolve

    gk "[player]!?"

    a "kau mengenalku?"

    gk "ahh maaf"

    "Di lihat dari penampilannya ia wanita seperti geng preman. dengan penampilan tomboy"

    show morune bad biasa with dissolve

    a "apa kita pernah bertemu sebelumnya?"

    gk "tentu tidak"

    a "anuu maaf apa kau melihat wanita kacamata, berambut dikepang lewat sini."

    gk "tidak..."

    gk "aku tak melihatnya..."

    a "ohh begitu ya."

    gk "apa yang kau mau lakukan dengan wanita itu? "

    menu:
        "Aku akan menyuruhnya kembali. Semua orang di rumah khawatir":
            jump scene_lora_06_01
        "Aku akan memberikannya nasehat. meskipun aku tidak tau apa keinginan sebenarnya dia":
            jump scene_lora_06_02

label scene_lora_06_01:

    gk "cuma itu saja?"

    a "iya"

    gk "hmmm , dah aku pergi dulu"

    jump scene_lora_07

label scene_lora_06_02:

    gk "hooh, nasehat apa ?"

    a "seorang gadis tidak layak keluar malam-malam karena itu berbahaya. masa depan ia masih panjang."

label scene_lora_07:

    gk "apa kau khawatir tentang dia? "

    a "tentu saja! meskipun jarang berbicara aku tetap khawatir"

    a "karena aku takut kehilangan seseorang lagi."

    #show (gk) blushing

    $renpy.pause(1.0)

    #show morune bad biasa with dissolve

    gk "apa yang dia mau lakukan sebenarnya malam-malam begini?"

    a "entahlah , katanya ia menuju ke perpustakaan"

    gk "perpustakaan lewat kanan situ"

    a "benarkah!?"

    gk "iya"

    a "makasih!"

    gk ". . ."

    a "omong-omong namamu?"

    show morune bad kaget with dissolve

    gk "!?"

    hide morune bad kaget with dissolve

    gk "*lari meninggalkan tempat*"

    a "apa-apaan itu tadi"

    scene bg black with fade

    # This ends the game.

label scene_lora_08:

    scene bg ruang_keluarga with fade

    a "aku pulang"

    show kyoko biasa 3 at left with dissolve
    k "apa ia sudah ketemu?"

    a "ia tidak ada diperpustakaan"

    a "malah perpustakaannya tutup"

    show chikka biasa 2 at slightleft with dissolve

    c "apa ia jangan-jangan diculik?"

    show lora biasa at slightright with dissolve
    l "jangan gitu dong cikko"

    c "tapi , ini sudah larut malam loh"

    show kyoko biasa 4 at left with dissolve

    k "mungkin sebaiknya kita telfon polisi"

    show morune biasa bawa buku at right with dissolve

    m "aku pulang"

    "Morune!?"

    m "ada apa?"

    show kyoko biasa 3 at left with dissolve

    k "kau kemana saja!?"

    c "kukira kau keculik"

    l "jangan biasakan pulang malam. . ."

    show morune senyum at right with dissolve

    m "*Menatapku tersenyum*"

    $renpy.pause(1.0)

    show morune biasa bawa buku at right with dissolve

    m "aku hanya berbelanja"

    #hide kyoko biasa
    #show kyoko marah

    k "omong dulu dong ke saya . semua orang khawatir"

    m "baik. . ."

    a "omong-omong kau berbelanja kan?"

    a "apa kau tidak melihat seorang wanita keren di samping gang"

    show morune capek at right with dissolve

    m "!???"

    m "tidak..."

    a "ohh kukira kau melihatnya"

    show chikka kaget at slightleft with dissolve

    c "jangan-jangan dia!?"

    a "kau tau cikko?"

    c "dia ketua geng di kota ini"

    c "2 tahun yang lalu saat dia masih smp"

    c "dia menghajar seluruh orang yang masuk ke wilayahnya."

    a "ohh. . ."

    show chikka biasa at slightleft with dissolve
    c "apa kau bertemu dengannya?"

    a "iya kenapa?"

    c "apa kau tak apa!?"

    show kyoko biasa 4 at left with dissolve

    k "baiklah... . . ayo kita tidur. sudah larut."

    "Baik"

    #hide chikka biasa

label scene_lora_09:


    scene bg bighouse with fade

    a "Hmm...."

    a "hari ini ya?"

    a "aku harus minta pendapat Lora tentang anak sekolahan"

    a "aku harus menuju ke kamarnya"

    scene bg lantai_3 with fade

    show lora biasa with dissolve

    l "ahh [player] ada apa keburu gitu?"

    a "ahh [player] ada apa keburu gitu?"

    show lora tanya with dissolve

    l "hm?"

    l "ahh soal pendapatan buat komikmu ya?"

    a "iya"

    show lora biasa with dissolve

    l "apa kau tak makan dahulu?"

    a "ehh..."

    a "aku lupa"

    show lora senang with dissolve

    l "nanti Bu Kusina marah loh , hehe"

    a "omong-omong Lora"

    show lora biasa with dissolve

    l "iya?"

    a "kenapa kau memanggilnya dengan bu?"

    show lora tanya with dissolve

    l "apa salah?"

    a "tidak-tidak . aku cuma bertanya saja"

    show lora biasa with dissolve

    l "aku memanggilnya bu..."

    l "karena dia persis dengan guru disekolaanku"

    a "ohh begitu ya."

    a "kalau soal guru , hal apa yang cocok kalau bisa di bikin komik?"

    show lora tanya with dissolve

    l "hm...."

    show lora senang with dissolve

    l "mungkin guru yang tidak terlalu serius"

    a "guru muda?"

    l "iyap. . ."

    show lora biasa with dissolve

    l "omong-omong [player]"

    show lora senang with dissolve

    l "masuk aja kamarku"

    l "tak enak di sini terus"

    a "apa tak apa aku masuk?"

    l "tak apa kok"

    #hide lora senang

    scene bg kamar_lora with fade

    a "woah jadi ini kamar Lora"

    show lora biasa with dissolve

    l "terlalu normal ya hehe"

    l "soalnya aku mau lulus, aku tak memerlukan banyak barang disini"

    a "setelah kau lulus kau pergi dari sini?"

    l "iya..."

    menu:
        "mungkin suasana agak sepi tanpamu":
            jump scene_lora_09_01
        "ohh begitu baguslah":
            jump scene_lora_09_01

label scene_lora_09_01:

    show lora tanya with dissolve

    l "masa?"

    show lora biasa with dissolve

    l "aku juga tak terlalu dekat"

    a "itu tidak benar"

    a "kau selalu menyapa mereka atau menanyakan keadaan mereka kan"

    show lora tanya with dissolve

    l "iya tetapi apa itu bisa dibilang dekat?"

    a "tentu saja"


    #kurang ehe?
    #hide lora biasa
    #show lora kaget
    show lora biasa with dissolve

    l "[player] kun!"

    a "a.. apa? tiba-tiba menjerit?"

    l "mungkin itu bisa dibuat refrensi komikmu!"

    a "apa?"

    #hide lora kaget
    #show lora biasa

    show lora senang with dissolve

    l "seorang gadis yang selalu menyapa teman sekelasnya menyapa sang pemeran utama"

    l "sang pemeran utama memendam perasaan ke gadis itu sudah lama"

    l "akhirnya tersipu malu"

    a "wah tak kusangka kau memikirkannya cepat sekali"

    #hide lora biasa
    #show lora senang

    show lora biasa with dissolve

    l "karena aku selalu melihat mengamati alur film"

    a "wah keren-keren"

    k "[player] , makananmu sudah dingin. cepat makan"

    a "ahh aku kelupaan"

    show lora senang with dissolve

    l "hehe , makan dulu sana"

    a "tunggu sebentar ya"

    l "iya-iya"

    hide lora biasa with dissolve

    "Akhirnya aku mengerjakan story board komik serta dibantu alur cerita oleh Lora"

    #hide lora biasa

    #Hari menjelang malam
    # BG lorong lantai 3

    scene bg lantai_3_malam with fade

    #show morune biasa

    a "ohh Morune"

    show morune biasa bawa buku with dissolve

    m "apa?"

    a "tak kukira kau ada di rumah"

    m "tak kukira kau ada di rumah"

    a "omong-omong soal buku"

    a "apa kau pernah baca lightnovel?"

    #hide morune biasa
    #show morune tanya

    show morune biasa 2 with dissolve

    m "apa itu?"

    a "semacam novel tetapi ada beberapa gambaran..."

    a "mungkin"

    m "aku tidak pernah baca"

    m "memang kenapa?"

    a "oh tak apa"

    a "aku hanya sedikit tertarik saja ke lightnovel meskipun belum pernah membacanya"

    show morune biasa 2 with dissolve

    m "..."

    a "ada apa?"

    show morune senyum with dissolve

    m "kau aneh ya?"

    a "ehehehe"

    m "baiklah selamat malam, aku mau masuk kamar dulu"

    a "baik"

    show morune biasa 2 with dissolve

    m "omong-omong [player]"

    a "iya?"

    #hide morune tanya
    #show morune biasa

    show morune senyum with dissolve

    m "mungkin aku akan membaca lightnovel itu"

    m "jarang sekali kau tertarik pada suatu bacaan selain komik"

    #BG rumah malam
    #Bg rumah pagi

    #hide morune biasa

    scene bg black with fade

    centered "[player] bangun. . ."

    scene bg kamar_a with dissolve

    a "ada apa?"

    show lora biasa with dissolve

    l "bu Kyoko menyuruh semua berkumpul"

    a "baik..."

    scene bg ruang_keluarga with fade

    #BG ruangan keluarga

    #show kyoko biasa

    show kyoko biasa 1 at left with dissolve

    k ". . ."

    show chikka biasa 2 at slightleft with dissolve

    c "ada apa?"

    show morune biasa bawa buku at right with dissolve

    m "..."

    show lora biasa at slightright with dissolve

    l "ada apa bu?"

    show kyoko nanya at left with dissolve

    k "kalian semua besok ujian kan?"

    c "iya..."

    m "aku tidak terlalu peduli..."

    l "iya besok UAS"

    a "aku tidak ada ujian"

    show chikka biasa at slightleft with dissolve

    c "jelas kamu sudah lulus"

    show morune senyum with dissolve

    m "ya ampun"

    show lora senang with dissolve

    l "hahaha"

    show morune biasa bawa buku with dissolve
    show lora biasa with dissolve
    show chikka biasa 2 at slightleft with dissolve



    k "untuk beberapa saran jangan terlalu tegang atau keluar dari kos-kosan ini"

    a "dia seperti bu guru..."

    k "apa?"

    a "ahh tidak"

    c "melihat film?"

    k "tidak!"

    m "memangnya ada apa bu? tak kusangka anda kuatir seperti ini"

    k "ya sebelum angkatan kalian ada seorang anak yang tidak naik kelas"

    k "dan dia terus depresi hingga keluar dari rumah ini."

    l "jadi begitu ya"

    a "anuu.. terus aku ngapain bu"

    k "terserah , tapi jangan ganggu mereka"

    a "baiklah"

    k "ya sekarang mulai belajar"

    k "nanti malam akan kumasakkan masakan enak"

    c "baik siap"

    m "ada keuntungan ya dari belajar"

label scene_lora_10:

    scene bg kamar_a with fade

    a "bingung mau ngapain..."

    a "semua pada belajar"

    a "nggak ada mood lagi buat gambar komik"

    a "cuaca lagi cerah"

    a "mungkin aku harus keluar"

    scene bg bighouse with fade

    a "ternyata sangat panas"

    a "paling enak begini ke supermarket"

    scene bg depan_supermarket with fade

    show morune bad marah with dissolve

    gk "[player]?"

    a "iya?"

    a "ohh bukankah kau orang yang waktu itu?"

    show morune bad biasa with dissolve

    gk "iya.."

    a "omong-omong namamu siapa?"

    gk ". . ."

    show morune bad marah with dissolve

    gk "omong-omong kenapa kau disini?"

    a "ahh aku mau membeli minuman."

    show morune bad biasa with dissolve

    gk "bisakah kau menolongku?"

    a "iya?"

    gk "aku tidak memasuki tempat tersebut"

    a "tempat?"

    gk "iya"

    scene depan_perpus with fade

    show morune bad biasa with dissolve

    a "apa ini maksudmu tempat?"

    gk "iya"

    gk "aku ingin meminjam buku matematika kelas 3 sma"

    a "hm!?"

    a "dilihat dari penampilanmu"

    a "jangan-jangan, kau"

    show morune bad kaget with dissolve

    gk "aa...apa?"

    a "masih sekolah?"

    show morune bad biasa with dissolve

    gk "tentu saja...."

    a "baik aku pinjamkan , kau tunggu disini"

    gk "baik"

    scene bg black with fade

    $renpy.pause(1.0)

    scene bg depan_perpus with fade

    show morune bad biasa with dissolve

    a "ini"

    gk "terimakasih"

    hide morune bad biasa with dissolve

    a  "ya sama-sama"

    a "omong-omong namamu?"

    a "ahh dia hilang..."

    a ". . ."

    a "siapa sebenarnya dia?"

    scene bg ruang_keluarga with fade

    show lora biasa with dissolve

    l "aku pulang"

    a "ohh Lora bagaimana hasil rapotmu?"

    l "lumayan , aku ranking 3"

    a "wah syukurlah"

    l "hehe"

    l "bisakah kau kekamarku?"

    a "Heeh!?"

    show lora senang with dissolve

    l "hey jangan berpikiran buruk"

    show lora biasa with dissolve

    l "mulai besok aku libur selama 2 minggu jadi aku tidak ada kerjaan"

    l "mungkin denganmu hari-hariku tidak membosankan"

    a "baiklah aku akan menemanimu"

    show lora senang with dissolve

    l "benarkah!?"

    a "aku juga tidak ada kerjaan selain menunggu hasil komikku"

    l "aku lihat dong komikmu"

    a "ahh aku malu"

    l "ayolah"

    a "baik-baik"

    show lora biasa with dissolve

    l "Aku tunggu di kamarku ya"

    a "baik..."

    scene bg black with fade

    $renpy.pause(1.0)

    "Aku membuka pintu kamar lora"

    # scene bg kamar_lora with fade
    "Ternyata lora sedang memakai bra"

    l "KYAAAAAAAAAAAAA!!!!!!!!!......."
        # with hpunch

    #insert lora no bra in here

    a "Ma-maaf!!!"

    scene bg lorong_2 with fade

    show lora blushing with dissolve

    a "........"

    l "........"

    l "masuklah"

    a "baik"

    scene bg kamar_lora with fade

    a "......."

    show lora blushing with dissolve

    l "......."

    menu:
        "Maaf atas yang tadi":
            jump scene_lora_10_01
        "Kau terlihat seksi tadi":
            jump scene_lora_10_01

label scene_lora_10_01:

    l "iya lagian tidak sengaja."

    show lora biasa with dissolve

    l "oh iya lihat komikmu yang kamu bawa itu"

    a "ini"

    show lora tanya with dissolve

    l "..............."

    l "ohh begitu ya"

    l "hm-hm"

    l "ini tentang horor ya?"

    a "iya"

    a "tetapi aku ingin sekali-kali membuat komik romance"

    a "tetapi aku kekurangan refrensi"

    show lora biasa with dissolve

    l "dulu kau disekolah memangnya tidak punya pacar"

    a "tidak... aku hanya penyendiri waktu aku sekolah"

    a "tetapi aku sekarang menyesal karena aku tidak mengakrabkan diri saat dikelas dulu"

    a "masa sekolahku hilang deh . hehe"

    a "kalau kau Lora?"

    show lora senang with dissolve

    l "kalau aku sih menurutku normal saja"

    show lora biasa with dissolve

    l "aku mendapat teman maupun akrab dengan seluruh kelas"

    a "wah enaknya"

    l "tetapi menurutku tidak ada yang istimewa"

    a "kenapa?"

    l "karena seluruh orang membahas hal yang sama saja"

    l "justru aku mencari orang yang berbeda.. ."

    show lora blushing with dissolve

    l "ah maaf"

    a "tak apa-apa"

    l "wajahmu memerah"

    a "kamu juga"

    l "hehehe"

    a "hahaha"

    scene ruang_keluarga with fade

    a "ohh Chikka selamat malam"

    show chikka biasa with dissolve

    c "yo..."

    a "ada apa kau sakit?"

    c "tidak, aku hanya sedikit mengantuk"

    a "mau ku antar?"

    show chikka biasa 2 with dissolve

    c "EH!!"

    c "Ten-Tentu saja tidak , Bodoh!"

    a "jujurlah pada dirimu"

    show chikka biasa with dissolve

    c "aku tak apa"

    a "haduh nih anak"

    show kyoko biasa 3 at slightright with dissolve
    show chikka biasa at slightleft with dissolve

    k "kalian sedang apa?"

    a "ahh tak apa nte aku cuma mencari udara segar"

    show kyoko biasa 4 at slightright with dissolve

    k "ohh , terus kenapa itu cikka mukanya suram"

    show chikka biasa 2 at slightleft with dissolve

    c "itu bi..."

    c "aku gak sempat lihat film di tv"

    show kyoko biasa 2 at slightright with dissolve

    k "aku kira apaan"

    a "download di internet mending"

    show chikka biasa at slightleft with dissolve

    c "aku tak punya kuota"

    a "nih pakai kuotaku"

    show chikka biasa 2 at slightleft with dissolve

    c "apa tak apa?"

    a "iya..."

    c "makasih"

    show kyoko biasa 3 at slightright with dissolve

    k "cie"

    a "apaan nte"

    show kyoko biasa 4 at slightright with dissolve

    show chikka marah at slightleft

    c "apaan sih!"

    show chikka biasa at slightleft
    show lora biasa at right with dissolve

    l "Ehem!"

    a "Ah... yo lora"

    show lora senang at right with dissolve

    l "[player] besok jangan lupa janji penggarapan ceritamu ya"

    show lora biasa at right

    a "baik-baik"

    k "kalian ngapain?"

    show kyoko biasa 3 at slightright with dissolve

    a "ahh ngerjain komik nte"

    show kyoko biasa 4 at slightright with dissolve

    k "jangan bilang kalau itu komik dewasa"

    #lora marah

    show lora blushing 2 at right

    show kyoko biasa 3 at slightright with dissolve

    l "te-tentu saja bukan!"

    show lora biasa at right

    show kyoko biasa 4 at slightright with dissolve

    k "hahaha bercanda kok"

    k "baiklah selamat malam"

    hide kyoko biasa with dissolve

    "...."

    a "aku mau ke tempat tidur"

    l "aku juga"

    a "oke"

    l "baik , selamat malam"

    a "selamat malam juga"

    scene bg kamar_tidur_malam with fade

    a "aduh aku mengantuk"

    "*Dok Dok*"

    c "ini hp kamu"

    a "oh iya silahkan masuk , pintunya tidak ku kunci"

    c "apa tak apa?"

    a "Tentu..."

    show chikka biasa with dissolve

    c "i..ini"

    a "ada apa malu-malu begitu"

    c "tentu saja , aku baru pertama kali masuk kamar laki-laki"

    a "baik-baik, jadi kamu menghabiskan berapa kuotaku?"

    c "3 giga"

    a "HA!?"

    c "aku mendownload semua film nya"

    a "ya ampun...."

    c "selamat malam , aku mau tidur"

    "....."

    c "te-terimakasih"

    hide chikka biasa with dissolve

    a "iya"

    scene bg black with fade

    $renpy.pause(1.0)

label scene_lora_11:

    scene bg kamar_lora with fade

    show lora biasa with dissolve

    l "lambat!"

    a "maaf-maaf"

    show lora senang with dissolve

    l "cepat lihatlah kemari"

    a "hmm?"

    show lora biasa with dissolve

    l "aku sudah mengerjakan Storynya di laptop sangat banyak"

    a "jangan bilang kalau kau"

    show lora senang with dissolve

    l "iya benar"

    a "tidak tidur!?"

    l "iya..."

    a "tak perlu terburu kok... ini deadline masih lama"

    show lora biasa with dissolve

    l "omong-omong soal deadline sekarang ini pengunguman lomba komikmu kan?"

    a "oh iya ayo kita lihat"

    a "ah gawat..."

    l "ada apa?"

    a "kuotaku habis"

    #show lora kaget with dissolve

    l "ya ampun..."

    menu:
        "mengajaknya keluar":
            jump scene_lora_11_01
        "meninggalkannya sendirian di kamar":
            jump scene_lora_11_01

label scene_lora_11_01:

    l "kemana?"

    a "ke supermarket mau beli pulsa. disana jualan kalau tak salah"

    show lora biasa with dissolve

    l "baik aku akan ikut"

    scene bg depan_supermarket with fade

    a "kau tunggu disini atau ikut masuk?"

    show lora biasa with dissolve

    l "baiklah aku akan tunggu disini?"

    show morune bad kaget at slightleft with dissolve
    #show lora kaget with dissolve
    show lora blushing at slightright with dissolve

    gk "Lora?"

    "???"

    l "apa kau mengenalku?"

    a "ahh wanita ketua geng ?"

    l "yang waktu cikko bilang itu?"

    a "apa kau sudah mengembalikan buku yang ku ambil di perpus itu?"

    show morune bad biasa at slightleft with dissolve

    gk "tentu saja"

    l "kau mengenalnya [player]"

    a "iya aku pernah bertemu saat kau belajar buat persiapan uas dan saat mencari Morune"

    l "tunggu dulu...."

    a "ahh aku kelupaan , aku mau beli pulsa. tunggu di sini Lora"

    l "bukankah kau..."

    gk "...."

    scene bg black with fade

    $renpy.pause(2.0);

    "...."

    a "maaf , aku terlambat"

    l "hey [player]"

    a "iya?"

    l "tidak.. tidak apa-apa"

    a "ahh baik , ayo kita segera pulang dan melihat hasilnya."

    scene bg kamar_lora with fade

    show lora biasa with dissolve

    a "ayo kita lihat hasilnya"

    l "......."

    a "ada masalah?"

    l "tidak..."

    show lora senang with dissolve

    l "oh iya ayo kita lihat hasilnya"

    a "baiklah"

    "....."

    show lora biasa with dissolve

    l "....."

    a "....."

    l "di peringkat 1 sampai 10 masih belum ada namamu"

    a "iya..."

    l "...."

    a "....."

    l "ini sudah ke peringkat 25"

    a "......"

    show lora senang with dissolve

    l "sepertinya kau harus berjuang lagi"

    a "iya..."

    show lora biasa with dissolve

    l "[player]!"

    a "i-iya??"

    show lora senang with dissolve

    l "ya jangan putus semangat!"

    a "cek aja dulu itu ceritaku"

    l "aku membuatnya sangat spesial"

    a "baiklah aku cek"

    #scene bg depan_rumah_sore with fade

    scene bg black with fade

    a "tak kusangka aku gagal di hadapan perempuan yang hendak membantuku"

    $renpy.pause(1.0)

    scene bg kamar_lora with fade

    #scene sp lora_01 with fade

    a "Lora , ceritamu ini apa benar kau yang buat sendiri?"

    a "ahh dia tertidur"

    a "baru pertamakali aku melihat wanita sekolahan tidur di kasur seperti ini."

    a "dia tampak manis ketika tidur"

    a "tak kusangka dia membantuku sampai tidak tidur"

    a "akan kupastikan komik selanjutnya akan menang"

    a "baiklah aku akan mengerjakan di kamarku.."

    scene bg black with fade

    $renpy.pause(2.0)

label scene_lora_12:

    scene bg ruang_keluarga with fade

    show lora senang with dissolve

    l "Hey hey, aku mendapatkan 3 tiket ke taman bermain."

    show lora senang at slightleft with dissolve
    show chikka biasa 2 at slightright with dissolve

    c "maaf aku tidak bisa, aku sedikit sakit"

    show kyoko biasa 1 at left with dissolve

    k "aku tidak bisa meninggalkan cikka sendirian dirumah...."

    l "Morune?"

    show morune biasa bawa buku at right with dissolve

    m "maaf."

    show lora biasa at slightleft with dissolve

    l "hmm"

    a "?"

    show lora senang at slightleft with dissolve

    l "hey [player] ayo..."

    a "baik-baik"

    m "aku juga akan ikut...."

    show lora biasa at slightleft with dissolve

    l "ahh kukira kau tidak ikut"

    show kyoko nanya at left with dissolve

    k "jangan pulang larut.."

    "baik..."

    scene bg city with fade

    show lora biasa with dissolve

    l "Wah besar"

    show lora biasa at slightleft with dissolve
    show morune senyum at slightright with dissolve

    m "baru pertamakali aku memasuki tempat seperti ini"

    show lora senang at slightleft with dissolve

    l "yah apa yang kita tunggu"

    l "ayo kita masuk"

    scene bg black with fade

    "Semua bersenang bersama-sama"

    "memasuki berbagai macam kawasan wahana"

    a "ahh sepertinya aku tersesat"

    a "apa aku harus menunggunya atau mencarinya ya?"

    a "baiklah, aku akan pergi"

    scene bg suatutempat with fade

    show lora biasa with dissolve

    l "hey Morune"

    show lora biasa at slightleft with dissolve
    show morune biasa 2 at slightright with dissolve

    m "iya?"

    l "dimana [player]"

    m "aku tidak tau"

    l "haduh gimana ini"

    m "mungkin kita harus mencarinya berpencar "

    l "baiklah"

    scene bg black with dissolve

    $renpy.pause(1.0)

    scene bg suatutempat with fade

    show lora biasa at slightleft with dissolve

    l "[player]"

    l "woyy"

    a "Lora!?"

    l "dasar kemana saja kau ini"

    a "maaf aku tersesat"

    l "dasar"

    a "dimana Morune?"

    l "dia mencari kamu"

    l "omong-omong [player]"

    a "iya?"

    l "aku ingin memberitaumu sesuatu"

    l "kau tau"

    l "Morune..."

    l "sebenarnya dia adalah"

    a "????????"

    l "ketua gang yang kau temui itu"

    a "!?"

    a "apa maksudmu?"

    l "dia selalu keluar tidak diketahui"

    l "entah apa tujuannya"

    l "tetapi Morune"

    l "Sudah membohongi kita"

    show morune bad biasa at slightright with dissolve

    m "apa maksudmu?"

    l "Morune!?"



    m "sudah kubilang kalau ini masalah kita pribadi"

    l "tapi .."

    l "kenapa kau menyembunyikannya dari kita"

    show morune bad kaget at slightright with dissolve

    m "karena..."

    m "*memandang malu ke [player]"

    m "cih!"

    hide morune bad kaget with dissolve

    l "Morune!"

    scene bg black with fade

    $renpy.pause(1.0)

label scene_lora_13:

    scene bg ruang_keluarga with fade

    show kyoko biasa 1 at slightleft with dissolve

    k "selamat datang..."

    k "dimana Morune?"

    show lora biasa at slightright with dissolve

    l "dia pergi"

    show kyoko kaget at slightleft with dissolve

    k "Kenapa!?"

    a "ada sesuatu hal yang seharusnya kami tidak beritahu"

    k "astaga..."

    k "mungkin dia masih diperpustakaan"

    l "tidak"

    l "dia tidak disitu"

    k "apa maksudmu"

    l "maaf nte, besok aku akan mencarinya"

    scene bg black with fade

    $renpy.pause(1.0)

label scene_lora_14:

    scene bg kamar_a with fade

    a "pagi ini tidak secerah kemarin..."

    a "apa mau hujan ya?"

    a "ahh iya, Morune"

    scene bg ruang_keluarga with fade

    show kyoko biasa 1 at slightleft with dissolve

    k "ada apa?"

    a "apa Morune sudah pulang?"

    k "belum..."

    k "tetapi lora sudah tidak ada di kamar"

    a "apa?"

    menu:
        "Mencarinya":
            jump scene_lora_14_01
        "tetap disini":
            jump scene_lora_14_01

label scene_lora_14_01:

    k "[player] kau mau kemana?"

    a "tentu saja aku akan mencarinya"

    show kyoko biasa 2 at slightleft with dissolve

    k "cepat kembali , cuaca mendung"

    a "iya!"

    scene bg bighouse with fade

    a "aku harus kemana?"

    menu:
        "Gang dekat perpustakaan":
            jump scene_lora_14_01_01
        "depan supermarket":
            jump scene_lora_14_01_02

label scene_lora_14_01_01:

    scene bg gang_kecil with fade

    a "Morune apa kau disini?"

    "...."

    jump scene_lora_15

label scene_lora_14_01_02:

    scene bg depan_perpus with fade

    a "Morune apa kau disini?"

    "...."

    jump scene_lora_15

label scene_lora_15:

    a "dia tidak ada."

    a "aku akan menunggunya"

    scene bg black with fade

    $renpy.pause(1.0)

    scene bg gang_kecil with fade

    gk "hei kau?"

    a "aku ?"

    gk "apa kau mencari ketua?"

    a "ketua?"

    a "maksutmu morune?"

    a "ahh iya ketua ya. iya"

    gk "dia sudah tidak disini lagi"

    a "jadi dia kemana?"

    gk "dia pulang ke desa"

    gk "mungkin kau orang yang dia cari selama ini"

    a "apa maksudmu?"

    gk "dulu saat dia smp dia satu sekolah denganku"

    gk "alasanya dia pergi dari desanya hanya untuk mencarimu"

    gk "dia terus mencarimu"

    gk "sampai-sampai dia masuk ke sebuah gang ada beberapa preman"

    gk "tetapi justru dia menghajarnya habis-habisan"

    gk "dan dia dijuluki sebagai ketuagang sekarang ini"

    gk "tetapi dia hanya menjaga ketertiban disekitar sini"

    a "jangan-jangan Morune!?"

    gk "ohh iya sebelum di jam segini dia terkadang di pantai dekat seberang"

    gk "katanya dia akan pulang siang ini"

    a "aku harus bergegas"

    a "aku harus bergegas"

    scene bg pantai with fade

    a "Morune!!!"

    show morune bad kaget with dissolve

    m "!!!"
    m "[player] ?"

    a "Morune! aku mencarimu kemana-mana"
    a "jangan buat kuatir dong"

    show morune bad biasa with dissolve
    m "a... apa yang kau mau?"

    a "kenapa kau tak bilang padaku"
    m "soal apa?"
    a "kalau kau itu sebenarnya adalah perempuan yang satu desa denganku dulu"

    show morune bad kaget with dissolve
    m "!!"
    m "siapa yang memberitau mu?"


    m "kenapa kau bisa tau kalau itu adalah aku"
    a "aku bertemu dengan seorang di sebuah gang"

    show morune bad marah with dissolve
    m "tak kusangka"
    m "dia akan memberitaukannya"
    a "siapa dia?"
    m "dia kakakku"
    a "kakak!? ahh apa maksutmu kak Mira"
    m "ya ampun kau ini..."
    m "ingat kakakku tetapi tidak ingat aku"
    a "maaf-maaf"
    a "dulu kau memiliki rambut pendek dan ceria"

    a "omong-omong morune"
    show morune bad biasa with dissolve
    m "?"
    a "kenapa kau tidak lansung mengatakannya ke aku saja?"
    a "bahwa kau orang yang bersamaku terakhirkalinya aku meninggalkan desa"
    m "apa kau tak membaca kado yang kuberikan?"
    a "ahh aku lupa aku menaruhnya dimana"
    show morune bad senyum with dissolve
    m "ya ampun..."
    m "kau selalu ceroboh "
    a "iya hehehe"
    m "hihihi"
    m "[player]"
    m "iya?"
    m "terimakasih..."

    a "tidak , jangan berterimakasih ke aku"
    a "Lora telah mencarimu kemana-mana"
    m "mungkin ini juga salahku karena lansung pergi tiba-tiba"
    m "ini semua gara-gara aku"
    a "yang terpenting sekarang kamu kembali dulu ya"
    m "baik"

    scene bg ruang_keluarga with dissolve

    show morune biasa bawa buku at slightright with dissolve
    m "aku pulang"
    show kyoko biasa 1 at slightleft with dissolve
    k "kau kemana saja"
    show chikka biasa 2 at right with dissolve
    c "aku mencemaskanmu"
    m "maaf-maaf"
    show lora biasa
    l ". . ."

    m "Lora , maafkan aku"
    l "tidak apa"
    l "aku juga melanggar janjimu"
    l "aku juga minta maaf"
    m "Lora bisakah aku memberimu kepercayaan sekali lagi"
    l "apa?"
    show morune senyum at slightright with dissolve
    m "tolong jaga [player]"
    m "* tersenyum"
    l "a... apa yang kau maksutkan Morune *Blushing"

# DAY 8
# BG berganti Cuaca hujan dras
scene bg kamar_lora with fade
show lora tanya with dissolve
l "bukankah sekarang penilaianya komik kita?"
a "iya..."
l "apa kau sudah mengeceknya di web?"
l "belum"
show lora biasa with dissolve
l "jangan bilang kuotamu habis lagi"
a "tidak-tidak, aku hanya ingin melihat hasilnya bersamamu"
l "aaa... *Blushing"
show lora blushing with dissolve
l "oh begitu ya.. *senyum"
a "baik ayo kita lihat"
l "Ehm! tentu saja"

show bg black with fade
$renpy.pause(2.0)
show bg kamar_lora with fade
"......"
show lora biasa with dissolve
a "aku tidak percaya ini"
l "aku juga..."
a "Kita berhasil!"
show lora senang with dissolve
l "Selamat [player]"
a "aku sungguh berterimakasih padamu"
l "ayo kita rayakan"
a "tentu saja"
show lora biasa with dissolve
k "Lora ! [player] !"
k "apa nte?"
k "Cikka!"
l "ada apa?"
k "Cepat ikuti aku!"

show bg kamar_chikka with fade
# BG berganti di kamar Cikka
# Cover berganti Cikka terjatuh di kasur dengan keadaan tak sadar diri
a "ada apa ini"
l "Chikka! Chikka!"
show morune biasa 2 at slightleft with dissolve
m "ada apa berisik sekali..."
show morune capek at slightleft with dissolve
m "Ci..Cikka!?"
show chikka kaget at slightright with dissolve
c "tidak apa bu... aku mengalami kecapekan sedikit"
show kyoko khawatir at left with dissolve
k "tidak! kondisimu sangat parah"
a "apa kita perlu memanggil ambulan?"

menu:
    "Ya":
        jump scene_lora_16
    "Tidak":
        jump scene_lora_16

label scene_lora_16:

a "ayo kita panggil ambulan"
c "tidak perlu..."
m "sudah diamlah Cikka , aku akan menelponnya"
l "tak perlu cemas Cikka, istirahat saja ya"
c "baik"
m "gawat"
k "ada apa?"
c "tidak tersambung"
# *CTARRR
l "apa yang harus kulakukan?"
# a "*Lari ke rumah sakit/ menunggu hujan rendah"
menu:
    "Lari ke rumah sakit":
        jump scene_lora_16_01
    "Menunggu hujan rendah":
        jump scene_lora_16_01

scene bg black with fade

"Ambulan akhirnya datang pukul 23.00"
"Kondisi Cikka memburuk"
"Kami semua menunggu kabar dari dokter"
"Yang bisa kami lakukan ialah berdoa saja"

# Day 9....
scene bg black with fade
$renpy.pause(2.0)
scene bg lorong_sakit with fade
# BG berganti di ruangan koridor rumah sakit
show morune capek at slightleft with dissolve
m "apa yang sebenarnya terjadi?"
show lora tanya at slightright with dissolve
l "aku tidak tau..."
"*hening"

show kyoko khawatir at left with dissolve
k "semuanya...."
# k "(tidak berani melihat)
k "........."
k "Chikka mengalami kanker tingkat 4...."
m "apa!?"
k "dia menyembunyikannya dari kita"
k "kata dokter, penyakitnya sudah dimulai dari sd"
l "ja-jadi?"
k "tingkat keselamatannya sangat rendah"

a ". . ."

scene bg black with dissolve
# Cover berada di samping kaca melihat Cikka tertidur di kamarnya
centered "Meskipun dia orang yang menyebalkan"
centered "pemalu"
centered "tsundere"
centered "dan sebagainya"
centered "Semua itu apakah akan menghilang?"
centered "kumohon..."
centered "kembalilah"
"..............................."
scene bg black with fade
"Operasi Cikka akhirnya dimulai"
"tidak tau apakah akan berhasil atau tidak"
"bila tidak"
"aku akan kehilangan dia selamanya...."
scene bg lorong_sakit with fade
# DAY 10
show morune capek at slightright with dissolve
m "apa yang harus kulakukan"
show lora tanya at slightright with dissolve
l "aku tidak tau"
m "Kenapa ini bisa terjadi!"
l "ini adalah kesalahan kita"
m "apa?"
show lora biasa at slightright with dissolve
l "seaindainya kita dekat dengak Cikka"
l "dia menganggap kita sebagai saudaranya"
l "tetapi kita tidak dekat dengannya"
m "ini kesalahanku"
m "sedikit akrab dengannya."
a "jangan saling menyalahkan"
a "kita tunggu saja kabar dari dokter"
". . ."
show kyoko khawatir at left with dissolve
k "semuanya...."
k "Cikka!!!"
l "..."
m "..."
a "...."
show kyoko biasa 2 at left with dissolve
k "dia"
k "Selamat"
show morune capek at slightright with dissolve
m "Benarkah!"
l "alhamdulillah"
a "kapan kita bisa bertemu denganya nte?"
k "besok mungkin ia pulang"
show kyoko khawatir at left with dissolve
k "tetapi... semuanya"

show lora tanya at slightright with dissolve
l "hm?"
k "Cikka mengalami kaki lumpuh sesisa hidupnya"
show morune capek at slightright with dissolve
m "apa!?"
k "operasinya berjalan lancar , tetapi dia mengalami kelumpuhan..."
m "cih..."
show lora biasa at slightright with dissolve
l "aku akan pulang"
m "mau ngapain?"
show lora senang at slightright with dissolve
l "tentu saja merayakan Chikka berhasil selamat"
l "untung dia masih selamat"
show morune senyum at slightright with dissolve
m "aku akan ikut denganmu"
l "baik, nte aku akan pergi"
show kyoko biasa 2 at left with dissolve
k "baik *senyum"
# k ". . .*cemberut"

a "ada apa?"
show kyoko khawatir at left with dissolve

k "aku harus menjual barang-barang dirumah"
a "apa!?"
k "biaya operasinya sangat mahal"
a "tidak Nte, tidak!"
a "aku sudah cukup beruntung dengan selamatnya Cikka"
a "jangan membuat ku kuatir lagi"
show kyoko kaget at left with dissolve
k "tetapi..."
a "Tidak!"
a "selama kita di rumah tidak ada masalah seperti ini"
a "kumohon jangan tambahkan lagi"
a "meskipun aku-"
a "tunggu sebentar"

k "apa?"
a "aku memenangkan lomba komik"
a "Bi berapa biayanya?"
show kyoko khawatir at left with dissolve
k "******"
a "cih tinggal sedikit lagi"
a "sekarang aku mempunyai uang *******"
k "aku memilikinya beberapa juga"
m "Bu"
show kyoko kaget at left with dissolve
k "uwaah! Morune!?"
show morune biasa 2 at slightright with dissolve
m "aku kesini mau berpamitan , tetapi aku mendengar masalah penting"
show morune senyum at slightright with dissolve
m "*senyum"
m "aku mempunyai dana uang anggota *******"
m "tentu saja bi, kau tidak perlu mengorbankan hal yang tidak-tidak"
k "semuanya...."
"semuanya tersenyum"
# Day 11
# BG depan rumah pagi
# BG ruang keluarga
scene bg black with fade

$renpy.pause(2.0)

scene bg ruang_keluarga with fade
show chikka biasa at slightright with dissolve
c "pa-pagi"
show lora senang at slightright with dissolve

l "CIKKA!"
l "selamat atas kesembuhanmu"
c "ii..iya..."
show lora biasa at slightright with dissolve

l "hehehe"
show morune senyum at slightright with dissolve

m "selamat atas kesembuhanmu cikka"
c "iya"
c "terimakasih"
a "selamat datang kembali Cikka"
show chikka biasa 2 at slightright with dissolve

c "maaf semuanya"
c "aku mengkhawatirkan kalian"

l "tidak-tidak , mungkin kita yang salah"
l "malah kita tidak tau kalau kau mengalami sakit begitu"
k "Cikka..."
c "iya bi?"
k "apa kau memang mau pergi?"
l "apa!?"
m "Apa maksudnya!?"
c "iya... orangtua ku akan menjemputku"
c "aku sudah tidak bisa bersekolah lagi"
l "tetapi!?"
k "ini keputusan Cikka"
k "kita tidak bisa mengelak lagi"
m "Cikka...."

l "Aku akan buatkan ceritanya"
a "baik baik..."
a "omong-omong soal komik?"
a "kenapa kau sangat bersemangat"
l "AH *Blushing"
a "ahh...."
l "anoo... apa ya..."
l "ah bagaimana kalau kita kencan buat soal komik"
l "*Hening"
l "WAHHH LUPAKAN!!!!"
a "ayo aja"
l "apa?"
a "ayo kita kencan"


# Day 12
# BG di taman
a ". . ."
l "maaf aku terlambat"
a "ahh tidak apa-apa"
l "ehmm bagaimana penampilanku"
a "kau tampak cantik/ kau layaknya ibuku"
l "benarkah..."
l "makasih"
a "ah... iya sama-sama"


l "ayo kita mulai kencan kita"
a "Baik...."



"Akhirnya kencaku dengan Lora dimulai"
"Ia tampak bahagia sekali"
"aku akan memutuskan kesempatan terakhirku"

"Aku akan menembakkan perasaan cintaku ke dia/ Aku akan menganggapnya dia seperti kakakku saja"


# Di taman sore hari

a "Lora!!"
l "ah iya [player]?"
a ". . ."
a "ini mungkin terlalu mendadak"
a "aa.."
a "ah maaf"
l "tidak apa-apa "
a "Mau jadi pacarku!?"
l "!!!!"
l "*menatap kesamping . menatap kembali"
l "* menangis"
l ": tentu saja"

# BG berubah menjadi putih
centered "Semua lulus dari sekolah masing-masing"
centered "mereka semua akhirnya kembali kerumahnya masing-masing"
centered "Tetapi di hari kelulusan itu aku mendapatkan sesuatu yang indah"
centered "yang namanya"
centered "Cinta"

scene bg black with dissolve

"5 tahun kedepan"
l "sayang..."
a "iya..."
l "aku hamil"
a "benarkah!? selamat"

centered "aku sudah menikah dengan Lora"
centered "kehidupanku dengannya serasa menyenangkan"
centered "Selamanya"
centered "Aku akan berada di sisinya..."
