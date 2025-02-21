# izobot
it's a Cigarette butt picking robot 
main branch contains codes and ROS2 nodes for computer, rpi branch contains codes and ROS2 nodes for actual izobot/raspberrypi. raspberrypi4 8GB model was used for this project.

izobot is abbrevation for izmarit picking bot, izmarit = cigarette but.

Izobot is designed for giving humans freedom to throw their cigarette butts without concerning about environmental polllution and also keep our university campus ,specially in front of the library, izo-free.

İlk başta insan hayatını tehlikeye atan işleri ve sürekli kendini tekrarlayan işleri
devralarak kullanılmaya başlanan robot teknolojileri artık yapay zekâ ve gelişen sensör
teknolojilerle daha kompleks işleri yapabilmektedir. Öncelikle global sorunlara çözüm
üretmek amacıyla geliştirilen bu teknolojinin kullanım alanlarından birisi de çevre
kirliliğini azaltmaya yönelik girişimlerdir. Bu amaç doğrultusunda okyanus yüzeyindeki
atıkların toplanmasında, atıkların ayrıştırılmasında, sokakların temizliğinde vb.
durumlarda otonom araçlar kullanılmaktadır. Günümüzde havaalanları, alışveriş
merkezleri, iş merkezleri gibi çok geniş alana yayılmış kapalı alanların zemin temizliği
işinde ve evlerde dahil robot süpürgeler kullanılmaktadır. Otonom temizlik robotlarının
çevresini algılama, haritalama ve birlikte hareket edebilme yetenekleri sayesinde
bulundukları ortamı %99’lara varan başarı oranıyla ve sürekli olarak temizlemesi,
insanların temizlik yapmasına kıyasla çok daha verimli bir yöntemdir. Bu şekilde hem
sürdürülebilirliğe hem de insanlara zaman kazandırması yönüyle otonom robotların
kullanım alanlarının giderek genişleyeceği öngörülmektedir. Bu öngörüye dayanarak
ileride sokaklarda ve parklarda otonom temizlik robotlarını görmeyi bekleyebiliriz.
Sokaklarda ve parklarda çevreyi kirleten etmenlerden birisi de sigara izmaritleridir Sigara
izmaritleri pek çok insanın dikkatinden kaçsa da hem çevre kirliliği hem de görüntü
kirliliği oluşturmaktadır. WHO (World Health Organization)’ un 2022 Dünya Tütünsüz
Gününde yayınladığı bildiriye göre yılda 6 trilyon sigara izmariti geride kalır ve bunun 4,5
trilyonu kontrolsüz şekilde doğaya atılmaktadır. Fransa’ da yürütülmüş bir çalışmaya
göre her yıl sigara izmaritlerini temizlenmesi için 100 milyon Euro harcanmaktadır [1].
Yine TÜSAD (Türkiye Solunum Araştırma Derneği)’ nin aynı günde yayınladığı bildiriye
göre Türkiye’ de sigara kullanım oranı tüm nüfusun %28’ ine denk gelmektedir yani
neredeyse her 10 kişiden 3’ ü sigara kullanmaktadır. Buna ek olarak 2018 yılında
ülkemizde 118,5 milyona yakın sigara tüketildiği açıklanmıştır [2]. Bu miktar
hesaplandığında yıllık 21 milyon kg, günlük 57 tonluk bir atık yük anlamına gelmektedir.

Sigara izmaritlerinde bir tür plastik olan selüloz asetat bulunmaktadır ve plastik uzun
vadede toprakta ve suda mikroplastik kontaminasyona yol açmaktadır. Sigara
izmaritinde kalan nikotin ve diğer zararlı bileşenler toprağa ve suya karıştığı takdirde
bitkilerin gelişimini yavaşlatmakta ve canlıların ölümüne neden olmaktadır [2]. Bütün bu
verilere baktığımızda ve İstanbul gibi büyük şehirleri ve belli zamanlarda insan
yoğunluğunun artmasına neden olan faaliyetlere sahip turizm şehirlerini göz önünde
bulundurduğumuz zaman park, bahçe, plaj vb. ortak kullanım alanlarında biriken
izmaritin çevre, sürdürülebilirlik ve insan sağlığı için tehlikeli olduğu çıkarımını
yapabiliriz. Aslında bu tarz ortak kullanım alanlarıyla günlük hayatımızda daha sıklıkla
karşılaşmaktayız. Örneğin üniversitelerin kampüslerinde bulunan çimenlik alanlar, sahil
bandlarındaki çimenlik alanlar, yürüyüş ve piknik alanları, kaldırımlar, toplu konut
bahçeleri gibi alanlar sigara kullanım oranları ve bu ortak kullanım alanlarının kullanım
sıklığı göz önüne alındığında yer yer izmarit birikintileri ile karşılaşma ihtimalimizin
yüksek olduğu yerlerdir. Bu izmaritlerin küçük yapıları nedeniyle ve çimenlerin arasında
gözle tespiti zor olması nedeniyle her zaman tam olarak temizlenmesi mümkün değildir.
Sonuç olarak izmaritler bu alanlarda rutin sulamalar ve yağışlarla birlikte toprağa
karışmakta veya akarsulara, denizlere karışmaktadır. Sigara filtreleri sigaradaki zararlı
maddeleri süzerler ve bu maddeleri yapılarında barındırırlar. Sigara izmaritinde bulunan
bu zararlı kimyasal maddeler hem toprakta yaşayan organizmalara zarar vermekte hem
de okyanuslardaki organizmaları kötü etkilemektedir. Dolayısıyla zaman geçtikçe bu
alanlarda kontaminasyonun artması, toprak verimliliğinin düşmesi, okyanustaki canlı
çeşitliliğinin azalması gibi sonuçlarla karşılaşmamız mümkündür.

Uzun yıllardır süregelen bu sorun çevreci kişilerin dikkatinden kaçmamıştır ki bu kirliliğin
önüne geçilebilmesi için birçok çözüm önerisi yayınlanmıştır. Şimdiye kadar sigara
izmaritlerinin geri dönüşümü için birçok yöntem geliştirilmiştir: briket üretimi, asfalt
üretimi,pestisit kontrolü, aktif karbon üretimi, biyofilm taşıyıcı, süperhidrophobic/süperleophilic
fiber üretimi, ses absorbe materyalleri, kâğıt üretimi, metal korozyon inhibitörü, 
li-on batarya membran ayracında kullanılmaktadır [3]. Bu tarz
geri dönüşüm yöntemlerinin sigara izmaritlerini geri dönüştürmede kullanılması hem
ekonomik açıdan hem de sürdürülebilirlik açısından faydalı olacaktır. Sigara 
izmaritlerinin toplanması sayesinde geri dönüşüm için daha fazla kaynak oluşturulması
sayesinde daha fazla ürün elde edilmesi ekonomik kazanç sağlayacaktır.

Yukarıda belirtilen sebeplerden ötürü izmaritlerin neden olduğu çevre kirliliğinin önüne
geçilebilmesi, sürdürülebilir çevre ve ekolojik dengelerin korunabilmesine katkıda
bulunması amacıyla bu projede otonom hareket edebilen, yapay zekâ sayesinde görüntü
işleyerek izmariti tespit edebilen ve depolayan, sürü olarak koordineli hareket ederek
alanın izmaritten arındırılmasını sağlayacak bir robot tasarlanacaktır. Bu robotların
birbirleri ile haberleşerek geniş alanları etkin bir şekilde taraması ve izmaritleri toplaması
planlanmaktadır. Belirlenen bir istasyon konumunda gerektiğinde enerjilerini
yenilemeleri ve depolarındaki atıkları uygun bir ortamda biriktirmeleri planlanmaktadır.
Böylece biriktirilen izmaritler daha sonra geri dönüşüm uygulanarak tekrar ekonomiye
kazandırılabilecek ve katma değer oluşturabilecektir. Ekonomik olarak geri
dönüştürülerek elde edilmiş ürünlerden gelir elde edilmesi, çevre sağlığı açısından
kirliliğin önüne geçilmesi dolayısıyla çeşitli canlıların hayatını tehlikeye atan durumun
ortadan kaldırılması başlıca faydalardır. Öte yandan izmaritlerin diğer atıklardan ayrı
olarak toplaması yönüyle atıkları ayrıştırma noktasında katkı sağlayacaktır.

