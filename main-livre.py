import flet as ft

def main(page: ft.Page):
    page.title = "Bibliotheque Plus"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.window_width = 1100
    page.window_height = 700

    # 1. barre de navigation laterale
    sidebar = ft.NavigationRail(
        selected_index = 0,
        label_type = ft.NavigationRailLabelType.ALL,
        min_width= 100,
        min_extended_width= 200,
        group_alignment = -0.9,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Accueil"),
            ft.NavigationRailDestination(icon=ft.Icons.LIBRARY_BOOKS, label="Mes bookins"),
            ft.NavigationRailDestination(icon=ft.Icons.PERSON, label="Profil"),
            ft.NavigationRailDestination(icon=ft.Icons.SETTINGS, label="Parametres"),
        ],
        on_change=lambda e: switch_view(e.control.selected_index),
    )
    #2. cration d'une carte de livre 
    def create_book_card(title, author, img_id):
        return ft.Container(
            # col={"sm": 6, "md": 4, "lg": 2} signifie : 
            # 2 colonnes sur grand écran (donc 6 livres par ligne car 12/2=6)
            col={"sm": 6, "md": 4, "lg": 2},
            content=ft.Column([
                ft.Container(
                    width=150,
                    height=220,
                    bgcolor=ft.Colors.GREY_900,
                    border_radius=8,
                    image=ft.DecorationImage(
                        src=f"covers/{img_id}.jpg",
                        fit=ft.ImageFit.COVER,
                    ),
                ),
                ft.Text(title, size=14, weight="bold", overflow=ft.TextOverflow.ELLIPSIS),
                ft.Text(author, size=12, color=ft.Colors.GREY_400),
            ]),
            margin=ft.margin.only(right=15),
            on_click=lambda _: print(f"livre clique: {title}")
        )
    #3. section de categorie
    trending_row = ft.Row(
        scroll=ft.ScrollMode.ADAPTIVE,
        controls=[
            create_book_card("L'Etranger", "Albert Camus",1),
            create_book_card("1984", "George Orwell",2),
            create_book_card("Le Petit Prince", "St-Exupery",3),
            create_book_card("Dune", "Frank Herbert",4),
            create_book_card("Fondation", "Isaac Asimov",5),
            create_book_card("Fahrenheit 451", "Ray Bradbury",6),    
        ]
    )
    #4. mise en page de la page principale
    main_content = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        spacing=0,
        controls=[
            ft.Text("Contenu principal ", size=24, weight="bols"),
            ft.Divider(height=30, color="transparent"),
            ft.Text("Tendances Actuelles", size=24, weight="bold"),
            ft.Divider(height=10, color="transparent"),
            trending_row,
            ft.Divider(height=30, color="transparent"),
            ft.Text("Nouveautes", size=24, weight="bold"),
            ft.Divider(height=10, color="transparent"),

        ],
    )
    # section mes bookins
    trending_row_bookins = ft.Row(
        scroll=ft.ScrollMode.ADAPTIVE,
        vertical_alignment=ft.CrossAxisAlignment.START, # Aligne le haut du livre et le haut du texte
        controls=[
            # 1. Le livre à gauche(Image + Titre en dessous via la fonction de depart create_book_card)
            create_book_card("L'Etranger", "Albert Camus", 1),
            
            # 2. Le Résumé à droite
            ft.Container(
                width=600, # LARGEUR FIXE : C'est ce qui crée l'effet "bloc" de paragraphe
                padding=ft.padding.only(left=30, top=10), # Espace entre le livre et le texte
                content=ft.Column([
                    ft.Text(
                        "RÉSUMÉ", 
                        size=18, 
                        weight="bold", 
                        color=ft.Colors.BLUE_400
                    ),
                    ft.Text(
                        "Dans l'Algérie coloniale, Meursault reçoit un télégramme annonçant la mort de sa mère. "
                        "Il assiste à l'enterrement sans manifester la douleur attendue par la société. "
                        "Quelques jours plus tard, sur une plage écrasée de soleil, il tue un Arabe sans raison apparente. "
                        "Le roman suit son procès, où il est jugé moins pour son crime que pour son indifférence et son refus de mentir. "
                        "Une œuvre majeure sur l'absurdité de la condition humaine.",
                        size=16,
                        text_align=ft.TextAlign.JUSTIFY, # Texte bien aligné à gauche et à droite
                        color=ft.Colors.BLUE_700,
                        # no_wrap=False est la valeur par défaut, donc le texte reviendra à la ligne
                    ),
                    ft.Divider(height=10, color="transparent"),
                    #bouton pour continuer la lecture
                    ft.ElevatedButton("Continuer la lecture", 
                        icon=ft.Icons.PLAY_ARROW_ROUNDED, 
                        icon_color=ft.Colors.WHITE, 
                        bgcolor=ft.Colors.BLUE_700, 
                        color=ft.Colors.WHITE, 
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),),
                        on_click=lambda e: print("Continuer la lecture clicked")
                    ),
                ], spacing=10)
            )
        ]
    )
    trending_row_bookins.margin = ft.margin.only(top=10, bottom=10)
    encours_bookins = ft.Row(
        scroll=ft.ScrollMode.ADAPTIVE,
        controls=[
            ft.Container(
                content=ft.Column([
                    create_book_card("Dune", "Frank Herbert",4),
                    ft.ProgressBar(value=0.45, width=150),
                    ft.Text("45% lu", size=12, color=ft.Colors.GREY_400),
                    #bouton pour continuer la lecture
                    ft.ElevatedButton("Lire", 
                        icon=ft.Icons.PLAY_ARROW_ROUNDED, 
                        icon_color=ft.Colors.WHITE, 
                        bgcolor=ft.Colors.BLUE_700, 
                        color=ft.Colors.WHITE, 
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),),
                        on_click=lambda e: print("Lire")
                    ),
                ], spacing=5),
            ),
            ft.Container(
                content=ft.Column([
                    create_book_card("Fondation", "Isaac Asimov",5),
                    ft.ProgressBar(value=0.40, width=150),
                    ft.Text("40% lu", size=12, color=ft.Colors.GREY_400),
                    #bouton pour continuer la lecture
                    ft.ElevatedButton("Lire", 
                        icon=ft.Icons.PLAY_ARROW_ROUNDED, 
                        icon_color=ft.Colors.WHITE, 
                        bgcolor=ft.Colors.BLUE_700, 
                        color=ft.Colors.WHITE, 
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),),
                        on_click=lambda e: print("Lire")
                    ),
                ], spacing=5),
            ),
            ft.Container(
                content=ft.Column([
                    create_book_card("1984", "George Orwell",2),
                    ft.ProgressBar(value=0.75, width=150),
                    ft.Text("75% lu", size=12, color=ft.Colors.GREY_400),
                    #bouton pour continuer la lecture
                    ft.ElevatedButton("Lire", 
                        icon=ft.Icons.PLAY_ARROW_ROUNDED, 
                        icon_color=ft.Colors.WHITE, 
                        bgcolor=ft.Colors.BLUE_700, 
                        color=ft.Colors.WHITE, 
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),),
                        on_click=lambda e: print("Lire")
                    ),
                ], spacing=5),
            ),
            ft.Container(
                content=ft.Column([
                    create_book_card("Le Petit Prince", "St-Exupery",3),
                    ft.ProgressBar(value=0.15, width=150),
                    ft.Text("15% lu", size=12, color=ft.Colors.GREY_400),
                    #bouton pour continuer la lecture
                    ft.ElevatedButton("Lire", 
                        icon=ft.Icons.PLAY_ARROW_ROUNDED, 
                        icon_color=ft.Colors.WHITE, 
                        bgcolor=ft.Colors.BLUE_700, 
                        color=ft.Colors.WHITE, 
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),),
                        on_click=lambda e: print("Lire")
                    ),
                ], spacing=5),
            ),
            ft.Container(
                content=ft.Column([
                    create_book_card("Fahrenheit 451", "Ray Bradbury",6),
                    ft.ProgressBar(value=0.09, width=150),
                    ft.Text("9% lu", size=12, color=ft.Colors.GREY_400),
                    #bouton pour continuer la lecture
                    ft.ElevatedButton("Lire", 
                        icon=ft.Icons.PLAY_ARROW_ROUNDED, 
                        icon_color=ft.Colors.WHITE, 
                        bgcolor=ft.Colors.BLUE_700, 
                        color=ft.Colors.WHITE, 
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),),
                        on_click=lambda e: print("Lire")
                    ),
                ], spacing=5),
            ),
            ft.Container(
                content=ft.Column([
                    create_book_card("L'Etranger", "Albert Camus",1),
                    ft.ProgressBar(value=0.47, width=150),
                    ft.Text("47% lu", size=12, color=ft.Colors.GREY_400),
                    #bouton pour continuer la lecture
                    ft.ElevatedButton("Lire", 
                        icon=ft.Icons.PLAY_ARROW_ROUNDED, 
                        icon_color=ft.Colors.WHITE, 
                        bgcolor=ft.Colors.BLUE_700, 
                        color=ft.Colors.WHITE, 
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8),),
                        on_click=lambda e: print("Lire")
                    ),
                ], spacing=5),
            ),
        ]
    )
    main_bookins = ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        spacing=0,
        controls=[
            ft.Text("Ma bibliotheque", size=24, weight="bold"),
            ft.Divider(height=30, color="transparent"),
            ft.Text("voici tous les livres auquels vous avez appercu ou lus lensembles des livres", size=20, weight="bold"),
            ft.Divider(height=10, color="transparent"),
            ft.TextField(label="Search", hint_text="Search..."),
            ft.Divider(height=10, color="transparent"),
            trending_row_bookins,
            ft.Divider(height=20, color="transparent"),
            ft.Text("En cours de lecture", size=24, weight="bold"),
            ft.Divider(height=20, color="transparent"),
            encours_bookins

        ]
    )# fin section mes bookins
    
    # zone de contenu principale qui changera selon la selection dans la barre laterale
    content_area = ft.Container(content=main_content, expand=True, padding=20)
    def switch_view(index):
        if index == 0:
            content_area.content = main_content
        elif index == 1:
            content_area.content = main_bookins
        elif index == 2:
            content_area.content = ft.Column([
                ft.Text("Mon Profil", size=30, weight="bold"),
                ft.CircleAvatar(content=ft.Icon(ft.Icons.PERSON), radius=50),
                ft.Text("Utilisateur : Ddjunet", size=20)
            ])
        elif index == 3:
            content_area.content = ft.Text("Paramètres de l'application", size=30)
        
        page.update() # On rafraîchit la page pour afficher le changement
    #5. l'espace des nouveautes de la bibliotheque
    main_content.controls.append(
        ft.Row(
            scroll=ft.ScrollMode.ADAPTIVE,
            controls=[
                create_book_card(f"Livre {i}", "Auteur", i+1) for i in range(6) # la boucle pour generer les livres d'une facon dynamique sans utiliser le for
            ]
        )
    )

    # assemblage des elements finaux
    page.add(
        ft.Row(
            [
                sidebar,
                ft.VerticalDivider(width=1),
                content_area, # MODIFICATION : On affiche content_area à la place de main_content
            ],
            expand=True,
        )
    )
# Run a Flet App
ft.app(target=main, assets_dir="images")