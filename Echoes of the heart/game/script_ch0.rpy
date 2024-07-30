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
    mc "Elle a raison, étant donné que tout le monde à l'école se connaît déjà, il faut que je sois en pleine forme si je veux faire bonne impression"
    n "Je mets rapidement mon uniforme tout neuf et je sors dans le salon"
    n "L'odeur de délicieux pain perdu emplit l'air."
    n "Mais je ne m'y attarde pas trop longtemps, car je suis déjà sur le point d'être en retard, maman avait raison de dire que je suis un gros dormeur"
    n "Avec le ventre plein et beaucoup de motivation, je me précipite hors de la maison à toute vitesse"
    show school with in_eye
    n "Nous y voilà... Ce n'est pas si intimidant quand on s'approche. Jusqu'à ce que la réalisation que c'est un moment décisif pour ma vie sociale frappe ; et tout à coup, c'est extrêmement intimidant"
    n "Mais plus j'y pense, plus je vais stresser, alors il est temps de se mettre en route et d'essayer de parler aux gens. Voyons ce qui semble intéressant."

    menu line:
        "Bibliothèque":
            jump ch0_hotaru
        "BDE":
            jump ch0_yuzu
        "Terrain de sport":
            jump ch0_misuto
            mc "Le terrain de sport semble être un bon endroit pour la camaraderie, peut-être que je m'intégrerai plus facilement dans un groupe"
        "Club de théatre":
            jump ch0_yamano
        "Allez en classe":
            jump ch0_izu           

    return


label ch0_hotaru:

    return



label ch0_izu:

    return



label ch0_misuto:
    show sport with dissolve
    n "J'observais à travers une porte double entrouverte, et je remarque qu'un match de volley était en plein déroulement. Je décide alors d’entrer et c’est là qu’un ballon vient voltiger vers ma direction"
    mi "Eh Mei ! Fais attention où tu tires la prochaine fois !"
    n "Une jeune fille vient de rattraper d’une vitesse le ballon qui arrivait à une vitesse fatale. Vêtue d’une veste sur l’uniforme scolaire, elle arborait une belle queue de cheval et un sourire radieux"
    show misute:
        zoom 0.34 
        xalign 0.5
    mi "Ouf, désolée pour ça"
    mi "Mei ne sait pas contrôler sa propre force, ça va ?"
    n "C’était un peu surprenant mais je ne suis pas à l'hôpital donc on peut considérer ça comme une victoire."
    menu:
        "Juste une petite frayeur":
            mc "Ça va, c'était juste une petite frayeur"
            mc "je vais m'en remettre"
            mi "D'accord, super à entendre ! Je suis sûre que tu seras de nouveau sur pied en un rien de temps"
            n "Misute me fait asseoir sur les gradins un moment"
        "J'ai besoin d'un moment pour respirer":
            mc "C'était terrifiant..."
            mc " Je pense que j'ai besoin d'un moment..."
            mc " pour respirer"
            mi "Je suis vraiment"
            mi "vraiment"
            mi "vraiment"
            mi "vraiment"
            mi "VRAIMENT"
            mi "désolée"
            mi "tu as besoin d'aller à l'infirmerie ?"
            mi "Je peux t'y emmener"
            n "Misute s'approche pour me soutenir sur son épaule"
            mc "J'ai juste besoin d'un moment, vraiment, tout va bien"
            n "Misute se redresse et me fait asseoir sur les gradins pour me reposer"
    mi "Oh, au fait, je ne t'ai jamais vu au club de sport avant, puis-je connaître ton nom ?"
    mc "Ah bien sûr, je m'appelle [mc]! Mais tu peux m'appeler..."
    n "J'essaie de penser à un surnom cool... Mais rien ne me vient à l'esprit"
    mc "En fait, restons sur [mc]"
    mi "Okidoki [mc]! Donne-moi une seconde"
    n "Misute retourne sur le terrain de volley et appelle une pause, puis elle revient vers moi pour discuter"
    mi "Alors ! Tu ne m'as pas dit pourquoi tu es ici, pourrais-je peut-être t'intéresser à des activités du club de sport ?"
    mi "Nous avons organisé une course pour aujourd'hui, si tu veux nous rejoindre, c'est le moment parfait !"
    
    menu:
        "Je suis toujours partant pour une course":
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
                    mc "C'est amusant ! Je ne me rendais pas compte à quel point ça m'avait manqué ce genre de chose."
                    mi "N'est-ce pas ? Rien de plus motivant que de se donner à fond avant une course vraiment importante."
                    mi "Il faut juste continuer à tout donner, de cette façon tu obtiens la plus grande récompense !"
                "Tout brûle...":
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

            return

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
                    mc "C'est tout ce que j'avais besoin d'entendre, compte sur moi à partir de maintenant !"
                    mi "C'est l'esprit !"
                    n "Misute me donne un gros câlin qui dure un temps très gênant. Je dois physiquement la repousser pour qu'elle arrête. Cependant, elle finit par me lâcher. Je sais maintenant ce que c'est que de lutter contre quelqu'un avec la force d'un ours, génial."
                "Je ne suis pas convaincu":
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
                    mc "Absolument. Je comprends pourquoi tu es si passionnée par ça. Ton énergie et vôtre synergie étaient incroyables."
                    mi "Contente que tu aies apprécié. Peut-être que la prochaine fois, tu seras avec nous sur le terrain, non ? Je pense que tu passerais un super moment."
                    mc "Seulement si la prochaine fois inclut quelques conseils personnalisés de la reine du volley elle-même."
                "Pff, je pourrais faire mieux":
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

            menu:
                "Reposons-nous un peu":
                    mc "Je suis encore un peu sous le choc, reposons-nous un peu."
                    mi "Ça me va, j'aurais bien besoin d'une petite pause après ce match."
                    n "Misute se lève et me conduit à son coin de détente, un joli petit coin à l'ombre près des gradins. Elle s'allonge alors et ferme les yeux, elle a l'air très confortable malgré le fait qu'elle soit allongée sur le sol. J'essaie de faire de mon mieux pour être aussi confortable qu'elle en m'allongeant, moi aussi, sur le sol à côté d'elle. Mon dos va me détester plus tard."
                    mi "Mince... Je vis vraiment ma meilleure vie."
                    mi "Rien ne vaut le combo sol froid et discussion avec quelqu'un."
                    mc "Je peux penser à beaucoup de choses qui valent mieux que le sol froid, mais je ne vais pas ruiner son moment, alors je me tais."
                    mi "Tout ce qu'il me faudrait, c'est de la bonne musique et je serais au paradis."
                    mc "En parlant de ça, quel genre de musique aimes-tu ?"
                    mi "Oh, j'écoute un peu de tout, mais j'ai un faible pour les chansons pop dynamiques, surtout celles qui me donnent envie de danser ! Et toi ?"
                    mc "Je dirais que j'aime les ballades relaxantes, quelque chose qui me calme après une longue journée."
                    mi "C'est un bon choix. On pourrait peut-être partager nos playlists un jour, qui sait ?"
                    mc "Pourquoi pas !"

            return
    n "Alors que Misute et moi sommes allongés sur l'herbe, profitant du soleil radieux du matin, un miaulement lointain de chat attire notre attention."
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
            mc "Eh bien, on se voit après les cours, hein ?"
            mi "Ça marche, à plus tard ! Bonne chance"
        "Je dois y aller d’urgence":
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