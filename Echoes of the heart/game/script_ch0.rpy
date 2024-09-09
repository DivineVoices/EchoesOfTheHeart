label ch0:
    stop music fadeout 4.0 
    show black with dissolve

    pause(3.5)
    camera:
        perspective True

    play audio "door.mp3"
    sfx "toc toc toc"
    n "Un bâillement m'échappe"
    window auto hide
    camera:
        subpixel True 
        zpos -234.0 
        easein_cubic 3.23 zpos 0.0 
    show bedroom:
        subpixel True blend None 
        alpha 0.0 
        linear 3.23 alpha 1.0 
    with Pause(3.33)
    camera:
        zpos 0.0 
    show bedroom:
        alpha 1.0 
    window auto show

    play music "Love in the Codes.mp3" 
    m "Allez mon chéri, on n'a pas déménagé à Takayama pour que tu dormes toute la journée"
    m "J'ai préparé ton plat préféré, il faut bien commencer la journée, non ? "
    n "La porte reste ouverte tandis que mes yeux s'habituent à la lumière vive qui pénètre"
    n "Elle a raison, étant donné que tout le monde à l'école se connaît déjà, il faut que je sois en pleine forme si je veux faire bonne impression"
    n "Je mets rapidement mon uniforme tout neuf et je sors dans le salon"
    n "L'odeur de délicieux pain perdu emplit l'air."
    n "Mais je ne m'y attarde pas trop longtemps, car je suis déjà sur le point d'être en retard, maman avait raison de dire que je suis un gros dormeur"
    n "Avec le ventre plein et beaucoup de motivation, je me précipite hors de la maison à toute vitesse"
    show school with in_eye
    n "Nous y voilà... Ce n'est pas si intimidant quand on s'approche."
    n "Jusqu'à ce que la réalisation que c'est un moment décisif pour ma vie sociale frappe ; et tout à coup, c'est extrêmement intimidant"
    n "Mais plus j'y pense, plus je vais stresser, alors il est temps de se mettre en route et d'essayer de parler aux gens."
    n "Voyons ce qui semble intéressant."

    menu line:
        "Bibliothèque":
            play audio "select.mp3"
            jump ch0_hotaru
        "BDE":
            play audio "select.mp3"
            jump ch0_yuzu
        "Terrain de sport":
            play audio "select.mp3"
            mc "Le terrain de sport semble être un bon endroit pour la camaraderie, peut-être que je m'intégrerai plus facilement dans un groupe"
            jump ch0_misuto
        "Club de théatre":
            play audio "select.mp3"
            jump ch0_yamano
        "Allez en classe":
            play audio "select.mp3"
            jump ch0_izu           
    return


label ch0_hotaru:

    return



label ch0_izu:

    return



label ch0_misuto:
    show sport with dissolve
    n "J'observais à travers une porte double entrouverte, et je remarque qu'un match de volley était en plein déroulement."
    n "Je décide alors d’entrer et c’est là qu’un ballon vient voltiger vers ma direction"
    un "Eh Mei ! Fais attention où tu tires la prochaine fois !"
    n "Une jeune fille vient de rattraper d’une vitesse le ballon qui arrivait à une vitesse fatale. Vêtue d’une veste sur l’uniforme scolaire, elle arborait une belle queue de cheval et un sourire radieux"
    show misute:
        zoom 0.34 
        xalign 0.5
    un "Ouf, désolée pour ça"
    un "Mei ne sait pas contrôler sa propre force, ça va ?"
    n "C’était un peu surprenant mais je ne suis pas à l'hôpital donc on peut considérer ça comme une victoire."
    menu:
        "Juste une petite frayeur":
            play audio "select.mp3"
            mc "Ça va, c'était juste une petite frayeur"
            mc "je vais m'en remettre"
            un "D'accord, super à entendre ! Je suis sûre que tu seras de nouveau sur pied en un rien de temps"
            n "Elle me fait asseoir sur les gradins un moment"
        "J'ai besoin d'un moment pour respirer":
            play audio "select.mp3"
            mc "C'était terrifiant..."
            mc "Je pense que j'ai besoin d'un moment..."
            mc "pour respirer"
            un "Je suis vraiment"
            un "vraiment"
            un "vraiment vraiment"
            un "VRAIMENT"
            un "désolée"
            un "tu as besoin d'aller à l'infirmerie ?"
            un "Je peux t'y emmener"
            n "Elle s'approche pour me soutenir sur son épaule"
            mc "J'ai juste besoin d'un moment, vraiment, tout va bien"
            n "Elle se redresse et me fait asseoir sur les gradins pour me reposer"
    un "Oh, au fait, je ne t'ai jamais vu au club de sport avant, puis-je connaître ton nom ?"
    mc "Ah bien sûr, je m'appelle [mc]! Mais tu peux m'appeler..."
    n "J'essaie de penser à un surnom cool... Mais rien ne me vient à l'esprit"
    mc "En fait, restons sur [mc]"
    mi "Okidoki [mc]! Juste pour info, moi c'est Misute."
    n "Misute regarde derriere elle"
    mi "Donne-moi une seconde"
    n "Misute retourne sur le terrain de volley et appelle une pause, puis elle revient vers moi pour discuter"
    mi "Alors ! Tu ne m'as pas dit pourquoi tu es ici, pourrais-je peut-être t'intéresser à des activités du club de sport ?"
    mi "Nous avons organisé une course pour aujourd'hui, si tu veux nous rejoindre, c'est le moment parfait !"
    
    menu:
        "Je suis toujours partant pour une course":
            play audio "select.mp3"
            mc "Une course, ça a l'air amusant ! Je suis toujours partant pour une course."
            mi "Génial ! Allons te faire inscrire et te préparer."
            mi "Ce sera une bonne occasion pour toi de rencontrer les autres aussi."
            n "Misute me conduit à une table où d'autres élèves sont rassemblés pour la course. Misute me prend ensuite par la main et me pousse soudainement sous les projecteurs devant tout le monde."
            mi "Hé tout le monde ! Voici [mc]. Il est nouveau ici, je m'attends à un accueil chaleureux de votre part !"
            n "La plupart des membres du club reprennent leurs conversations, mais certains viennent me dire bonjour, ainsi que me donner des high fives."
            n "Misute semble relativement ennuyée par le manque d'accueil chaleureux, elle prend la parole."
            mi "Peut-être qu'ils sont trop concentrés pour discuter. On y reviendra bientôt ! Allez, tu as une course à faire."
            n "Elle me tape sur le dos comme une personne qui ne sait pas comment faire la manœuvre de Heimlich, en essayant de son mieux."
            n "Le groupe se dirige vers le terrain. Misute commence à diriger les exercices d'échauffement, expliquant chaque mouvement en détail."
            mi "D'abord, nous ferons quelques étirements pour éviter les blessures. Touchez vos orteils, levez les bras vers le ciel, ce genre de choses. C'est bon ?"
            n "Nous suivons tous les étirements un par un, et nous les terminons relativement rapidement."
            
            menu:
                "Je m'éclate !":
                    play audio "select.mp3"
                    mc "C'est amusant ! Je ne me rendais pas compte à quel point ça m'avait manqué ce genre de chose."
                    mi "N'est-ce pas ? Rien de plus motivant que de se donner à fond avant une course vraiment importante."
                    mi "Il faut juste continuer à tout donner, de cette façon tu obtiens la plus grande récompense !"
                "Tout brûle...":
                    play audio "select.mp3"
                    mc "Tout brûle... Est-ce trop tard pour renoncer ?"
                    mi "Allez, ça veut dire que tu fais bien les choses !"
                    mi "Si tu commences quelque chose, vas jusqu'au bout ! La victoire sera d'autant plus douce à la fin, non ? Cela ne vaut-il pas tous ces efforts ?"
                    n "Paroles de véritable coach de motivation. Je suppose qu'elle a raison, bien que cela ne m'empêche pas de brûler de douleur."

            mi "Tiens, bois, il faut rester hydraté si tu veux gagner cette course !"
            mi "Cependant..."
            mi "Je vais participer aussi, mais je vais te soutenir pour que tu finisses deuxième !"
            n "Je ne pense pas qu'elle réalise que ce qu'elle dit sonne comme une insulte, mais la course est maintenant officiellement lancée. Pas de retour en arrière maintenant, surtout pas avec ce sourire narquois sur le visage de Misute."
            n "Je vois tout le monde finir leurs boissons, et un coach nous aligne tous sur la piste. Je jette un coup d'œil rapide à Misute, il y a du feu dans ses yeux, et une concentration totale."
            co "PRÊTS ?"
            n "Plus de coups d'œil, il est temps de se concentrer !"
            co "PARTEZ !"
            n "Le son du signal de départ résonne dans mes oreilles, et nous nous élançons tous en avant. L'adrénaline me propulse, mais je vois déjà Misute en tête, sa queue de cheval volant derrière elle comme une bannière de victoire qui me nargue."
            n "Je brûle de l'intérieur, mais je me pousse à suivre les autres, mes muscles tendus à chaque foulée. L'énergie compétitive est palpable."
            n "Misute est une ombre devant, ses jambes bougeant avec une telle rapidité et précision qu'elles me motivent à dépasser la douleur. Je dois me concentrer sur la course, rien n'est plus important maintenant."
            n "La sueur perle sur mon front, alors que je jette un coup d'œil aux concurrents à côté de moi ; leur détermination faiblissant légèrement."
            n "La ligne d'arrivée est en vue maintenant. La piste semble s'allonger, chaque mètre semblant infiniment plus long que le précédent. Je repousse mes limites, ma vision se focalisant sur la ligne d'arrivée."
            n "Et avec une dernière poussée d'énergie, je balance mes bras plus fort, mes jambes bougeant presque mécaniquement. Chaque muscle hurle de protestation, mais je dépasse la douleur, poussé par la pure volonté..."
            n "Je respire difficilement en franchissant la ligne d'arrivée, levant les yeux pour voir Misute déjà en train de boire une bouteille d'eau. Mon cœur battant comme un tambour."
            mi "Pas mal, pas mal du tout [mc] !"
            n "Elle rayonne, la sueur brillant sur son front. Je m'effondre sur l'herbe, respirant lourdement mais avec un sentiment d'accomplissement."
            mi "Bienvenue au club de sport, [mc]."
            n "Elle me tend la main pour me relever, j'ai vraiment besoin de me reposer après ça."
            n "Nous restons ensemble près des gradins, la détente envahit mon corps. Je ferme les yeux."

        "Parle-moi un peu de ce club":
            mc "Peux-tu me parler un peu plus du club de sport ?"
            mi "Bien sûr !"
            n "Misute s'assoit à côté de moi, parlant de tout ce qui lui vient à l'esprit en regardant le ciel."
            mi "Alors, notre club de sport est assez diversifié. Nous avons le volley dont je suis la capitaine, super excitant ! Nous avons le football, un de mes favoris personnels, nous avons nos amis de l'athlétisme, et même une équipe de natation si tu es prêt à te jeter à l'eau."
            mc "Wow, tu as beaucoup à gérer, ça ne devient pas fatiguant à la longue ?"
            mi "Psh- non, je gère tout en étant la meilleure version de moi-même, et tu ne me vois pas rouiller, n'est-ce pas ?" 
            mi "En plus, nous avons des capitaines pour chaque sport qui organisent les entraînements et les événements, donc je ne peux pas vraiment prendre tout le crédit."
            mi "De plus, ce club est comme. Ma vraie famille. Nous nous soutenons les uns les autres, sur et en dehors du terrain. Alors je dois tout donner pour nous garder organisés."
            n "On dirait que Misute a vraiment une belle chose qui se passe dans ce club, peut-être que je devrais envisager de rejoindre. Ça pourrait être très amusant."
            mi "Alors, mes talents de persuasion sont-ils toujours au top ? Ou ai-je besoin de te donner une motivation supplémentaire pour nous rejoindre ?"
            n "Misute me sourit malicieusement."

            menu:
                "Je suis convaincu":
                    play audio "select.mp3"
                    mc "C'est tout ce que j'avais besoin d'entendre, compte sur moi à partir de maintenant !"
                    mi "C'est l'esprit !"
                    n "Misute me donne un gros câlin qui dure un temps très gênant. Je dois physiquement la repousser pour qu'elle arrête. Cependant, elle finit par me lâcher. Je sais maintenant ce que c'est que de lutter contre quelqu'un avec la force d'un ours, génial."
                "Je ne suis pas convaincu":
                    play audio "select.mp3"
                    mc "J'aimerais faire un tour avec tout le monde d'abord avant de m'engager dans un club."
                    n "Misute regarde le sol tristement, puis me regarde de nouveau, enroulant son bras autour de mon cou."
                    mi "Je dois admettre, ce n'était pas la réponse que j'espérais."
                    mi "MAIS."
                    mi "Tu finiras par changer d'avis, je le sais."
                    n "Misute me lâche alors de l'étranglement accidentel qu'elle m'avait infligé."

            mi "Bon, de toute façon, je ne devrais probablement pas retarder le match de volley plus longtemps que je ne l'ai déjà fait. Tu devrais venir regarder ! Ça te donnera une bonne idée de comment fonctionne notre club."
            mc "Bien sûr, je suppose que regarder le match pourrait être amusant. Montre-moi le chemin."
            mi "Génial ! J'ai la meilleure place de la maison, rien que pour toi, tousse aussi connue sous le nom de sol tousse, alors assure-toi de nous encourager, d'accord ?"
            n "Nous nous levons tous les deux des gradins et nous nous dirigeons vers le terrain de volley où je trouve le coin de sol le plus confortable possible."
            n "J'aperçois Misute sur le terrain, sa queue de cheval se balançant tandis qu'elle s'étire et discute avec ses coéquipiers."
            co "D'accord l'équipe, donnons tout ce que nous avons. Misute, tu commences avec le premier service."
            n "Misute s'avance, son expression passant de l'excitation joyeuse à une concentration absolue."
            n "Elle lance la balle haut et la frappe avec une précision parfaite."
            n "Le service est puissant, envoyant la balle au-dessus du filet."
            n "L'équipe adverse se démène, mais elle ne parvient pas à la renvoyer."
            n "Le premier point est attribué à l'équipe de Misute."
            n "Le match continue avec des échanges rapides et un travail d'équipe impressionnant."
            n "Misute et son équipe semblent se téléporter partout, plongeant pour sauver des balles difficiles, mettant en place des passes parfaites et délivrant des smashes puissants."
            n "Il est clair que leur travail d'équipe est très bien rodé."
            n "Le match atteint son apogée. C'est un point de match, et les deux équipes donnent tout ce qu'elles ont. L'équipe de Misute prépare leur dernière action."
            n "Misute place la balle… Et avec un SMASH puissant, Mei frappe la balle, et elle atterrit carrément dans le camp adverse."
            n "C'etait un coup puissant, je suis chanceux que celui-là n'ait pas été dirigé vers ma tête."
            n "Après la célébration, Misute court vers moi, encore en train de reprendre son souffle mais rayonnant de joie."
            mi "Alors, qu'en as-tu pensé ? Plutôt incroyable, non ?"

            menu:
                "Ouais c'était super":
                    play audio "select.mp3"
                    mc "Absolument. Je comprends pourquoi tu es si passionnée par ça. Ton énergie et vôtre synergie étaient incroyables."
                    mi "Contente que tu aies apprécié. Peut-être que la prochaine fois, tu seras avec nous sur le terrain, non ? Je pense que tu passerais un super moment."
                    mc "Seulement si la prochaine fois inclut quelques conseils personnalisés de la reine du volley elle-même."
                "Pff, je pourrais faire mieux":
                    play audio "select.mp3"
                    mc "Pff, c'était correct, je pourrais faire mieux."
                    mi "Mieux vaut que tu mettes ton argent là où ta bouche est alors, la prochaine fois, nous mettons les enjeux !"
                    n "Misute me donne le sourire le plus confiant, je ne sais pas si défier elle était la meilleure idée, mais maintenant nous sommes engagés. Elle regarde ensuite le sol, fatiguée."
                    mi "La prochaine fois, je te montrerai quelque chose de vraiment incroyable…"
                    n "Misute marche ensuite vers les bancs pour se reposer."

            n "Misute me fait alors signe de venir aux bancs pour me rafraîchir après le match intense."
            mi "Hé [mc], merci d'être venu regarder. Ça compte beaucoup pour moi."
            mc "N'importe quand. C'était un plaisir."
            mi "Puis-je prendre ça comme une façon détournée de dire que nous le referons un de ces jours ?"
            mc "Absolument."
            n "Misute me sourit alors que nous nous allongeons sur les bancs, épuisés."

        "Reposons-nous un peu":
            play audio "select.mp3"
            mc "Je suis encore un peu sous le choc, reposons-nous un peu."
            mi "Ça me va, j'aurais bien besoin d'une petite pause après ce match."
            n "Misute se lève et me conduit à son coin de détente, un joli petit coin à l'ombre près des gradins. Elle s'allonge alors et ferme les yeux, elle a l'air très confortable malgré le fait qu'elle soit allongée sur le sol. J'essaie de faire de mon mieux pour être aussi confortable qu'elle en m'allongeant, moi aussi, sur le sol à côté d'elle. Mon dos va me détester plus tard."
            mi "Mince... Je vis vraiment ma meilleure vie."
            mi "Rien ne vaut le combo sol froid et discussion avec quelqu'un."
            mc "Je peux penser à beaucoup de choses qui valent mieux que le sol froid, mais je ne vais pas ruiner son moment, alors je me tais."
            mi "Tout ce qu'il me faudrait, c'est de la bonne musique et je serais au paradis."
            n "C'est peut-être mon moyen d'apprendre plus sur ses autres hobbies ! "
            menu:
                    "En parlant de ça, quel genre de musique aimes-tu ?":
                        play audio "select.mp3"
                        mc "En parlant de ça, quel est ton genre de musique préféré ? Peut-être que je pourrais en mettre."
                        n "Misute hésite, puis commence à balancer la tête de gauche à droite en parlant."
                        mi "Pas pour la détente, mais un bon vieux rock avant de faire quoi que ce soit, et ma motivation augmente dix fois." 
                        mi "Eye of the Tiger, peut-être du Linkin Park, et c'est parti, je recommande fortement."
                        mi "Ou bien, je dis rock mais tout ce qui est motivant fait des merveilles pour l'âme."
                        mi "Mais quoi qu'il en soit, on ne peut pas se tromper avec les classiques."
                    "À part la musique, que fais-tu pour te détendre ?":
                        play audio "select.mp3"
                        mc "À part la musique, qu'aimes-tu faire pour te détendre ?"
                        mi "Hm, rien ne me fait plus de bien qu'un bon repas."
                        mi "Si tu cherches des recommandations, le curry du restaurant au bout de la rue, ça ne peut pas être mieux."
                        mi "Et bien sûr, toujours le prendre extra épicé, fais-moi confiance là-dessus."
            n "Misute penche la tête sur le côté, écrasant son visage."
            mi "Mec, j'aimerais qu'on ait l'option de rester ici toute la journée. J'adore le sport, mais ce que je donnerais pour ne pas avoir à essayer parfois."
            n "Misute penche la tête encore, regardant le ciel avec une expression pensive."
            mi "Bon… fini de paresser, faisons quelque chose !"
            mc "Oh, bien sûr, à quoi penses-tu ?"
            n "Misute saute soudainement."
            mi "Suis-moi, je sais exactement ce qu'on va faire."
            n "Elle me prend par la main et me tire vers un hangar près du terrain de sport."
            n "Elle l'ouvre pour révéler une grande collection de matériel sportif, d'où elle sort un jeu de fers à cheval."
            mi "Tu as déjà joué aux fers à cheval ? On peut faire une petite partie avant d'aller en cours."
            menu:
                "Je suis un pro du fer à cheval, regarde ça.":
                    play audio "select.mp3"
                    mc "On m'appelait « le cow-boy » au lycée pour une raison, je suis un pro."
                    n "Je prends le fer à cheval de sa main et le serre avec une confiance absolue après cette réplique magnifique."
                    mc "Regarde ça, facile comme bonjour."
                    n "Elle me sourit malicieusement, place les deux piquets dans le sol et me regarde préparer un lancer."
                    n "Je lance ensuite le fer à cheval avec une technique parfaite, avec l'élan d'un athlète olympique!"
                    n "...Et il rate complètement."
                    n "Misute retient un grand éclat de rire et reprend son visage de compétitrice."
                    mi "C'est un bon lancer, [mc]."
                    n "Elle se concentre ensuite intensément, faisant le même mouvement que moi, mais avec toute la force physique d'une véritable athlète."
                    n "...Et rate complètement aussi."
                    n "Alors que nous regardons tous les deux, stupéfaits, les piquets encore debout"
                    n "Nous nous regardons et convenons d'un commun accord que la première manche n'a jamais eu lieu, maintenant le VRAI jeu commence."
                "Je n'ai aucune idée de ce qu'il faut faire.":
                    play audio "select.mp3"
                    mc "Je n'ai aucune idée de ce qu'il faut faire. Je n'ai jamais joué aux fers à cheval avant."
                    n "Misute rit, un éclat espiègle dans les yeux."
                    mi "Ne t'inquiète pas, [mc]. C'est assez simple. Laisse-moi te montrer comment on fait. "
                    n "Elle prend un fer à cheval et se dirige vers le piquet, démontrant un lancer fluide et confiant."
                    n "Le fer à cheval vole dans les airs, mais manque complètement la cible."
                    n "Elle rit, secouant la tête."
                    mi "Ok, peut-être pas comme ça… Mais tu as compris l'idée, non ?"
                    n "Misute me tend ensuite un fer à cheval, guidant ma prise et ma posture."
                    mi "Balance juste ton bras comme ça, et relâche-le d'un coup de poignet. Facile."
                    n "Je tente le coup, imitant ses mouvements, et le fer à cheval atterrit effectivement."
                    mi "Wow ! Bien joué, refaisons une vraie partie maintenant, montre-moi ton potentiel ! "
                    n "Nous prenons tous les deux nos positions, prêts pour que le vrai jeu commence."
            n "Misute et moi prenons nos positions près des piquets, et elle me sourit malicieusement."
            mi "D'accord, [mc], c'est du sérieux maintenant ! Prêt à montrer ce que tu sais faire ?"
            mc  "Ouais, allons-y !"
            n "Je prends une grande inspiration, aligne mon premier lancer et relâche le fer à cheval."
            n "Il atterrit un peu à côté de la cible. Mais Misute applaudit avec un sourire encourageant."
            mi "Bien essayé ! On dirait que tu as du potentiel en toi après tout."
            mc "Je suppose que j'ai appris quelques trucs. "
            n "Elle se prépare ensuite pour son tour, faisant un lancer précis qui atterrit proprement sur le piquet."
            mi "Voilà le coup de magie dont j'avais besoin, je suis concentrée, à toi encore, mon pote."
            n "Elle fait tourner un fer à cheval autour de son doigt, manquant presque de se frapper au visage."
            n "Je prends un autre fer à cheval et me prépare à lancer. Je fais une pause pour me concentrer, ce que Misute remarque."
            mi"Je vois que tu prends ton temps, tu as besoin d'un discours de motivation ?"
            n "Je ris en me concentrant sur mon lancer. "
            mi "Ça va… Mais un discours de motivation pourrait aider."
            mi "D'accord, tu vas y arriver ! Tu es génial, tu vas faire de cette partie de fers à cheval la meilleure de toutes ! Tu peux le faire !"
            n "Il semble que sa compétence en sport se traduit également par des compétences de cheerleading incroyables."
            n "Avec une détermination dans le cœur, je lance avec une telle grâce que je réussis un coup parfait !"
            mi "Qui aurait cru que mes compétences ne se limitaient pas aux sports, je suis vraiment la meilleure."
            n "Elle rit pour elle-même, alors que le jeu progresse jusqu'à la dernière manche."
            n "Misute sourit et se prépare pour le dernier lancer."
            mi "D'accord, dernière manche ! Voyons si tu peux me surpasser."
            n "Je me prépare pour mon dernier lancer, me sentant détendu."
            n "Le fer à cheval vole dans les airs et atterrit près du piquet."
            n "Le dernier lancer de Misute est fluide mais se termine juste à côté de l'anneau."
            n "Elle s'effondre sur l'herbe à côté de moi avec un sourire."
            mi "Eh bien, eh bien, on dirait que tu m'as battue ! Bien joué."
            n "Je la rejoins sur l'herbe."
            mc "Je suppose que j'ai quelques tours dans mon sac."
            n "Misute me donne un coup de coude en riant."
            mi "Tu en as certainement !"
            mi "Et hé, si tu veux affiner ces compétences, tu es le bienvenu au club de sport à tout moment, [mc]."
            mi "Nous serions heureux de t'avoir parmi nous."
            mc "Merci, Misute. C'était vraiment amusant. J'ai hâte de faire d'autres parties."
            n "Misute s'étire, semblant contente."
            mi "Moi aussi ! Mais la c'est la meilleure partie — juste se détendre et passer un bon moment après une bonne partie."
            n "Je hoche la tête en m'allongeant sur l'herbe." 
            mc "Définitivement. Je m'y habitue déjà."

    n "Alors que Misute et moi sommes allongés, profitant du soleil radieux du matin, un miaulement lointain de chat attire notre attention."
    n "Nous nous redressons tous les deux, cherchant la source du son."
    mi "Hé, t'as entendu ça ?"
    n "Je regarde autour de moi, apercevant un petit chat noir aux yeux jaunes curieux, qui sort à moitié de derrière un buisson voisin."
    mc "Oh, regarde là-bas."
    n "Les yeux de Misute s'illuminent, toute la fatigue précédente disparaissant de son corps, son énergie est contagieuse."
    mi "Allons voir si nous pouvons l'attirer. Peut-être qu'il veut se joindre à notre séance de détente !"
    n "Nous nous levons tous les deux et nous approchons lentement du chat."
    n "Il nous observe prudemment mais ne recule pas. Misute s'accroupit, tendant la main."
    mi "Viens ici minou, minou, minou. Allez, on ne te fera pas de mal."
    n "Misute arbore le plus large sourire que j'ai vu aujourd'hui."
    n "Le chat avance prudemment, reniflant l'air."
    n "Il semble s'habituer à nous, et bientôt il frotte sa tête contre la main tendue de Misute."
    n "Misute rit doucement, visiblement heureuse."
    mc "On dirait qu'il t'aime bien."
    n "Je détourne le regard une seconde, et en me retournant, je vois déjà Misute en train de lui caresser le ventre et de jouer avec lui."
    mi "Je suppose qu'il reconnaît une âme gentille quand il en voit une."
    n "Elle me sourit fièrement."
    n "Je tends la main et caresse également le chat. Il ronronne bruyamment, manifestement content de l'attention."
    n "Juste à ce moment, le son fort et résonnant d'une cloche d'école retentit à travers le terrain, signalant le début des cours."
    mi "Oh, il est temps. Nous devrions vraiment aller en cours."
    mc "Oui, il vaut mieux ne pas être en retard le premier jour..."
    n "Je me lève à contrecœur, donnant au chat une dernière caresse derrière les oreilles."
    n "Misute reste penchée au-dessus du chat tandis que je m'éloigne un peu."
    menu:
        "Parlons après les cours":
            play audio "select.mp3"
            mc "Eh bien, on se voit après les cours, hein ?"
            mi "Ça marche, à plus tard ! Bonne chance"
        "Je dois y aller d’urgence":
            play audio "select.mp3"
            mc "J'ai passé un bon moment, mais je dois y aller maintenant, à plus."
            mi "Pas de soucis, je devrais probablement commencer à y aller aussi."
            n "Elle me fait un signe de la main."
    n "Je m'éloigne un peu en entendant, hors de portée, Misute parler avec le chat."
    mi "Hé, toi."
    n "Murmure-t-elle, sa voix portant une pointe de lassitude."
    n "Misute soupire, se penchant légèrement sur le chat."
    n "Le chat cligne lentement des yeux, son regard fixe presque réconfortant."
    mi "Je me donne tellement de mal, et pourtant ce n'est jamais assez..."
    n "Le chat se frotte contre sa main, ronronnant un baume apaisant pour ses pensées troublées."
    n "Misute sourit légèrement."
    mi "Pourquoi est-ce que je dis ça à toi… Tu ne sais même pas ce que je dis, tu apprécies juste tes caresses…"
    mi "Mec… On dit que tu portes malheur, mais pour moi tu es un petit morceau de bonne fortune. Tu le sais, mon pote ?"
    mi "Tu te fiches de mes notes ou de mes trophées. Tu restes juste ici et te détends avec moi."
    mi "Peut-être que tu es pareil, tellement de gentillesse dans un si petit corps, et pourtant ce mythe persiste."
    mi "Hmm… On se ressemble plus que je ne le pensais après tout."
    n "Elle reste assise là quelques instants de plus, la compagnie silencieuse du chat lui apportant une petite mesure de paix. "
    n "Elle se lève ensuite, donnant une dernière caresse au chat."
    mi "À plus, mon pote."
    n "Dit-elle doucement, avant de courir vers le bâtiment de l'école, sa persona habituelle et énergique revenant en place."
    n "Elle m'aperçoit, et son visage pâlit alors qu'elle prétend ne pas m'avoir vu la regarder tout le temps. "
    n "Elle se met alors à sprinter pour ne pas arriver en retard en cours… "
    n "Et je réalise que c'est mon signal pour faire de même…"
    n "3 minutes de retard le premier jour, un début fantastique de mon année scolaire..."
    return



label ch0_yamano:

    return



label ch0_yuzu:

    return