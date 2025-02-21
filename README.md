# izobot
it's a Cigarette butt picking robot 
main branch contains codes and ROS2 nodes for computer, rpi branch contains codes and ROS2 nodes for actual izobot/raspberrypi. raspberrypi4 8GB model was used for this project.

izobot is abbrevation for izmarit picking bot, izmarit = cigarette but.

Izobot is designed for giving humans freedom to throw their cigarette butts without concerning about environmental polllution and also keep our university campus ,specially in front of the library, izo-free.

ABSTRACT
Robot technologies, which were first used to take over jobs that endangered human life and constantly repetitive jobs, can now do more complex jobs with artificial intelligence and developing sensor technologies. One of the areas of use of this technology, which was developed primarily to produce solutions to global problems, is initiatives to reduce environmental pollution. For this purpose, autonomous vehicles are used in cases such as collecting waste on the ocean surface, separating waste, cleaning streets, etc. Today, robot vacuum cleaners are used in floor cleaning of very wide-spread indoor areas such as airports, shopping malls, business centers, and in homes. Thanks to the ability of autonomous cleaning robots to perceive, map and move together with their surroundings, they continuously clean the environment they are in with a success rate of up to 99%, which is a much more efficient method compared to human cleaning. In this way, it is predicted that the areas of use of autonomous robots will gradually expand in terms of both sustainability and saving people time. Based on this prediction, we can expect to see autonomous cleaning robots on streets and parks in the future.

One of the factors that pollute the environment on streets and parks is cigarette butts. Although cigarette butts escape the attention of many people, they cause both environmental and visual pollution. According to the declaration published by WHO (World Health Organization) on World No Tobacco Day 2022, 6 trillion cigarette butts are left behind every year, 4.5 trillion of which are uncontrolledly thrown into nature. According to a study conducted in France, 100 million Euros are spent to clean cigarette butts every year [1].

According to the declaration published by TÜSAD (Turkish Respiratory Research Association) on the same day, the smoking rate in Turkey corresponds to 28% of the entire population, meaning that almost 3 out of every 10 people smoke. In addition, it was announced that nearly 118.5 million cigarettes were consumed in our country in 2018 [2]. When this amount is calculated, it means a waste load of 21 million kg per year and 57 tons per day.

Cigarette butts contain cellulose acetate, a type of plastic, and plastic causes microplastic contamination in the soil and water in the long term. If the nicotine and other harmful components left in cigarette butts mix with the soil and water, they slow down the development of plants and cause the death of living things [2]. When we look at all this data and consider big cities like Istanbul and tourism cities with activities that cause an increase in human density at certain times, we can conclude that butts accumulated in common areas such as parks, gardens, beaches, etc. are dangerous for the environment, sustainability, and human health. In fact, we encounter such common areas more frequently in our daily lives. For example, grassy areas on university campuses, grassy areas on coastal strips, walking and picnic areas, sidewalks, and public housing gardens are places where we are likely to encounter cigarette butt accumulations in places, considering the smoking rates and the frequency of use of these common areas. Due to the small structure of these cigarette butts and the difficulty of detecting them with the eye among the grass, it is not always possible to clean them completely. As a result, cigarette butts mix with the soil in these areas with routine irrigation and rainfall, or mix with streams and seas. Cigarette filters filter the harmful substances in cigarettes and contain these substances in their structures. These harmful chemicals found in cigarette butts both harm organisms living in the soil and adversely affect organisms in the oceans. Therefore, it is possible for us to encounter consequences such as increased contamination in these areas, decreased soil fertility, and decreased diversity of life in the ocean as time passes.

This problem, which has been going on for many years, has not escaped the attention of environmentalists, and many solutions have been published to prevent this pollution. Many methods have been developed for the recycling of cigarette butts so far: briquette production, asphalt production, pesticide control, active carbon production, biofilm carrier, superhydrophobic/superleophilic fiber production, sound absorbing materials, paper production, metal corrosion inhibitor, and li-on battery membrane separator [3]. The use of such recycling methods in recycling cigarette butts will be beneficial both economically and in terms of sustainability. The collection of cigarette butts will provide more resources for recycling, and thus, more products will be obtained economically.

For the reasons mentioned above, environmental pollution caused by butts can be prevented. In order to contribute to the preservation of sustainable environmental and ecological balances, a robot that can move autonomously, detect and store cigarette butts by processing images with artificial intelligence, and act in a coordinated manner as a herd to ensure that the area is cleared of cigarette butts will be designed in this project. It is planned that these robots will communicate with each other and effectively scan large areas and collect cigarette butts. It is planned that they will renew their energy when necessary at a designated station location and collect the waste in their storage in a suitable environment. Thus, the cigarette butts collected will later be recycled and returned to the economy and create added value. The main benefits are to obtain income from products obtained by recycling economically, to prevent pollution in terms of environmental health, and to eliminate the situation that endangers the lives of various living creatures. On the other hand, collecting cigarette butts separately from other wastes will contribute to the separation of waste.

ÖZET
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

[1] World Health Organization, «World No Tobacco Day,» 2022.
[2] Türkiye Solunum Araştırtmaları Derneği, «www.solunum.org.tr,» 30 Mayıs 2022.
[Çevrimiçi]. Available: https://www.solunum.org.tr/haber/1516/31-mayis-dunya-
tutunsuz-gunu-basin-bildirisi.html.
[3] M. F. Javad Torkashvand, «A systematic rewiev on cigarette butt management as a
hazardous waste and prevelant litter: control and recycling,» Environmental
Science and Pollution Research, 2019.

