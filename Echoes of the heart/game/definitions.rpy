# Fichier de definitions des images, fichier ect...

define m = Character('Maman', color="#76946d")
define iz = Character('Izu', color="#fca2e1")
define mi= Character('Misute', color="#d12c2c")
define ya = Character('Yamano', color="#3f1370")
define yu = Character('Yuzu', color="#ffeb77")
define ho = Character('Hotaru', color="#55ddd2")   
define co = Character('Coach', color="#858585")   
define mc = Character("[mc]", color="#1feb18")
define sfx = Character("", color="#000000")
define n = Character("", color="#000000")

define n_nvl = Character("Nighten", kind=nvl, image="nighten", callback=Phone_SendSound)
define e_nvl = Character("Eileen", kind=nvl, callback=Phone_ReceiveSound)
define yukiko_nvl = Character("Yukiko", kind=nvl, callback=Phone_ReceiveSound)
define airi_nvl = Character("Airi", kind=nvl, callback=Phone_ReceiveSound)
define kagayai_nvl = Character("Kagayai", kind=nvl, callback=Phone_ReceiveSound)
define yuzu_nvl = Character("Yuzu", kind=nvl, callback=Phone_ReceiveSound)
define hotaru_nvl = Character("Hotaru", kind=nvl, callback=Phone_ReceiveSound)
define anon_nvl = Character("Numéro Inconnu", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)