class Dosya4():

    def __init__(self,):
        with open("mailler.txt", "r", encoding="utf-8") as file:

            liste1 = []
            satirlar1 = file.readlines()

            ayikla1 = file.readline()

            self.satirlar_listesi = list()

            for i in satirlar1:
                self.satirlar_listesi.append(i)

            for i in self.satirlar_listesi:

        # founds the specific characters for an e-mail adress if there is counts

                y = i.endswith(".com\n")
                s = i.count(".")
                z = i.find("@")

                if z == -1:

                    print("@ kullanılmayan bir e posta türü saptandı.")

                if y == True and z != -1 and s < 3:
                    liste1.append(i)

                    print("e-postanın sonunda .com olduğu tespit edildi ve listeye eklendi.")
                    print(liste1)

        # adds another txt file verified e-mail adresses
        with open("gerçek_mailler.txt", "w", encoding="utf-8") as file2:

            print("txt dosyası oluşturulmuş durumda")

            for i in liste1:

                file2.writelines(i)








dosya4 = Dosya4()


















