label scene_chikka_01:

    a "Baiklah"

    a "Aku akan menunggunya"

    #bg_depanrumahpagiberubahsiang

    #bg_berpindahlorongdilantai_2

    a "kau sudah pulang chikka?"

    c "ada apa? kau menungguku?"

    a "bisakah aku minta tolong padamu?"

    c "Ha!? tumben sekali"

    a "aku butuh referensi komik"

    c "heh!?"

    c "apa kau ingin melihat tubuhku!?"

    a "tidak!"

    a "bukan itu yang kumaksud"

label scene_chikka_02:

    c "Dasar mesum!!"

    a "Hee!?"

    #SFX Brak Menutup Pintu

    a "apa-apaan sifat tsunderenya itu"

    k "ada apa keributan apa?"

    a "ahh tidak"

    #Suara dari kamar

    c "(A) Mesum Bi!"

    menu:
        "Menghampiri C":
            jump scene_chikka_02_01
        "Membiarkan C":
            jump scene_chikka_02_02

label scene_chikka_02_01:

    a "C, aku bisa menjelaskan maksud dari perkataanku tadi,"

    a "Jadi aku mohon bukakan pintu ini"

    c "Tidak! Jika kamu masuk,"

    c "Nanti kamu akan berbuat macam-macam kepadaku sebagai referensi Komikmu,"

    c "Aku tidak mau Titik!"

    a "Tolonglah C, aku sangat membutuhkan referensi Komik"

    c "Benarkah? Benarkah kau bias menjaga ucapanmu itu?"

    a "Benar"

    c "Baiklah jika kamu berkata begitu, besok saja kau dating lagi kesini"

    a "Sankyu"

label scene_chikka_02_02:

    #A bangun

    menu:
        "Menghampiri C":
            jump scene_chikka_02_01_01
        "Tidak menghampiri kamar C untuk sarapan":
            jump scene_chikka_02_01_02

label scene_chikka_02_01_01:

    #C sudah bangun dan diajak sarapan oleh A

    a "C, ayo kita sarapan"

    c "Iya! Meskipun tidak kamu beritahu aku bakal turun buat sarapan kok,"

    c "Lagian kenapa kamu datang ke kamarku?!"

    a "Aku kemarin kan sudah bilang, aku nanti minta referensi untuk komik kepadamu"

    c "Baiklah Baiklah"

    #Selesai sarapan

    a "Jadi? Kita akan bicara tentang referensi di kamarmu ya?"

    c "Ke-kenapa harus di kamarku?!"
    a "Karena kamarku penuh dengan Sampah"

    c "Aa~ Ternyata kamu jorok juga ya"

    a "Bukan begitu, aku kan Komikus"

    c "Baiklah, ayo ke kamarku, jangan sentuh apapun ya"

    a "Baiklah"

    #BG kamar C

    #A dan C masuk ke kamar

    c "Duduklah dibawah ya, jangan sentuh apapun"

    a "Baiklah"

    c "Jadi, kamu mau meminta referensi Komik tentang apa?"

    a "Sebelum itu, bisakah kita memperkenalkan diri lebih dalam lagi?"

    c "Hee?!"

    c "Apakah kau menginginkan sesuatu dariku?"

    a "Tidak tidak, aku hanya ingin dekat dengan lawan diskusiku, jadi wajar dong"

    c "Apakah yang seperti itu memang harus diperlukan?"

    a "Tidak sih, tetapi aku kan tinggal di dekatmu juga,"

    a "Kalau kamu kenapa-napa nanti kan aku tidak tahu,"

    a "Misal-nya kalau kamu sakit"

    c "Benar sih, tapi tetap saja…"

    c "Menceritakan masa laluku atau kehidupanku kepada Orang lain,"

    c "Terutama kepada Laki-laki,"

    c "Tapi kau janji tidak memberitahu ke siapa-siapa ya?!"

    a "Baiklah, ini hanya rahasia kita berdua"

    c "Ehh, kita berdua?"

    a "Iya"

    c "Kalau begitu besok lagi saja kau datang kesini,"

    c "Agar aku mengingat masa laluku dulu, ya?"

    a "Iya"

label scene_chikka_03:

label scene_chikka_04:

    #Keesokan hari-nya

    #BG lorong

    #A bangun dan menghampiri C

    #C Telat masuk sekolah dan terburu-buru untuk berangkat ke sekolah

    a "Ohay-"

    #C dengan tergesa-gesa membuka pintu

    #C menabrak A

    #C kaget

    c "Kenapa kamu disini! A"

    a "Aku kesini hanya untuk menyapamu"

    c "Hanya untuk menyapaku? Yang lebih penting, aku sudah telat sekolah, aku buru-buru"

    a "Baiklah, Itterasshai~"

    #Sore hari setelah pulang sekolah

    #BG kamar C

    #C Langsung berbaring di atas Kasur-nya karena kelelahan

    c "C: Hari ini melelahkan sekali ya, Ujian-nya lumayan berat"

    #A menghampiri kamar C

    #A mengetuk pintu kamar C

    a "A: A, apakah aku boleh masuk ke kamarmu?"

    c "Hee! Tunggu sebentar, aku masih belum ganti Baju"

    a "Baiklah"

    #BG kamar C

    c "Masuklah, aku sedang lumayan lelah saat ini, jadi aku tidak akan banyak bergerak"

    a "Lelah? Apakah kamu baru mengerjakan Ujian?"

    c "Ya begitulah, Ujian yang lumayan Berat"

    a "Boleh aku liat nilaimu?"

    menu:
        "Melihat nilai C":
            jump scene_chikka_04_01
        "Tidak melihat nilai C":
            jump scene_chikka_04_02

label scene_chikka_04_01:

    a "Hee, nilaimu lumayan bagus juga rupa-nya"

    c "Iya, tapi aku lelah sekarang, aku harus belajar banyak hal"

    a "Baiklah, aku akan segera menanyai, bagaimana tentang kehidupanmu dulu?"

    c ": Kehidupanku dulu ya, bisa dikatakan kalau aku dulu mempunyai penyakit…"

    a "Penyakit? Penyakit apa itu?"

    c "Kanker..."

    a "Sejak kapan kamu mengalami kanker itu?"

    c "Sejak aku kelas SD"

    c "Kata Dokter itu bawaan dari lingkungan sekitar"

    menu:
        "Bagaimana tentang sekolahmu dulu?":
            jump scene_chikka_04_01_01
        "Diam":
            jump scene_chikka_04_01_02
        "Apa ada orang yang mengetahui tentang penyakitmu itu dulu?":
            jump scene_chikka_04_01_03

label scene_chikka_04_01_03:

    c "Kau tahu? Orang Tuaku dulu saat mengetahui kalau aku mempunyai Kanker..."

    c "Mereka tidak bisa membawaku ke Rumah Sakit karena pada saat itu keluargaku ekonomi-nya kurang"

    c "Jadi..."

    c "Mereka putus asa, tapi aku tidak mau putus asa hanya karena aku mempunyai penyakit Kanker,"

    c "Aku akan terus berusaha,"

    c "Meskipun aku mengetahui kalau suatu saat aku akan mati"

    c "Aku masih mempunyai impian yang harus aku capai, agar aku bisa membanggakan mereka"

    c "Bagaimana? Sangat tragis bukan?"

    menu:
        "Ya, sangat tragis":
            jump scene_chikka_04_01_01_01
        "Tidak, itu cerita yang menyentuh":
            jump scene_chikka_04_01_01_02
        "Bagaimana ya..":
            jump scene_chikka_04_01_01_03

label scene_chikka_04_01_01_03:

    c "Meskipun aku sudah dicap tidak bisa hidup lama lagi, aku tidak peduli."

    c " Soal-nya jika aku tidak melakukan apa-apa, maka kehidupanku akan sia-sia, ‘kan?"

    a "Iya, kamu benar…"

    c "..."

    a "Tetapi, kamu sekarang berada disini kan? Di tempat yang orang lain peduli padamu, kamu tidak usah menutup diri lagi, karena kami menyambutmu dengan hangat, bahkan dengan kasih sayang"

    c "Iya, kamu benar, sebaik-nya aku tidak bersedih kan, terima kasih. Kamu telah memotivasiku, aku jadi sedikit tenang"

    c "Souyeba, ini sudah larut Malam, aku jadi terbawa suasana tadi sampai tidak melihat Jam, apakah bisa kita teruskan besok mencari referensi komik untukmu"

    a "Besok ya.."

    c "Ada apa?"

    a "Tidak, aku tiba-tiba terlintas sesuatu"

    c "Apa itu?"

    a "Entahlah"

    c "Cepat tidur sana, atau kalua tidak kau akan mimpi buruk"

    a "Baiklah, Oyasumi"

    c "Oyasumi Nasai"

label scene_chikka_05:

    #BG lorong

    #A bangun dan menghampiri kamar C

    #C mulai berangkat ke sekolah

    a "Ohayou, C"

    c "Ohayou, aku akan berangkat"

    a "Itterasshai~"

    c "Pagi-pagi jangan malas, nanti Istrimu akan malas juga loh untuk mengurusimu"

    a "Kalau Istriku nanti kamu bagaimana?"

    c "B-b-baka! Tentu saja tidak mungkin bodoh"

    a "Iya iya, berangkatlah sana"

    c "Dah"

    a "Dah"

    #BG Rumah

    #C pulang dan tidur di Sofa

    #A menghampiri C

    a "Kenapa kamu malah tidur di Sofa?"

    c "Terserahku kan! Lagian aku mau santai-santai setelah pulang dari sekolah"

    a "Jangan lupa makan atau kamu nanti sakit"

    c "Kenapa kau sangat perhatian kepadaku? Kau sendiri bagaimana?"

    a "Sudah dong, justru kamu yang harus lebih memerhatikan keadaan dan kesehatanmu"

    c "Apa kau kesini cuma mau mengingatkanku makan?"

    a "Tidak, aku nanti berencana akan meminta pendapatmu untuk Karakter Utama di Komikku"

    c "Kenapa kau terus meminta kepadaku saja? Yang lain bagaimana?"

    a "Yang lain sedang sibuk, kalau kau kan masih SMP, jadi banyak waktu luang"

    c "Fuyukai desu"

    #BG kamar C

    a "Ojamashimasu, C-san"

    c "Hey bodoh! Kenapa kau tidak mengetuk Pintu terlebih dahulu sebelum masuk?"

    c "Bagaimana kalau nanti ternyata saat kau membuka pintu aku sedang ganti Baju?"

    c "Apa jangan-jangan kau ini Hentai"

    a "Aku tidak bermaksud begitu, Deadlineku untuk pembuatan Komik tinggal sebentar lagi, besok aku sudah harus mengerjakan Komik-nya, dan aku masih belum mendapatkan Ide, maka-nya aku segera bergegas untuk ke Kamarmu"

    c "Tapi tau aturan juga, dasar"

    a "Maaf-maaf. Jadi, kau ada waktu luang kan?"

    c "Ada"

    a "Baiklah, aku akan meminta waktumu"

    c "Apakah kau bermaksud mengambil nyawaku?!"

    a "Tidak-tidak, maksudku ayo kita berdiskusi untuk pemeran utama di Komikku"

    c "Memang-nya Komikmu mengangkat tema tentang apa?"

    a "Tentang kamu, mungkin?"

    c "Hee, tentangku? Kau bodoh beneran ya?"

    a "Datte sa, hidupku selama ini kebanyakan ditempati oleh orang Kost, terutama kamu, maka-nya aku buat Tema tentangmu"

    c "Memang-nya tidak ada hal lain yang bisa menginspirasimu?"

    a " Aku kehabisan ide"

    c "Hmm.."

    a "Bagaimana?"

    c "Boleh saja"

    a "Beneran"

    c "Iya, bener"

    a "Baiklah, mari kita mulai"

    c "Bagaimana kalau kita mulai dengan Tokoh-nya dulu?"

    a "Boleh"

    a "Bagaimana kalau sifatmu ada juga disini?"

    c "Sifatku?"

    a "Iya, kan aku membuat komik tentangmu, jadi sifatmu juga harus ada disini"

    c "Iya, memang-nya kau tau sifatku apa saja?"

    a "Etto.. Mungkin Pemalu, Penyendiri, tapi ternyata baik?"

    c "Memang-nya a-aku seperti itu?"

    a "Iya, kan aku sering berada di dekatmu"

    c "T-tapi kenapa kau juga bisa sangat tau akan sifatku? Apa kau memerhatikanku?"

    a "Mungkin ya"

    c "Hee"

label scene_chikka_06:

    #BG lorong

    #A baru bangun begitu juga dengan C

    #C sudah mau berangkat ke sekolah

    a "Ohayou, C"

    c "O-ohayou"

    a "Nanti setelah kamu pulang sekolah, aku akan menggarap Komik yang telah kita bahas kemarin"

    c "Iyaa"

    #BG rumah

    #C sudah pulang dari sekolah

    c "Tadaimaa"

    a "Okaeri Nasai"

    c "Huft, lelah-nya"

    c "Aku akan mandi dulu ya"

    a "Iya, yang bersih ya"

    c "Ya jelas, bodoh"

    #BG Lorong

    a "Moshi-Moshi, C?"

    c "Hai’?"

    a "Apakah aku boleh masuk?"

    c "Sebentar lagi, awas jika kau mencoba untuk membuka Pintu itu"

    a "Hai hai’"

    c "Masuklah"

    a "Hai’, Ojamashimasu"

    a "Aku akan memulai untuk menggarap Ceritaku"

    c "Aku akan jadi pendengar dulu kan"

    menu:
        "Menceritakan hasil yang sudah dibuat":
            jump scene_chikka_06_01
        "Tidak menceritakan hasil yang telah dibuat":
            jump scene_chikka_06_02

label scene_chikka_06_01:

    a "Iya, aku akan bacakan kerangka ceritaku dulu yang sudah aku buat kemarin, meskipun ada yang berantakan (Setelah Diceritakan)"

    c "Wah, itu sudah bagus cerita-nya, hanya saja kurang dalam pengembangan cerita"

    a "Bagian mana-nya?"

    c "Ini(Sambil menunjukkan bagian yang kurang)"

    a "Owh, begitu. Jadi, bagaimana aku harus mengembangkan-nya?"

    c "Kau harus mengembangkan karakter dengan pelan-pelan, dan diikuti Orientasi yang pas, jangan terlalu terburu-buru untuk mengejar langsung ke Inti cerita"

    a "Begitu ya, akan aku perbaiki, terima kasih C"

    c "Bukan apa-apa kok, lagian kan lebih baik dikerjakan dnegan 2 Orang daripada sendirian"

    a "Sudah kuperbaiki, bagaimana?"

    c "Hmm.. Mungkin ini sudah bagus"

    c "Kapan kau akan mengirimkan hasil cerita ini?"

    a "Besok, dan Besok Lusa sudah diumumkan pemenang-nya"

    c "Deadline yang sangat mepet ya"

    a "Begitulah"

    a "Ya sudah, kita akhiri saja disini, sudah selesai. Besok aku akan megumpulkan-nya saat kamu sekolah"

    c "Hai’, lagipula aku sekarang juga sudah mengantuk"

    a "Oyasumi"

    c "Oyasumi Nasai"

label scene_chikka_07:

    #BG Lorong

    #A menghampiri C dan menyapa C yang akan berangkat ke sekolah

    a "Ohayou"

    c "Ohayou mo"

    a "Hati-hati ya"

    c "Baiklah, dan jangan lupa kalau kau akan mengumpulkan hasil komikmu kan?"

    a "Ah iya, hari ini tepat dikumpulkan"

    c "Iya, aku akan berangkat dulu"

    #Masih pagi

    #BG rumah

    #C pulang

    a "C, kenapa kamu pulang lebih cepat hari ini? Apakah kamu sakit?"

    c "Aku hanya tidak enak badan kok, bagaimana dengan komikmu?"

    a "Oh Komikku, sudah aku kumpulkan, dan pengumuman pemenang-nya besok loh, aku sangat senang C. Karena kamu telah membantuku mengerjakan komik itu"

    c "A-aku tidak membantu apa-apa kok, aku hanya menyarankan"

    a "Meskipun begitu, terima kasih ya"

    c "Sama-sama"

    a "Bagaimana kalau sebagai ucapan terima kasihku, aku mengajakmu ke suatu tempat?"

    c "Ehh, kemana?"

    a "Kita cari saja nanti di jalan"

    a "Ayo Naik"

    c "Hmm"

    a "Bagaimana rasa Es Krim-nya?"

    c "Enak"

    a"C.."

    c "Iya?"

    a "Apa benar kamu tidak apa-apa?"

    c "Tidak apa-apa, jangan khawatirkan aku, kalau aku istirahat yang cukup besok aku pasti sudah sembuh. Persiapkan dirimu buat besok, Senpai"

    a "Baiklah, akan kuantar kamu ya sampe kamar"

    c "Apakah kau mau mencabuliku? Cukup depan kamar saja"

    a "Baiklah"

label scene_chikka_08:

    #BG Rumah

    #A: C-C-C

    c "Ada apa Pagi-pagi sudah ribut begini? Berisik tau"

    a "Apakah kamu sudah baikan?"

    c "Lumayan"

    a "Aku Pagi ini sudah bersiap untuk pengumuman-nya, aku sangat gugup sekaligus senang"

    c "Berangkat sana"

    a "Kamu juga hati-hati ya"

    #Masih Pagi

    #BG Rumah

    a "Wahh aku menang, ini semua berkat C, aku sangat senang bisa dibantu oleh C. Aku harus berterima kasih kepada-nya"

    a "Eh? C tidak berangkat ke sekolah?"

    menu:
        "Pergi ke Kamar":
            jump scene_chikka_08_01
        "Menghampiri C":
            jump scene_chikka_08_02
        "Hanya memberitahu C tentang kemenangan-nya dalam kontes Komik":
            jump scene_chikka_08_03

    label scene_chikka_08_02:

    a "C, kenapa kamu tidak ke sekolah?"

    c "Aku sakit lagi"

    a "Sakit apa? "

    c "Sebenar-nya, Senpai. Aku punya penyakit, dan sekarang penyakitku kambuh dan mengharuskanku untuk operasi di Rumah Sakit, maaf ya telat memberitahumu."

    a "Apa kamu bilang? Jadi kemarin penyakitmu kambuh? Kenapa kamu diam saja, kalau kamu bilang begitu dari kemarin, aku bisa membawamu ke Rumah Sakit"

    c "Aku hanya tidak mau kau mengkhawatirkanku, karena Hari ini Komikmu diumumkan ‘kan? Bagaimana?"

    a "Jangan begitu, aku lebih baik mementingkan seseorang daripada Kontes Komikku. Bagus, aku menang"

    c "Seperti-nya hidupku tidak akan lama lagi"

    menu:
        "Memberi pertolongan pertama":
            jump scene_chikka_08_01_01
        "Tidak tau harus melakukan apa":
            jump scene_chikka_08_01_02
        "Membawa-nya ke Rumah Sakit":
            jump scene_chikka_08_01_03
        "Bersama-sama meratapi nasib dengan C":
            jump scene_chikka_08_01_04

label scene_chikka_08_01_03:

    a "Ayo, aku akan membawamu ke Rumah Sakit sekarang"

    c "Ehh?!"

    a "Jangan banyak protes"

    #BG Rumah Sakit

    a "Bagaimana tentang penyakitmu?"

    c "Dokter berkata.."

    a "Berkata?"

    c "Bahwa aku harus dioperasi besok"

    a "Apakah penyakitmu sungguh parah?"

    c "Mungkin, dan bisa saja aku besok mati"

    menu:
        "Jangan berkata begitu":
            jump scene_chikka_08_01_01_01
        "Kenapa kamu berkata begitu":
            jump scene_chikka_08_01_01_02
        "Besok kamu masih bisa hidup":
            jump scene_chikka_08_01_01_03
        "Kamu masih punya aku":
            jump scene_chikka_08_01_01_04

label scene_chikka_08_01_01_01:

    a "Jangan berkata begitu, kamu harus berjuang sampai besok saat operasi. Di Rumah banyak yang khawatir tentangmu"

    c "Baiklah, kau pulang sana, untuk apa repot-repot mengantarkanku ke Rumah Sakit segala, dasar Senpai bodoh"

    a "Tumben ya sekarang manggil memakai Senpai"

    c "Ehh, aku hanya keceplosan, jangan terlalu dianggap serius"

    a "Baiklah, aku akan pulang dulu ya, jaga kesehatanmu"

label scene_chikka_09:

    #BG Rumah Sakit

    a "Bagaimana rasa-nya tidur di Rumah Sakit? Apakah ada yang menghantuimu?"

    c "Yang begitu mana mungkin lah bodoh"

    a "Apakah kamu gugup?"

    c "Ya, sedikit"

    menu:
        "Aku akan mendo’akan yang terbaik untukmu":
            jump scene_chikka_09_01
        "Semoga bisa bertahan":
            jump scene_chikka_09_02
        "Jangan murung begitu":
            jump scene_chikka_09_03
        "Mungkin sudah saat-nya":
            jump scene_chikka_09_04

label scene_chikka_09_03:

    a "Jangan murung begitu"

    c "Aku tidak murung kok"

    a "Kalau kamu begitu berarti kamu sudah tidak gugup ya"

    c "Tapi, aku takut, bagaimana jika Operasi-nya tidak berjalan dengan lancar?"

    a "Bagaimana jika aku meninggal hari ini juga? Aku sangat ketakutan Senpai"

    #A Tiba-tiba memeluk C

    a "Tidak, operasimu pasti berhasil"

    #C Memanas

    c "Kau pulang sana, Operasi-nya masih lama, dan juga penjenguk hanya bisa menjenguk besok. Jadi jangan khawatirkan aku"

    menu:
        "Tidak, aku jelas khawatir":
            jump scene_chikka_09_01_01
        "Aku tidak khawatir":
            jump scene_chikka_09_01_02
        "Apakah it maumu?":
            jump scene_chikka_09_01_03

label scene_chikka_09_01_01:

    a "Tidak, aku jelas khawatir"

    c "Eh?"

    a "Bagaimana tidak khawatir, padahal aku sudah sangat dekat denganmu, bahkan saat-saat kamu membantuku untuk mengoreksi Komikku"

    c "Itu bukan apa-apa, aku hanya membantu sedikit"

    a "Tapi tetap saja"

    c "Ya sudah sana pergi, nanti kalau ikut dioperasi tau rasa loh"

    a "Iya, aku juga sudah membelikanmu sesuatu, aku taruh di Meja ya"

    c "Iya"

label scene_chikka_10:

    #BG Rumah Sakit
    a "Bagaimana operasi-nya? Apakah berjalan dengan lancar?"

    c "Hmp, berjalan dengan lancar, dan ternyata aku masih hidup"

    c "Terima kasih Senpai, karena kemarin sudah menyemangatiku, aku jadi tidak putus asa"

    a "Tidak apa-apa, aku juga senang kalau operasi-nya berjalan dengan lancar"

    c "Maaf ya, aku masih diharuskan banyak beristirahat, jadi Senpai dibatasi dalam menjenguk"

    a "Tidak apa-apa, aku sudah senang kalau melihatmu senang juga"

    c "Datanglah kesini besok"

    a "Pasti"

    c "Akan kutunggu ya"

    a "Iya"

label scene_chikka_11:

    #BG Rumah Sakit
    a "Apakah kamu sudah bagikan? Aku membawakanmu bubur, jika kamu mau makanlah"

    c "Benarkah?"

    a "Benar, mau aku suapkan?"

    c "Ehhh, kenapa kau menawarkan seperti itu?"

    a "Memang-nya kamu bisa makan dengan Tubuh begitu?"

    c "Tidak bisa"

    a "Baiklah, aku suapkan ya"

    a "Buka Mulut-nya dan bilang Aaa"

    c "Pelan-pelan, tiup dulu Bubur-nya"

    a "Iya-iya, aku tiupkan"

    c "Aaa"

    a "Enak?"

    c "Enak"
