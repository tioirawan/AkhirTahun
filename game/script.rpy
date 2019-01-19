default persistent.playername = ""
default player = persistent.playername

define a = DynamicCharacter("player")
define c = Character("Chikka")
define gk = Character("?")
define k = Character("Kyoko")
define l = Character("Lora")
define m = Character("Morune")

#SCENE
image bg white = "bg_white.png"
image bg black = "bg_black.png"
image bg tree = "scene_tree.png"
image bg intro = "scene_intro.png"
image bg city = "scene_city.png"
image bg bighouse = "scene_bighouse.png"
image bg kamar_a = "scene_kamar_a.png"
image bg lorong = "scene_lorong.png"
image bg makan = "scene_makan.png"
image bg kamar_a_sore = "scene_kamar_a_sore.png"
image bg kamar_tidur_malam = "scene_kamar_tidur_malam.png"
image bg teras_sore = "scene_teras_sore.png"
image bg teras_malam = "scene_teras_malam.png"
image bg lorong_2 = "scene_lorong_2.png"
image bg rumah_malam = "scene_rumah_malam.png"
image bg gang_kecil = "scene_gang_kecil.png"
image bg ruang_keluarga = "scene_ruang_keluarga.png"
image bg depan_rumah = "scene_depan_rumah.png"
image bg lantai_3 = "scene_lantai_3.png"
image bg kamar_lora = "scene_kamar_lora.png"
image bg lantai_3_sore = "scene_lantai_3_sore.png"
image bg lantai_3_malam = "scene_lantai_3_malam.png"
image bg kamar_lora = "scene_kamar_lora.png"
image bg depan_supermarket = "scene_depan_supermarket.png"
image bg depan_perpus = "scene_depan_perpus.png"
image bg suatutempat = "scene_suatutempat.png"
image bg pantai = "scene_pantai.png"
image bg kamar_chikka = "scene_kamar_chikka.png"
image bg lorong_sakit = "scene_lorong_sakit.jpg"

#Character

image lora biasa = "char/lora biasa.png"
image chikka marah = "char/chikka marah.png"

#Position
transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0


#define white_fade = fade(0.1, 2.0, 0.5, color="#fff")

label start:
    call splashscreens
    jump scene_00

label scene_00:


    scene bg white with fade
    # hide bg white with fade
    $ renpy.pause(2.0)
    scene bg intro with dissolve
    $ renpy.pause(1.0)


    # These display lines of dialogue.

    gk "Hey...."

    a "Iya..."

    gk "Apa kita bisa bertemu lagi?"

    a "Entahlah..."

    gk "Tak kusangka kita akan berpisah"

    a "Iya"

    gk "Ehm....."

    gk "Ini untukmu"

    a "Apa ini?"

    a "Sebuah kado?"

    gk "Jangan kamu buka disini."

    gk "Bukalah di rumah baru mu."

    a "Baik..."

    scene bg black with dissolve
    $renpy.pause(1.0)

    scene bg city with fade

    "Aku pergi ke kota yang amat besar"

    "Aku kehilangan desa karena orangtuaku telah meninggal akibat kecelakaan"

    "Rumahku akhirnya di jual"

    "Tetapi ayahku mempunyai rumah di kota ini sekaligus ada pemiliknya"

    "Inilah kehidupanku sekarang"

    scene bg bighouse with fade

    "Aku tinggal di rumah yang besar ini"

    "Tetapi aku tidak sendirian. . ."

    scene bg kamar_a with fade
    $renpy.pause(1.0)

    play audio "alarm_jam.mp3"

    pause 1

    a "Ah. . ."

    a "...."

    a "Jam segini ya...."

    gk "[player] ayo cepat bangun, sarapan sudah siap."

    a "Baik"

    scene bg lorong with fade
    $renpy.pause(1.0)

    # "*Brak....."
    with hpunch

    a "Aduhhh...."

    gk "Aduhh, sakit....."

    a "Ohh maaf Cikko" 

    show chikka marah with dissolve

    c "Hati-hati dong [player] duhh"

    c "Kakiku jadi sakit nih"

    a "Maaf-maaf"

    c "Kalau jalan it-"

    k "Ayo cepat"

    # hide chikka marah with dissolve
    show chikka kaget with dissolve

    c "Ba-baik. . ."

    hide chikka kaget with dissolve

    a "Haduh dasar anak itu kalau sudah emosi gak bisa di berhentiin"

    $renpy.pause(1.0)

    scene bg makan with fade

    show kyoko biasa 1

    k "Makanan mu sudah siap [player]"

    a "Baik..."

    "Namanya adalah kyoko"

    "Semenjak lulus kuliah ia disuruh orangtua ku menjaga rumah ini"

    "Dulu ia anak kos disini"

    "Tetapi ayahku justru memberikan kepercayaan untuk menjaga rumah ini dan menjaga ibu kos."

    k "Omong-omong [player], apa kau melihat Morune?"

    a "Tidak aku tidak melihatnya"

    show kyoko biasa 2

    k "Apa dia ketiduran di perpustakaan umum lagi? ya ampun"

    "Morune. ia tinggal di lantai 3"

    "Ia berada disebelah kamarku"

    "Karena terlalu diam dan misterius. keberadaannya hampir saja tidak terasa"

    scene bg lorong with fade

    show lora biasa

    l "Bu, aku pergi dulu. . ."

    k "Udah sarapan?"

    l "Sudah..."

    "Namanya Lora"

    "Ia berada di lantai 2"

    "Wanita paling ceria, energik, dan sosial tinggi"

    show chikka kaget at slightleft with dissolve
    show lora biasa at slightright  with dissolve

    c "Aduhhhh gawaaat..."

    k "Ada apa?"

    c "PR ku belum kukerjakan!"

    k "Heh?"

    show chikka biasa at slightleft with dissolve

    c "Oke bi aku berangkat. aku kerjakan di sekolah"

    hide lora biasa with dissolve
    hide chikka biasa with dissolve

    "Nama anak itu Cikka"

    "Kelas 3 smp, sifat tsundere minta ampun"

    "Meskipun begitu dia memiliki bakat tetap menjalani hidup"

    "Walau katanya sebenarnya dia sakit."

    $renpy.pause(1.0)

    show kyoko nanya with dissolve

    k "Omong-omong [player]"

    a "Iya?"

    k "Apa pekerjaanmu sudah selesai?"

    a "Ohh komik? sudah tante"

    show kyoko biasa 2 with dissolve

    k "Ho-oh"

    k "Kapan-kapan liat ya"

    a "Iya"

    hide kyoko biasa 2  with dissolve

    "Pekerjaanku komikus"

    "Aku sudah lulus sekolah"

    "Aku mendapatkan uang dari komik"

    #hide kyoko senyum

    $renpy.pause(1.0)

label scene_000:

    scene bg makan with fade

    "Setelah makan"

    show kyoko biasa 2 with dissolve

    a "terimakasih nte"

    k "Ya sama-sama"

    hide kyoko biasa 2  with dissolve

    gk "Aku pulang"

    a "Morune!?"

    show morune capek  with dissolve

    m "Ada apa?"

    a "Bukankah ini jam masuk sekolah?"

    m "Maaf aku capek"

    k "Apa kau tak enak badan morune?"

    m "...."

    "Namanya Morune"

    "Ia seorang genius"

    "Selalu ranking 1"

    "Tetapi tidak ada teman atau seorang yang dekat dengan dia."

    "....."

    hide morune capek  with dissolve

    a "Oh iya"

    a "Aku harus selesaiin komikku untuk lomba mendatang."

    scene bg kamar_a with fade

    a "Hmm tak ada refrensi"

    a "Apa yang mau aku lakukan ya. . ."

    a "Mungkin untuk mengisi waktu luangku aku mencoba mendekat ke salah satu perempuan di kos ini"

    a "Siapa tau aku dapat refrensi untuk komik yang akan datang"

    menu:
        "Lora":
            jump scene_lora_01
        "Morune":
            jump scene_morune_01
        "Chikka":
            jump gksido_chikka
        "Kyoko":
            jump gksido_kyoko

label gksido_kyoko:

    a "mungkin dia masih sibuk"

    a "yang lain saja"

    menu:
        "Lora":
            jump scene_lora_01
        "Morune":
            jump gksido_moruna
        "Chikka":
            jump gksido_chikka


label gksido_moruna:

    a "mungkin dia masih sibuk"

    a "yang lain saja"

    menu:
        "Lora":
            jump scene_lora_01
        "Kyoko":
            jump gksido_kyoko
        "Chikka":
            jump gksido_chikka

label gksido_chikka:

    a "mungkin dia masih sibuk"

    a "yang lain saja"

    menu:
        "Lora":
            jump scene_lora_01
        "Morune":
            jump gksido_moruna
        "Kyoko":
            jump gksido_kyoko



    return
