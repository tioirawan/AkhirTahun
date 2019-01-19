label scene_morune_01:
    a "Baiklah"
    a "Aku akan menunggunya"

    scene bg ruang_keluarga with fade

    # show morune biasa with dissolve

    a "dia masih belum datang..."
    a "apa dia diperpustakaan ya?"

    "..."

    pause 1

    m "Aku pulang"

    show lora biasa with dissolve

    a "*dia datang"
    a "Morune bisa bicara sebentar?"
    m "A-aku?"
    a "Iya"
    m "A...ada apa?"
    a "Anu..."
    a "Ohh omong-omong kau sering ke perpustakaan kan?"
    m "Iya"

    a "apa kau menyukai doujin?"

    # show morune kageat

    m "HEH!? (BLUSHING)"
    m "Maaf? "
    a "Ahh maksudku komik"

    # show morune biasa

    m "Aa terkadang aku membacanya"
    m "Memang kenapa?"
    a "Bisakah kau membantuku"
    m "Membantu?"
    a "Membantuku mencari refrensi buat komikku"
    m "Kenapa aku?"
    a "Karena kamu cewek misterius/ Karena kamu sering ke perpustakaan"
    m "...."
    m "Pffttt hehehe"

    m "Tentu ayo aku bantu"
    a "Makasih"

    "Berhenti sejenak..."

    m "Baik aku ke kamar dulu"
    m "Omong-omong besok kalau mau aku bantu"
    m "Bersiaplah jam 3 sore di perpustakaan"
    m "Tunggu aku sebentar disana, mungkin aku pulang sekolah agak terlambat."
    a "Baik"

    "....."

    "Tak kusangka cewek itu bisa ceria"
    "Besok aku akan pergi ke perpustakaan bersamanya"
    "Seperti kencan saja...."

    show bg kamar_tidur_malam with fade
    
    m "Aku berangkat"

    show lora biasa at slightright with dissolve
    show kyoko biasa 1 at slightleft with dissolve

    k "Mau kemana?"
    m "Ke perpustakaan..."
    k "Ini larut malam loh"
    m "Tak apa"
    a "Apa yang morune mau lakukan"

    menu:
        a "What should i do nigga"

        "Membiarkanya":
            jump scene_morune_01_01
        "Mengikutinya":
            jump scene_morune_01_02

label scene_morune_01_01:
    pass

label scene_morune_01_02:
    scene bg lorong with fade

    show kyoko nanya with dissolve

    k "Kau juga mau kemana [player]"
    a "Aku akan mengikutinya"

    show kyoko khawatir with dissolve

    k "Jangan pulang malam-malam"
    a "Baik!"

    # scene bg rumah malam

    menu:
        a "Kemana dia pergi tadi?"

        "Kiri":
            a "Aku akan belok kiri saja..."

            jump scene_morune_02
        "Kanan":
            a "Aku akan lewat kanan saja"

            "..."

            a "..."
            a "Tak ada siapa-siapa"
            a "Aku akan kembali belok kiri"

            jump scene_morune_02

label scene_morune_02:
    scene bg gang_kecil with fade

    gk "Hey kau!?"
    a "Siapa?"
    gk "Kau siapa memasuki wilayahku?"
    a "Namaku [player], aku mencari seseorang"
    gk "[player]!?"
    a "Kau mengenalku?"
    gk "Ahhh maaf"

    "Dilihat dari penampilannya ia seperti geng preman."
    extend "Dengan penampilan tomboy"
    a "Apa kita pernah bertemu sebelumnya?"
    gk "Tentu tidak!"
    a "Anuu..." 
    extend " Maaf apa kau melihat wanita kacamata, berambut dikepang lewat sini."
    gk "Aku tak melihatnya..."
    a "Ohh begitu ya."
    gk "Apa yang kau mau lakukan dengan wanita itu?"

    menu:
        "Aku akan menyuruhnya kembali. Semua orang di rumah khawatir":
            call scene_morune_02_01
        "Aku akan memberikannya nasehat meskipun aku tidak tau apa keinginan sebarnya dia"
            jump scene_morune_02_02

label scene_morune_02_01:
    gk "Hooh, nasehat apa?"
    a "Seorang gadis tidak layak keluar malam-malam karena itu berbahaya. masa depan ia masih panjang."

label scene_morune_02_02:
    gk "Apa kau khawatir tentang dia?"
    a "Tentu saja! meskipun jarang berbicara aku tetap khawatir."
    extend " Karena aku taku kehilangan seseorang lagi"
