"""
THE CASE FILES - Dark Psychological Thriller Investigation Game
100% Python Standard Library (Tkinter, json, os).
Run directly with: python main.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import cases
import save_manager

# --- PALETTE DIRECTION ---
BG_DEEP       = "#040203"
BG_PANEL      = "#0E0508"
BG_CARD       = "#16070B"
BG_ACCENT     = "#240A10"
BORDER_RED    = "#4A0C16"
RED_CRIMSON   = "#8E1726"
RED_BRIGHT    = "#B52638"
TEXT_IVORY    = "#F4E9DE"
TEXT_MUTED    = "#9C8A84"
TEXT_DIM      = "#6B5B57"
ACCENT_GOLD   = "#D4AF37"

# --- SYSTEM FONTS ---
FONT_TITLE_HERO   = ("Georgia", 32, "bold")
FONT_TITLE_MED    = ("Georgia", 20, "bold")
FONT_TITLE_SUB    = ("Georgia", 14, "bold")
FONT_MONO_STAMP   = ("Consolas", 11, "bold")
FONT_MONO_SMALL   = ("Consolas", 9)
FONT_BODY         = ("Segoe UI", 11)
FONT_BODY_BOLD    = ("Segoe UI", 11, "bold")
FONT_BODY_LARGE   = ("Segoe UI", 13)
FONT_BUTTON       = ("Georgia", 11, "bold")


class TheCaseFilesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("THE CASE FILES — Crime Investigation Archive")
        self.geometry("1180x800")
        self.minsize(1050, 720)
        self.configure(bg=BG_DEEP)

        self.center_window(1180, 800)

        self.progress_data = save_manager.load_progress()
        self.current_case = None
        self.investigation_state = {}

        self.container = tk.Frame(self, bg=BG_DEEP)
        self.container.pack(fill="both", expand=True)

        self.show_loading_screen()

    def center_window(self, width, height):
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = max(0, (sw - width) // 2)
        y = max(0, (sh - height) // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def clear_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    # =========================================================================
    # 1. LOADING SCREEN
    # =========================================================================
    def show_loading_screen(self):
        self.clear_screen()
        canvas = tk.Canvas(self.container, bg=BG_DEEP, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        w, h = 1180, 800

        for y in range(0, 800, 4):
            canvas.create_line(0, y, 1200, y, fill="#070204", width=1)

        canvas.create_rectangle(40, 40, 1140, 760, outline=BORDER_RED, width=2)
        canvas.create_rectangle(46, 46, 1134, 754, outline="#1C060B", width=1)

        canvas.create_text(w//2, 170, text="FEDERAL BUREAU OF SPECIAL INVESTIGATIONS", font=FONT_MONO_STAMP, fill=RED_CRIMSON)
        canvas.create_text(w//2, 230, text="THE CASE FILES", font=("Georgia", 42, "bold"), fill=TEXT_IVORY)
        canvas.create_text(w//2, 290, text="EVERY CRIME LEAVES SOMETHING BEHIND.", font=("Georgia", 13, "italic"), fill=TEXT_MUTED)

        status_text = canvas.create_text(w//2, 450, text="INITIALIZING CRIME ARCHIVE...", font=FONT_MONO_STAMP, fill=TEXT_MUTED)

        canvas.create_rectangle(w//2 - 220, 490, w//2 + 220, 502, outline=BORDER_RED, fill="#0B0305")
        bar_fill = canvas.create_rectangle(w//2 - 218, 492, w//2 - 218, 500, outline="", fill=RED_BRIGHT)

        steps = [
            (20, "RETRIEVING ENCRYPTED DOSSIERS..."),
            (50, "INDEXING FORENSIC BALLISTICS & TIMELINES..."),
            (75, "RECONSTRUCTING COLD CASE EVIDENCE..."),
            (100, "ACCESS GRANTED.")
        ]

        def animate_step(idx=0):
            if idx < len(steps):
                pct, msg = steps[idx]
                canvas.itemconfig(status_text, text=msg)
                fill_width = (436 * pct) // 100
                canvas.coords(bar_fill, w//2 - 218, 492, (w//2 - 218) + fill_width, 500)
                self.after(180, lambda: animate_step(idx + 1))
            else:
                self.after(100, self.show_main_menu)

        self.after(100, animate_step)

    # =========================================================================
    # 2. MAIN MENU SCREEN
    # =========================================================================
    def show_main_menu(self):
        self.clear_screen()
        self.progress_data = save_manager.load_progress()

        root = tk.Frame(self.container, bg=BG_DEEP)
        root.pack(fill="both", expand=True)

        header = tk.Frame(root, bg=BG_PANEL, height=130, highlightthickness=1, highlightbackground=BORDER_RED)
        header.pack(fill="x", padx=30, pady=(25, 10))

        tk.Label(header, text="TOP SECRET // CLASSIFIED LAW ENFORCEMENT ACCESS ONLY", font=FONT_MONO_SMALL, fg=RED_CRIMSON, bg=BG_PANEL).pack(pady=(12, 2))
        tk.Label(header, text="THE CASE FILES", font=FONT_TITLE_HERO, fg=TEXT_IVORY, bg=BG_PANEL).pack()
        tk.Label(header, text="CRIME ARCHIVE • HOMICIDE DIVISION • INVESTIGATION SUITE", font=FONT_MONO_STAMP, fg=TEXT_MUTED, bg=BG_PANEL).pack(pady=(2, 10))

        body = tk.Frame(root, bg=BG_DEEP)
        body.pack(fill="both", expand=True, padx=30, pady=10)

        # Left Dossier Card
        dossier = tk.Frame(body, bg=BG_PANEL, width=420, highlightthickness=1, highlightbackground=BORDER_RED)
        dossier.pack(side="left", fill="y", padx=(0, 15), pady=10)
        dossier.pack_propagate(False)

        tk.Label(dossier, text="OPERATIVE DOSSIER", font=FONT_TITLE_SUB, fg=RED_BRIGHT, bg=BG_PANEL).pack(anchor="w", padx=25, pady=(20, 5))
        tk.Frame(dossier, bg=BORDER_RED, height=1).pack(fill="x", padx=25, pady=(0, 15))

        solved_count = len(self.progress_data["solved_cases"])
        total_cases = len(cases.get_all_cases())
        rank = save_manager.get_rank(solved_count)

        info_items = [
            ("DETECTIVE RANK", rank),
            ("SOLVED CASES", f"{solved_count} / {total_cases}"),
            ("CLEARANCE STATUS", "LEVEL 4 ACTIVE"),
            ("HOMICIDE SQUAD", "COLD CASE RETRIEVAL UNIT"),
            ("SOLVE ACCURACY", f"{100 - min(80, self.progress_data.get('wrong_attempts', 0) * 8)}%")
        ]

        for lbl, val in info_items:
            f = tk.Frame(dossier, bg=BG_PANEL)
            f.pack(fill="x", padx=25, pady=6)
            tk.Label(f, text=lbl, font=FONT_MONO_SMALL, fg=TEXT_DIM, bg=BG_PANEL).pack(anchor="w")
            tk.Label(f, text=val, font=("Georgia", 13, "bold"), fg=TEXT_IVORY if lbl != "DETECTIVE RANK" else ACCENT_GOLD, bg=BG_PANEL).pack(anchor="w")

        quote_frame = tk.Frame(dossier, bg="#070204", highlightthickness=1, highlightbackground="#24070D")
        quote_frame.pack(fill="x", side="bottom", padx=20, pady=25)
        quote_text = "\"Physical evidence cannot be intimidated. It does not forget. It cannot lie. Only human interpretation fails.\""
        tk.Label(quote_frame, text=quote_text, font=("Georgia", 10, "italic"), fg=TEXT_MUTED, bg="#070204", wraplength=340, justify="left").pack(padx=15, pady=15)

        # Right Menu
        menu_frame = tk.Frame(body, bg=BG_DEEP)
        menu_frame.pack(side="right", fill="both", expand=True, padx=(10, 0), pady=10)

        buttons = [
            ("ACCESS CASE ARCHIVE", "Inspect all active homicide dossiers and cold files.", self.show_archive, RED_CRIMSON),
            ("DETECTIVE RECORD", "Review cleared case convictions, career history and accuracy stats.", self.show_record, "#2D0A11"),
            ("INVESTIGATION PROTOCOL", "Guidelines on physical clues, interrogation contradictions, and deductions.", self.show_protocol, "#1A060A"),
            ("TERMINATE TERMINAL SESSION", "Safely save progress and exit the investigation system.", self.destroy, "#0D0305")
        ]

        for title, desc, cmd, color in buttons:
            btn_panel = tk.Frame(menu_frame, bg=BG_PANEL, highlightthickness=1, highlightbackground=BORDER_RED)
            btn_panel.pack(fill="x", pady=10, ipady=8)

            btn = tk.Button(
                btn_panel, text=f"▶  {title}", font=FONT_BUTTON,
                fg=TEXT_IVORY, bg=color, activebackground=RED_BRIGHT, activeforeground=TEXT_IVORY,
                relief="flat", cursor="hand2", anchor="w", padx=20,
                command=cmd
            )
            btn.pack(fill="x", padx=12, pady=(10, 3))
            tk.Label(btn_panel, text=desc, font=FONT_BODY, fg=TEXT_MUTED, bg=BG_PANEL, anchor="w").pack(fill="x", padx=32, pady=(0, 8))

    # =========================================================================
    # 3. CASE ARCHIVE SCREEN (Guaranteed Direct Treeview & Live Dossier)
    # =========================================================================
    def show_archive(self):
        self.clear_screen()
        self.progress_data = save_manager.load_progress()
        all_cases = cases.get_all_cases()

        root = tk.Frame(self.container, bg=BG_DEEP)
        root.pack(fill="both", expand=True)

        top_bar = tk.Frame(root, bg=BG_PANEL, height=70, highlightthickness=1, highlightbackground=BORDER_RED)
        top_bar.pack(fill="x", padx=25, pady=(20, 10))

        tk.Button(
            top_bar, text="← MAIN ARCHIVE MENU", font=FONT_BUTTON,
            fg=TEXT_IVORY, bg=BORDER_RED, activebackground=RED_BRIGHT,
            relief="flat", cursor="hand2", command=self.show_main_menu
        ).pack(side="left", padx=15, pady=12)

        tk.Label(top_bar, text="CENTRAL HOMICIDE DOSSIER ARCHIVE", font=FONT_TITLE_MED, fg=TEXT_IVORY, bg=BG_PANEL).pack(side="left", padx=20)

        solved_count = len(self.progress_data["solved_cases"])
        solved_txt = f"SOLVED: {solved_count} / {len(all_cases)}"
        tk.Label(top_bar, text=solved_txt, font=FONT_MONO_STAMP, fg=ACCENT_GOLD, bg=BG_PANEL).pack(side="right", padx=20)

        # Split Archive Layout: Left Case List (520px), Right Live Case Dossier (Remaining)
        archive_body = tk.Frame(root, bg=BG_DEEP)
        archive_body.pack(fill="both", expand=True, padx=25, pady=(0, 15))

        left_pane = tk.Frame(archive_body, bg=BG_PANEL, width=540, highlightthickness=1, highlightbackground=BORDER_RED)
        left_pane.pack(side="left", fill="both", padx=(0, 12))
        left_pane.pack_propagate(False)

        right_pane = tk.Frame(archive_body, bg=BG_CARD, highlightthickness=1, highlightbackground=BORDER_RED)
        right_pane.pack(side="right", fill="both", expand=True)

        # Left Table Header
        tk.Label(left_pane, text="CLASSIFIED FILE INDEX (SELECT CASE TO PREVIEW)", font=FONT_MONO_STAMP, fg=RED_BRIGHT, bg=BG_PANEL).pack(anchor="w", padx=15, pady=(15, 8))

        # Styled Treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Archive.Treeview",
            background="#0C0407",
            foreground=TEXT_IVORY,
            fieldbackground="#0C0407",
            rowheight=36,
            font=("Segoe UI", 10)
        )
        style.configure(
            "Archive.Treeview.Heading",
            background="#20060C",
            foreground=ACCENT_GOLD,
            font=("Consolas", 10, "bold")
        )
        style.map("Archive.Treeview", background=[("selected", RED_CRIMSON)], foreground=[("selected", TEXT_IVORY)])

        tree_frame = tk.Frame(left_pane, bg=BG_PANEL)
        tree_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical")
        columns = ("id", "title", "status")
        tree = ttk.Treeview(tree_frame, columns=columns, show="headings", yscrollcommand=tree_scroll.set, style="Archive.Treeview")
        tree_scroll.config(command=tree.yview)

        tree.heading("id", text="DOSSIER")
        tree.heading("title", text="CASE TITLE")
        tree.heading("status", text="STATUS")

        tree.column("id", width=85, anchor="center")
        tree.column("title", width=290, anchor="w")
        tree.column("status", width=120, anchor="center")

        tree.pack(side="left", fill="both", expand=True)
        tree_scroll.pack(side="right", fill="y")

        # Right Live Dossier Elements
        lbl_dossier_id = tk.Label(right_pane, text="DOSSIER PREVIEW", font=FONT_MONO_STAMP, fg=RED_BRIGHT, bg=BG_CARD)
        lbl_dossier_id.pack(anchor="w", padx=25, pady=(20, 2))

        lbl_case_title = tk.Label(right_pane, text="Select a case from the index", font=FONT_TITLE_MED, fg=TEXT_IVORY, bg=BG_CARD)
        lbl_case_title.pack(anchor="w", padx=25, pady=(0, 5))

        lbl_meta = tk.Label(right_pane, text="", font=FONT_MONO_SMALL, fg=TEXT_MUTED, bg=BG_CARD)
        lbl_meta.pack(anchor="w", padx=25, pady=(0, 10))

        dossier_box = tk.Frame(right_pane, bg="#0E0306", highlightthickness=1, highlightbackground=BORDER_RED)
        dossier_box.pack(fill="both", expand=True, padx=25, pady=(0, 15))

        lbl_victim = tk.Label(dossier_box, text="", font=FONT_BODY_BOLD, fg=ACCENT_GOLD, bg="#0E0306")
        lbl_victim.pack(anchor="w", padx=15, pady=(15, 6))

        lbl_synopsis = tk.Label(dossier_box, text="", font=FONT_BODY_LARGE, fg=TEXT_IVORY, bg="#0E0306", wraplength=480, justify="left")
        lbl_synopsis.pack(anchor="w", padx=15, pady=4)

        lbl_cod = tk.Label(dossier_box, text="", font=FONT_BODY, fg=RED_BRIGHT, bg="#0E0306")
        lbl_cod.pack(anchor="w", padx=15, pady=8)

        btn_launch = tk.Button(
            right_pane, text="OPEN CASE FILE & COMMENCE INVESTIGATION →", font=FONT_BUTTON,
            fg=TEXT_IVORY, bg=RED_CRIMSON, activebackground=RED_BRIGHT,
            relief="flat", cursor="hand2", padx=20, pady=12
        )
        btn_launch.pack(fill="x", padx=25, pady=(0, 20))

        case_map = {c["id"]: c for c in all_cases}

        def on_case_select(event=None):
            selected = tree.selection()
            if not selected:
                return
            item_vals = tree.item(selected[0], "values")
            c_id = item_vals[0]
            c = case_map.get(c_id)
            if not c:
                return

            is_solved = c["id"] in self.progress_data["solved_cases"]

            lbl_dossier_id.config(text=f"CLASSIFIED DOSSIER // {c['id']}")
            lbl_case_title.config(text=c["title"].upper())
            lbl_meta.config(text=f"LOCATION: {c['location']}   |   TIME: {c['time']}   |   CATEGORY: {c['category']}")
            lbl_victim.config(text=f"VICTIM: {c['victim']}")
            lbl_synopsis.config(text=c["synopsis"])
            lbl_cod.config(text=f"CAUSE OF DEATH: {c['cause_of_death']}")

            btn_txt = "RE-EXAMINE ARCHIVE FILE →" if is_solved else "OPEN CASE FILE & COMMENCE INVESTIGATION →"
            btn_bg = "#2C1E0A" if is_solved else RED_CRIMSON
            btn_launch.config(text=btn_txt, bg=btn_bg, command=lambda c_ref=c: self.start_investigation(c_ref))

        tree.bind("<<TreeviewSelect>>", on_case_select)

        # Insert all cases into the list
        for c in all_cases:
            is_solved = c["id"] in self.progress_data["solved_cases"]
            status_text = "✓ CLOSED" if is_solved else "● ACTIVE"
            tree.insert("", "end", values=(c["id"], c["title"], status_text))

        # Select first case automatically
        children = tree.get_children()
        if children:
            tree.selection_set(children[0])
            on_case_select()

    # =========================================================================
    # 4. INVESTIGATION HUB SCREEN
    # =========================================================================
    def start_investigation(self, case_obj):
        self.current_case = case_obj
        self.investigation_state = {
            "examined_evidence": set(),
            "interviewed_suspects": set(),
            "dialogue_step": {s["id"]: 0 for s in case_obj["suspects"]},
            "wrong_guesses": 0,
            "hints_revealed": 0
        }
        self.show_investigation_view("CRIME_SCENE")

    def show_investigation_view(self, tab_key="CRIME_SCENE"):
        self.clear_screen()
        c = self.current_case

        root = tk.Frame(self.container, bg=BG_DEEP)
        root.pack(fill="both", expand=True)

        top_bar = tk.Frame(root, bg=BG_PANEL, height=80, highlightthickness=1, highlightbackground=BORDER_RED)
        top_bar.pack(fill="x", padx=25, pady=(15, 8))

        tk.Button(
            top_bar, text="← ARCHIVE DOSSIER", font=FONT_BUTTON,
            fg=TEXT_IVORY, bg=BORDER_RED, activebackground=RED_BRIGHT,
            relief="flat", cursor="hand2", command=self.show_archive
        ).pack(side="left", padx=15, pady=15)

        title_box = tk.Frame(top_bar, bg=BG_PANEL)
        title_box.pack(side="left", padx=15, pady=10)
        tk.Label(title_box, text=f"ACTIVE HOMICIDE INVESTIGATION // {c['id']}", font=FONT_MONO_SMALL, fg=RED_BRIGHT, bg=BG_PANEL).pack(anchor="w")
        tk.Label(title_box, text=c["title"].upper(), font=FONT_TITLE_MED, fg=TEXT_IVORY, bg=BG_PANEL).pack(anchor="w")

        ev_done = len(self.investigation_state["examined_evidence"])
        ev_total = len(c["evidence"])
        sus_done = len(self.investigation_state["interviewed_suspects"])
        sus_total = len(c["suspects"])
        prog_pct = int(((ev_done / ev_total) * 0.5 + (sus_done / sus_total) * 0.5) * 100)

        prog_box = tk.Frame(top_bar, bg=BG_PANEL)
        prog_box.pack(side="right", padx=20, pady=10)
        tk.Label(prog_box, text=f"CASE COMPLETION: {prog_pct}%", font=FONT_MONO_STAMP, fg=ACCENT_GOLD, bg=BG_PANEL).pack(anchor="e")
        tk.Label(prog_box, text=f"Clues: {ev_done}/{ev_total} | Suspects: {sus_done}/{sus_total}", font=FONT_MONO_SMALL, fg=TEXT_MUTED, bg=BG_PANEL).pack(anchor="e")

        nav_bar = tk.Frame(root, bg="#0A0305", height=45, highlightthickness=1, highlightbackground="#24070D")
        nav_bar.pack(fill="x", padx=25, pady=(0, 10))

        tabs = [
            ("CRIME SCENE", "CRIME_SCENE"),
            ("PHYSICAL EVIDENCE", "EVIDENCE"),
            ("SUSPECT PROFILES", "SUSPECTS"),
            ("INTERROGATIONS", "INTERROGATION"),
            ("TIMELINE RECONSTRUCTION", "TIMELINE"),
            ("FINAL DEDUCTION", "DEDUCTION")
        ]

        for label, key in tabs:
            is_active = (key == tab_key)
            t_bg = RED_CRIMSON if is_active else "#120508"
            t_fg = TEXT_IVORY if is_active else TEXT_MUTED

            cmd = lambda k=key: self.show_investigation_view(k)
            btn = tk.Button(
                nav_bar, text=label, font=FONT_MONO_STAMP,
                fg=t_fg, bg=t_bg, activebackground=RED_BRIGHT, activeforeground=TEXT_IVORY,
                relief="flat", cursor="hand2", padx=15, pady=8, command=cmd
            )
            btn.pack(side="left", padx=2, pady=2)

        content_frame = tk.Frame(root, bg=BG_PANEL, highlightthickness=1, highlightbackground=BORDER_RED)
        content_frame.pack(fill="both", expand=True, padx=25, pady=(0, 15))

        if tab_key == "CRIME_SCENE":
            self.render_crime_scene(content_frame)
        elif tab_key == "EVIDENCE":
            self.render_evidence_room(content_frame)
        elif tab_key == "SUSPECTS":
            self.render_suspects_profile(content_frame)
        elif tab_key == "INTERROGATION":
            self.render_interrogation_room(content_frame)
        elif tab_key == "TIMELINE":
            self.render_timeline_room(content_frame)
        elif tab_key == "DEDUCTION":
            self.render_deduction_board(content_frame)

    # -------------------------------------------------------------------------
    # SUB-VIEW: Crime Scene
    # -------------------------------------------------------------------------
    def render_crime_scene(self, parent):
        c = self.current_case

        left = tk.Frame(parent, bg=BG_PANEL)
        left.pack(side="left", fill="both", expand=True, padx=25, pady=20)

        tk.Label(left, text="INCIDENT BRIEFING & PERIMETER ANALYSIS", font=FONT_TITLE_SUB, fg=RED_BRIGHT, bg=BG_PANEL).pack(anchor="w", pady=(0, 10))

        syn_box = tk.Frame(left, bg=BG_CARD, highlightthickness=1, highlightbackground=BORDER_RED)
        syn_box.pack(fill="x", pady=6, ipady=8)
        tk.Label(syn_box, text="PRIMARY DISPATCH REPORT", font=FONT_MONO_SMALL, fg=RED_CRIMSON, bg=BG_CARD).pack(anchor="w", padx=15, pady=(8, 2))
        tk.Label(syn_box, text=c["synopsis"], font=FONT_BODY_LARGE, fg=TEXT_IVORY, bg=BG_CARD, wraplength=520, justify="left").pack(anchor="w", padx=15, pady=4)

        cod_box = tk.Frame(left, bg="#1A0409", highlightthickness=1, highlightbackground=RED_CRIMSON)
        cod_box.pack(fill="x", pady=10, ipady=6)
        tk.Label(cod_box, text="CORONER PRELIMINARY CAUSE OF DEATH:", font=FONT_MONO_SMALL, fg=ACCENT_GOLD, bg="#1A0409").pack(anchor="w", padx=15, pady=(6, 2))
        tk.Label(cod_box, text=c["cause_of_death"], font=FONT_BODY_BOLD, fg=TEXT_IVORY, bg="#1A0409").pack(anchor="w", padx=15, pady=(0, 6))

        right = tk.Frame(parent, bg="#0B0305", highlightthickness=1, highlightbackground=BORDER_RED, width=460)
        right.pack(side="right", fill="both", padx=(10, 20), pady=20)
        right.pack_propagate(False)

        tk.Label(right, text="CRIME SCENE MARKERS & PHYSICAL TRACES", font=FONT_MONO_STAMP, fg=TEXT_IVORY, bg="#0B0305").pack(anchor="w", padx=15, pady=(15, 10))

        for idx, obs in enumerate(c["scene_details"], start=1):
            item_frame = tk.Frame(right, bg="#140609", highlightthickness=1, highlightbackground="#24070D")
            item_frame.pack(fill="x", padx=15, pady=5)

            marker = tk.Label(item_frame, text=f"MARKER #{idx:02d}", font=FONT_MONO_STAMP, fg=RED_BRIGHT, bg="#140609")
            marker.pack(anchor="w", padx=10, pady=(6, 2))

            desc = tk.Label(item_frame, text=obs, font=FONT_BODY, fg=TEXT_IVORY, bg="#140609", wraplength=400, justify="left")
            desc.pack(anchor="w", padx=10, pady=(0, 6))

    # -------------------------------------------------------------------------
    # SUB-VIEW: Evidence Room
    # -------------------------------------------------------------------------
    def render_evidence_room(self, parent):
        c = self.current_case

        left_frame = tk.Frame(parent, bg=BG_PANEL, width=420)
        left_frame.pack(side="left", fill="y", padx=20, pady=20)
        left_frame.pack_propagate(False)

        tk.Label(left_frame, text="LOGGED FORENSIC CLUES", font=FONT_TITLE_SUB, fg=RED_BRIGHT, bg=BG_PANEL).pack(anchor="w", pady=(0, 10))

        right_frame = tk.Frame(parent, bg=BG_CARD, highlightthickness=1, highlightbackground=BORDER_RED)
        right_frame.pack(side="right", fill="both", expand=True, padx=(10, 20), pady=20)

        self.ev_detail_label_id = tk.Label(right_frame, text="EVIDENCE INSPECTOR", font=FONT_MONO_STAMP, fg=RED_CRIMSON, bg=BG_CARD)
        self.ev_detail_label_id.pack(anchor="w", padx=25, pady=(20, 2))

        self.ev_detail_title = tk.Label(right_frame, text="Select a clue from the log to examine", font=FONT_TITLE_SUB, fg=TEXT_IVORY, bg=BG_CARD)
        self.ev_detail_title.pack(anchor="w", padx=25, pady=(0, 10))

        self.ev_detail_desc = tk.Label(right_frame, text="Evidence logs contain critical contradictions and forensic data.", font=FONT_BODY_LARGE, fg=TEXT_MUTED, bg=BG_CARD, wraplength=520, justify="left")
        self.ev_detail_desc.pack(anchor="w", padx=25, pady=5)

        self.ev_deeper_box = tk.Frame(right_frame, bg="#100306", highlightthickness=1, highlightbackground=BORDER_RED)
        self.ev_deeper_box.pack(fill="both", expand=True, padx=25, pady=20)

        self.ev_deeper_title = tk.Label(self.ev_deeper_box, text="LAB FORENSIC ANALYSIS", font=FONT_MONO_STAMP, fg=ACCENT_GOLD, bg="#100306")
        self.ev_deeper_title.pack(anchor="w", padx=15, pady=(15, 5))

        self.ev_deeper_text = tk.Label(self.ev_deeper_box, text="[Clue not yet examined in detail]", font=FONT_BODY, fg=TEXT_DIM, bg="#100306", wraplength=480, justify="left")
        self.ev_deeper_text.pack(anchor="w", padx=15, pady=5)

        self.ev_examine_btn = tk.Button(
            right_frame, text="CONDUCT MICROSCOPIC / CHEMICAL ANALYSIS", font=FONT_BUTTON,
            fg=TEXT_IVORY, bg=RED_CRIMSON, activebackground=RED_BRIGHT,
            relief="flat", cursor="hand2", state="disabled"
        )
        self.ev_examine_btn.pack(anchor="w", padx=25, pady=(0, 20))

        def select_evidence(ev_item):
            ev_id = ev_item["id"]
            self.ev_detail_label_id.config(text=f"EVIDENCE DOSSIER // {ev_id}")
            self.ev_detail_title.config(text=ev_item["name"])
            self.ev_detail_desc.config(text=ev_item["desc"])

            is_examined = ev_id in self.investigation_state["examined_evidence"]

            if is_examined:
                self.ev_deeper_text.config(text=ev_item["details"], fg=TEXT_IVORY)
                self.ev_examine_btn.config(state="disabled", text="ANALYSIS COMPLETED ✓", bg="#20060B")
            else:
                self.ev_deeper_text.config(text="Forensic lab analysis available. Click below to inspect deeper layers.", fg=TEXT_DIM)
                self.ev_examine_btn.config(
                    state="normal", text="CONDUCT FORENSIC EXAMINATION", bg=RED_CRIMSON,
                    command=lambda: perform_examination(ev_item)
                )

        def perform_examination(ev_item):
            self.investigation_state["examined_evidence"].add(ev_item["id"])
            select_evidence(ev_item)

        for ev in c["evidence"]:
            is_done = ev["id"] in self.investigation_state["examined_evidence"]
            btn_bg = "#1B070D" if is_done else BG_CARD
            border_c = ACCENT_GOLD if is_done else "#24070D"

            btn_frame = tk.Frame(left_frame, bg=btn_bg, highlightthickness=1, highlightbackground=border_c)
            btn_frame.pack(fill="x", pady=4)

            b = tk.Button(
                btn_frame, text=f"{ev['id']}: {ev['name']}", font=FONT_BODY_BOLD,
                fg=TEXT_IVORY if not is_done else ACCENT_GOLD, bg=btn_bg,
                activebackground=RED_CRIMSON, activeforeground=TEXT_IVORY,
                relief="flat", anchor="w", cursor="hand2", padx=10, pady=8,
                command=lambda item=ev: select_evidence(item)
            )
            b.pack(fill="x")

        if c["evidence"]:
            select_evidence(c["evidence"][0])

    # -------------------------------------------------------------------------
    # SUB-VIEW: Suspect Profiles
    # -------------------------------------------------------------------------
    def render_suspects_profile(self, parent):
        c = self.current_case

        left_list = tk.Frame(parent, bg=BG_PANEL, width=380)
        left_list.pack(side="left", fill="y", padx=20, pady=20)
        left_list.pack_propagate(False)

        tk.Label(left_list, text="PERSONS OF INTEREST", font=FONT_TITLE_SUB, fg=RED_BRIGHT, bg=BG_PANEL).pack(anchor="w", pady=(0, 10))

        right_dossier = tk.Frame(parent, bg=BG_CARD, highlightthickness=1, highlightbackground=BORDER_RED)
        right_dossier.pack(side="right", fill="both", expand=True, padx=(10, 20), pady=20)

        lbl_id = tk.Label(right_dossier, text="SUSPECT PROFILE", font=FONT_MONO_STAMP, fg=RED_CRIMSON, bg=BG_CARD)
        lbl_id.pack(anchor="w", padx=25, pady=(20, 2))

        lbl_name = tk.Label(right_dossier, text="Select a suspect from the list", font=FONT_TITLE_MED, fg=TEXT_IVORY, bg=BG_CARD)
        lbl_name.pack(anchor="w", padx=25, pady=(0, 4))

        lbl_role = tk.Label(right_dossier, text="", font=FONT_BODY_BOLD, fg=TEXT_MUTED, bg=BG_CARD)
        lbl_role.pack(anchor="w", padx=25, pady=(0, 15))

        profile_box = tk.Frame(right_dossier, bg="#0E0407", highlightthickness=1, highlightbackground=BORDER_RED)
        profile_box.pack(fill="both", expand=True, padx=25, pady=(0, 20))

        lbl_alibi_title = tk.Label(profile_box, text="STATED ALIBI AT TIME OF MURDER:", font=FONT_MONO_STAMP, fg=ACCENT_GOLD, bg="#0E0407")
        lbl_alibi_title.pack(anchor="w", padx=15, pady=(15, 2))

        lbl_alibi = tk.Label(profile_box, text="", font=FONT_BODY_LARGE, fg=TEXT_IVORY, bg="#0E0407", wraplength=500, justify="left")
        lbl_alibi.pack(anchor="w", padx=15, pady=(0, 15))

        lbl_motive_title = tk.Label(profile_box, text="ESTABLISHED MOTIVE / CONFLICT:", font=FONT_MONO_STAMP, fg=RED_BRIGHT, bg="#0E0407")
        lbl_motive_title.pack(anchor="w", padx=15, pady=(10, 2))

        lbl_motive = tk.Label(profile_box, text="", font=FONT_BODY_LARGE, fg=TEXT_IVORY, bg="#0E0407", wraplength=500, justify="left")
        lbl_motive.pack(anchor="w", padx=15, pady=(0, 15))

        btn_go_interrogate = tk.Button(
            right_dossier, text="COMMENCE FORMAL INTERROGATION →", font=FONT_BUTTON,
            fg=TEXT_IVORY, bg=RED_CRIMSON, activebackground=RED_BRIGHT,
            relief="flat", cursor="hand2"
        )
        btn_go_interrogate.pack(anchor="w", padx=25, pady=(0, 20))

        def display_suspect(sus):
            lbl_id.config(text=f"SUSPECT DOSSIER // {sus['id']}")
            lbl_name.config(text=sus["name"])
            lbl_role.config(text=f"RELATIONSHIP: {sus['role']}")
            lbl_alibi.config(text=f"\"{sus['alibi']}\"")
            lbl_motive.config(text=sus["motive"])

            btn_go_interrogate.config(
                command=lambda: self.show_investigation_view("INTERROGATION")
            )

        for s in c["suspects"]:
            is_int = s["id"] in self.investigation_state["interviewed_suspects"]
            bg_c = "#1B070D" if is_int else BG_CARD
            border_c = ACCENT_GOLD if is_int else "#24070D"

            s_frame = tk.Frame(left_list, bg=bg_c, highlightthickness=1, highlightbackground=border_c)
            s_frame.pack(fill="x", pady=5)

            btn = tk.Button(
                s_frame, text=f"{s['name']}\n{s['role']}", font=FONT_BODY_BOLD,
                fg=TEXT_IVORY if not is_int else ACCENT_GOLD, bg=bg_c,
                activebackground=RED_CRIMSON, activeforeground=TEXT_IVORY,
                relief="flat", anchor="w", justify="left", cursor="hand2", padx=10, pady=8,
                command=lambda item=s: display_suspect(item)
            )
            btn.pack(fill="x")

        if c["suspects"]:
            display_suspect(c["suspects"][0])

    # -------------------------------------------------------------------------
    # SUB-VIEW: Interrogation Room
    # -------------------------------------------------------------------------
    def render_interrogation_room(self, parent):
        c = self.current_case

        left_pane = tk.Frame(parent, bg=BG_PANEL, width=320)
        left_pane.pack(side="left", fill="y", padx=20, pady=20)
        left_pane.pack_propagate(False)

        tk.Label(left_pane, text="SUBJECT IN CUSTODY", font=FONT_TITLE_SUB, fg=RED_BRIGHT, bg=BG_PANEL).pack(anchor="w", pady=(0, 10))

        right_pane = tk.Frame(parent, bg=BG_CARD, highlightthickness=1, highlightbackground=BORDER_RED)
        right_pane.pack(side="right", fill="both", expand=True, padx=(10, 20), pady=20)

        transcript_box = tk.Frame(right_pane, bg="#080204", highlightthickness=1, highlightbackground=BORDER_RED)
        transcript_box.pack(fill="both", expand=True, padx=20, pady=(20, 10))

        transcript_text = tk.Text(
            transcript_box, bg="#080204", fg=TEXT_IVORY,
            font=("Segoe UI", 11), wrap="word", relief="flat", padx=15, pady=15
        )
        t_scroll = ttk.Scrollbar(transcript_box, orient="vertical", command=transcript_text.yview)
        transcript_text.config(yscrollcommand=t_scroll.set)

        transcript_text.pack(side="left", fill="both", expand=True)
        t_scroll.pack(side="right", fill="y")

        transcript_text.tag_configure("det", foreground=RED_BRIGHT, font=("Consolas", 11, "bold"))
        transcript_text.tag_configure("sus", foreground=ACCENT_GOLD, font=("Consolas", 11, "bold"))
        transcript_text.tag_configure("body", foreground=TEXT_IVORY, font=("Segoe UI", 11))

        control_frame = tk.Frame(right_pane, bg=BG_CARD)
        control_frame.pack(fill="x", padx=20, pady=(0, 15))

        active_suspect = [c["suspects"][0]]

        def load_suspect_dialogue(sus):
            active_suspect[0] = sus
            self.investigation_state["interviewed_suspects"].add(sus["id"])
            curr_step = self.investigation_state["dialogue_step"].get(sus["id"], 0)
            dialogues = sus.get("dialogue", [])

            transcript_text.config(state="normal")
            transcript_text.delete("1.0", "end")

            for q, a in dialogues[:curr_step + 1]:
                transcript_text.insert("end", "DETECTIVE:\n", "det")
                transcript_text.insert("end", f"{q}\n\n", "body")
                transcript_text.insert("end", f"{sus['name'].upper()}:\n", "sus")
                transcript_text.insert("end", f"{a}\n\n", "body")
                transcript_text.insert("end", "-" * 40 + "\n\n", "body")

            transcript_text.config(state="disabled")
            transcript_text.see("end")

            for w in control_frame.winfo_children():
                w.destroy()

            if curr_step + 1 < len(dialogues):
                btn_next = tk.Button(
                    control_frame, text="PRESS SUSPECT FURTHER WITH EVIDENCE →", font=FONT_BUTTON,
                    fg=TEXT_IVORY, bg=RED_CRIMSON, activebackground=RED_BRIGHT,
                    relief="flat", cursor="hand2", padx=15, pady=8,
                    command=lambda: advance_dialogue(sus)
                )
                btn_next.pack(side="left")
            else:
                tk.Label(control_frame, text="SUBJECT HAS PROVIDED FULL STATEMENT.", font=FONT_MONO_STAMP, fg=ACCENT_GOLD, bg=BG_CARD).pack(side="left", pady=8)

        def advance_dialogue(sus):
            self.investigation_state["dialogue_step"][sus["id"]] = self.investigation_state["dialogue_step"].get(sus["id"], 0) + 1
            load_suspect_dialogue(sus)

        for s in c["suspects"]:
            is_int = s["id"] in self.investigation_state["interviewed_suspects"]
            bg_c = "#1B070D" if is_int else BG_CARD
            border_c = ACCENT_GOLD if is_int else "#24070D"

            s_frame = tk.Frame(left_pane, bg=bg_c, highlightthickness=1, highlightbackground=border_c)
            s_frame.pack(fill="x", pady=4)

            btn = tk.Button(
                s_frame, text=f"EXAMINE: {s['name']}", font=FONT_BODY_BOLD,
                fg=TEXT_IVORY if not is_int else ACCENT_GOLD, bg=bg_c,
                activebackground=RED_CRIMSON, activeforeground=TEXT_IVORY,
                relief="flat", anchor="w", cursor="hand2", padx=10, pady=8,
                command=lambda item=s: load_suspect_dialogue(item)
            )
            btn.pack(fill="x")

        if c["suspects"]:
            load_suspect_dialogue(c["suspects"][0])

    # -------------------------------------------------------------------------
    # SUB-VIEW: Timeline Reconstruction
    # -------------------------------------------------------------------------
    def render_timeline_room(self, parent):
        c = self.current_case

        root_tl = tk.Frame(parent, bg=BG_PANEL)
        root_tl.pack(fill="both", expand=True, padx=25, pady=20)

        tk.Label(root_tl, text="FORENSIC TIMELINE RECONSTRUCTION", font=FONT_TITLE_SUB, fg=RED_BRIGHT, bg=BG_PANEL).pack(anchor="w", pady=(0, 10))

        tl_box = tk.Frame(root_tl, bg=BG_CARD, highlightthickness=1, highlightbackground=BORDER_RED)
        tl_box.pack(fill="both", expand=True)

        tl_text = tk.Text(tl_box, bg=BG_CARD, fg=TEXT_IVORY, font=("Segoe UI", 11), wrap="word", relief="flat", padx=20, pady=20)
        tl_scroll = ttk.Scrollbar(tl_box, orient="vertical", command=tl_text.yview)
        tl_text.config(yscrollcommand=tl_scroll.set)

        tl_text.pack(side="left", fill="both", expand=True)
        tl_scroll.pack(side="right", fill="y")

        tl_text.tag_configure("time", foreground=RED_BRIGHT, font=("Georgia", 13, "bold"))
        tl_text.tag_configure("desc", foreground=TEXT_IVORY, font=("Segoe UI", 12))
        tl_text.tag_configure("sep", foreground=BORDER_RED, font=("Consolas", 10))

        for idx, (t_stamp, event_desc) in enumerate(c["timeline"], start=1):
            tl_text.insert("end", f"[{t_stamp}]   EVENT SEQUENCE #{idx:02d}\n", "time")
            tl_text.insert("end", f"{event_desc}\n\n", "desc")
            tl_text.insert("end", "—" * 60 + "\n\n", "sep")

        tl_text.config(state="disabled")

    # -------------------------------------------------------------------------
    # SUB-VIEW: Final Deduction Board
    # -------------------------------------------------------------------------
    def render_deduction_board(self, parent):
        c = self.current_case

        root_db = tk.Frame(parent, bg=BG_PANEL)
        root_db.pack(fill="both", expand=True, padx=25, pady=20)

        tk.Label(root_db, text="FINAL HOMICIDE CHARGE & ARREST WARRANT", font=FONT_TITLE_SUB, fg=RED_BRIGHT, bg=BG_PANEL).pack(anchor="w", pady=(0, 6))
        tk.Label(root_db, text="Identify the perpetrator based on timeline contradictions, physical evidence, and broken alibis.", font=FONT_BODY, fg=TEXT_MUTED, bg=BG_PANEL).pack(anchor="w", pady=(0, 15))

        center_frame = tk.Frame(root_db, bg=BG_CARD, highlightthickness=1, highlightbackground=BORDER_RED)
        center_frame.pack(fill="both", expand=True, ipady=10)

        tk.Label(center_frame, text="WHO KILLED THE VICTIM?", font=FONT_MONO_STAMP, fg=ACCENT_GOLD, bg=BG_CARD).pack(anchor="w", padx=25, pady=(20, 10))

        selected_suspect = tk.StringVar(value="")

        sus_options_frame = tk.Frame(center_frame, bg=BG_CARD)
        sus_options_frame.pack(fill="x", padx=25, pady=5)

        for sus in c["suspects"]:
            r_card = tk.Frame(sus_options_frame, bg="#140609", highlightthickness=1, highlightbackground="#24070D")
            r_card.pack(fill="x", pady=4)

            rb = tk.Radiobutton(
                r_card, text=f"{sus['name']}  —  {sus['role']}",
                variable=selected_suspect, value=sus["id"],
                font=FONT_BODY_BOLD, fg=TEXT_IVORY, bg="#140609",
                selectcolor="#4A0C16", activebackground="#140609", activeforeground=TEXT_IVORY,
                cursor="hand2", padx=15, pady=8
            )
            rb.pack(anchor="w")

        self.feedback_box = tk.Frame(center_frame, bg="#0E0305", highlightthickness=1, highlightbackground=BORDER_RED)
        self.feedback_box.pack(fill="x", padx=25, pady=15, ipady=6)

        self.lbl_feedback_title = tk.Label(self.feedback_box, text="DEDUCTION BOARD STATUS: READY", font=FONT_MONO_STAMP, fg=TEXT_MUTED, bg="#0E0305")
        self.lbl_feedback_title.pack(anchor="w", padx=15, pady=(8, 2))

        self.lbl_feedback_msg = tk.Label(
            self.feedback_box,
            text="Review all physical clues and timeline gaps before submitting formal homicide charges.",
            font=FONT_BODY, fg=TEXT_IVORY, bg="#0E0305", wraplength=900, justify="left"
        )
        self.lbl_feedback_msg.pack(anchor="w", padx=15, pady=(0, 8))

        btn_submit = tk.Button(
            center_frame, text="SUBMIT FORMAL INDICTMENT →", font=FONT_BUTTON,
            fg=TEXT_IVORY, bg=RED_CRIMSON, activebackground=RED_BRIGHT,
            relief="flat", cursor="hand2", padx=20, pady=10,
            command=lambda: self.validate_deduction(selected_suspect.get())
        )
        btn_submit.pack(anchor="w", padx=25, pady=(5, 15))

    def validate_deduction(self, chosen_id):
        if not chosen_id:
            messagebox.showwarning("Incomplete Indictment", "You must select a prime suspect before submitting the case charges.")
            return

        c = self.current_case
        if chosen_id == c["murderer_id"]:
            save_manager.mark_case_solved(c["id"])
            self.show_case_closed_screen()
        else:
            save_manager.record_wrong_attempt()
            self.investigation_state["wrong_guesses"] += 1
            wg = self.investigation_state["wrong_guesses"]

            hints = c.get("hints", [])
            hint_idx = min(wg - 1, len(hints) - 1)
            hint_text = hints[hint_idx] if hints else "Re-examine suspect alibis against the physical crime timestamps."

            self.feedback_box.config(bg="#22050B", highlightbackground=RED_BRIGHT)
            self.lbl_feedback_title.config(text=f"DEDUCTION INCONCLUSIVE // ATTEMPT #{wg} REJECTED", fg=RED_BRIGHT, bg="#22050B")
            self.lbl_feedback_msg.config(
                text=f"The prosecutor rejected this indictment: The evidence does not fully link this person without contradictions.\n\n{hint_text}",
                fg=TEXT_IVORY, bg="#22050B"
            )

    # =========================================================================
    # 5. CASE CLOSED SCREEN
    # =========================================================================
    def show_case_closed_screen(self):
        self.clear_screen()
        c = self.current_case

        root = tk.Frame(self.container, bg=BG_DEEP)
        root.pack(fill="both", expand=True)

        center_card = tk.Frame(root, bg=BG_PANEL, highlightthickness=2, highlightbackground=ACCENT_GOLD, width=900, height=640)
        center_card.pack(expand=True, padx=40, pady=30)
        center_card.pack_propagate(False)

        tk.Label(center_card, text="★ ★ ★  FEDERAL ARCHIVE CONVICTION CONFIRMED  ★ ★ ★", font=FONT_MONO_STAMP, fg=ACCENT_GOLD, bg=BG_PANEL).pack(pady=(25, 5))
        tk.Label(center_card, text="CASE CLOSED", font=("Georgia", 38, "bold"), fg=TEXT_IVORY, bg=BG_PANEL).pack()
        tk.Label(center_card, text=f"THE PERPETRATOR WAS: {c['murderer_name'].upper()}", font=FONT_TITLE_SUB, fg=RED_BRIGHT, bg=BG_PANEL).pack(pady=(5, 15))

        sol_box = tk.Frame(center_card, bg="#080204", highlightthickness=1, highlightbackground=BORDER_RED)
        sol_box.pack(fill="both", expand=True, padx=30, pady=10)

        tk.Label(sol_box, text="DEDUCTION SYNTHESIS & RECONSTRUCTION", font=FONT_MONO_STAMP, fg=ACCENT_GOLD, bg="#080204").pack(anchor="w", padx=20, pady=(15, 6))
        tk.Label(sol_box, text=c["solution_summary"], font=FONT_BODY_LARGE, fg=TEXT_IVORY, bg="#080204", wraplength=800, justify="left").pack(anchor="w", padx=20, pady=6)

        rank = save_manager.get_rank(len(save_manager.load_progress()["solved_cases"]))
        stat_lbl = f"SOLVED CASES RECORDED: {len(save_manager.load_progress()['solved_cases'])}  |  CURRENT RANK: {rank}"
        tk.Label(center_card, text=stat_lbl, font=FONT_MONO_STAMP, fg=TEXT_MUTED, bg=BG_PANEL).pack(pady=10)

        tk.Button(
            center_card, text="RETURN TO CASE ARCHIVE →", font=FONT_BUTTON,
            fg=BG_DEEP, bg=ACCENT_GOLD, activebackground="#F5D77F", activeforeground=BG_DEEP,
            relief="flat", cursor="hand2", padx=25, pady=10,
            command=self.show_archive
        ).pack(pady=(5, 25))

    # =========================================================================
    # 6. DETECTIVE RECORD SCREEN
    # =========================================================================
    def show_record(self):
        self.clear_screen()
        data = save_manager.load_progress()

        root = tk.Frame(self.container, bg=BG_DEEP)
        root.pack(fill="both", expand=True)

        top_bar = tk.Frame(root, bg=BG_PANEL, height=70, highlightthickness=1, highlightbackground=BORDER_RED)
        top_bar.pack(fill="x", padx=25, pady=(20, 15))

        tk.Button(
            top_bar, text="← MAIN MENU", font=FONT_BUTTON,
            fg=TEXT_IVORY, bg=BORDER_RED, activebackground=RED_BRIGHT,
            relief="flat", cursor="hand2", command=self.show_main_menu
        ).pack(side="left", padx=15, pady=12)

        tk.Label(top_bar, text="DETECTIVE SERVICE RECORD & COMMENDATIONS", font=FONT_TITLE_MED, fg=TEXT_IVORY, bg=BG_PANEL).pack(side="left", padx=20)

        content = tk.Frame(root, bg=BG_PANEL, highlightthickness=1, highlightbackground=BORDER_RED)
        content.pack(fill="both", expand=True, padx=25, pady=(0, 20))

        stat_bar = tk.Frame(content, bg="#0E0407", highlightthickness=1, highlightbackground=BORDER_RED)
        stat_bar.pack(fill="x", padx=25, pady=20)

        total_solved = len(data["solved_cases"])
        all_count = len(cases.get_all_cases())
        rank_name = save_manager.get_rank(total_solved)

        stats = [
            ("DETECTIVE RANK", rank_name),
            ("SOLVED RATIO", f"{total_solved} / {all_count}"),
            ("REJECTED CHARGES", str(data.get("wrong_attempts", 0))),
            ("CONVICTION CLEARANCE", f"{int((total_solved / max(1, total_solved + data.get('wrong_attempts', 0))) * 100)}%")
        ]

        for title, val in stats:
            card = tk.Frame(stat_bar, bg="#0E0407")
            card.pack(side="left", expand=True, padx=15, pady=15)
            tk.Label(card, text=title, font=FONT_MONO_SMALL, fg=TEXT_DIM, bg="#0E0407").pack()
            tk.Label(card, text=val, font=("Georgia", 16, "bold"), fg=ACCENT_GOLD if title == "DETECTIVE RANK" else TEXT_IVORY, bg="#0E0407").pack(pady=4)

        tk.Label(content, text="CLEARED HOMICIDE FILES", font=FONT_TITLE_SUB, fg=RED_BRIGHT, bg=BG_PANEL).pack(anchor="w", padx=25, pady=(10, 5))

        list_frame = tk.Frame(content, bg=BG_CARD, highlightthickness=1, highlightbackground="#24070D")
        list_frame.pack(fill="both", expand=True, padx=25, pady=(0, 20))

        if not data["solved_cases"]:
            tk.Label(list_frame, text="NO HOMICIDE CASES CURRENTLY SOLVED.\nACCESS THE CASE ARCHIVE TO COMMENCE INVESTIGATIONS.", font=FONT_BODY_LARGE, fg=TEXT_DIM, bg=BG_CARD).pack(expand=True)
        else:
            for c_id in data["solved_cases"]:
                case_item = cases.get_case_by_id(c_id)
                if case_item:
                    row = tk.Frame(list_frame, bg="#130508", highlightthickness=1, highlightbackground=ACCENT_GOLD)
                    row.pack(fill="x", padx=15, pady=5)
                    tk.Label(row, text="✓ CONVICTED", font=FONT_MONO_STAMP, fg=ACCENT_GOLD, bg="#130508").pack(side="left", padx=15, pady=8)
                    tk.Label(row, text=f"{case_item['id']} — {case_item['title']} (Perpetrator: {case_item['murderer_name']})", font=FONT_BODY_BOLD, fg=TEXT_IVORY, bg="#130508").pack(side="left", padx=10)

    # =========================================================================
    # 7. INVESTIGATION PROTOCOL SCREEN
    # =========================================================================
    def show_protocol(self):
        self.clear_screen()
        root = tk.Frame(self.container, bg=BG_DEEP)
        root.pack(fill="both", expand=True)

        top_bar = tk.Frame(root, bg=BG_PANEL, height=70, highlightthickness=1, highlightbackground=BORDER_RED)
        top_bar.pack(fill="x", padx=25, pady=(20, 15))

        tk.Button(
            top_bar, text="← MAIN MENU", font=FONT_BUTTON,
            fg=TEXT_IVORY, bg=BORDER_RED, activebackground=RED_BRIGHT,
            relief="flat", cursor="hand2", command=self.show_main_menu
        ).pack(side="left", padx=15, pady=12)

        tk.Label(top_bar, text="STANDARD FORENSIC INVESTIGATION PROTOCOL", font=FONT_TITLE_MED, fg=TEXT_IVORY, bg=BG_PANEL).pack(side="left", padx=20)

        panel = tk.Frame(root, bg=BG_PANEL, highlightthickness=1, highlightbackground=BORDER_RED)
        panel.pack(fill="both", expand=True, padx=25, pady=(0, 20))

        guidelines = [
            ("1. PHYSICAL CRIME SCENE MARKERS", "Begin by thoroughly reviewing the scene brief and markers. Subtle details such as broken clocks, mud prints, or open latches indicate points of entry, struggle, and precise impact times."),
            ("2. DEEP FORENSIC EXAMINATION", "Never rely only on surface descriptions of clues. Click 'CONDUCT FORENSIC EXAMINATION' in the Evidence room to unlock lab analysis, toxicological reports, fingerprints, and secret data."),
            ("3. CROSS-EXAMINING SUSPECT ALIBIS", "Interrogate each suspect repeatedly using 'PRESS SUSPECT FURTHER'. Liars often invent alibis that directly contradict receipts, surveillance logs, or fellow witness testimonies."),
            ("4. TIMELINE GAP ANALYSIS", "Cross-reference the forensic timeline against suspect movements. Murderers frequently claim to have been elsewhere during the exact five-to-ten-minute window of the killing."),
            ("5. PROGRESSIVE DEDUCTION & HINTS", "The murderer is never chosen at random. If an indictment fails, the prosecutor provides progressive forensic hints pointing towards the critical contradiction.")
        ]

        for title, text in guidelines:
            box = tk.Frame(panel, bg=BG_CARD, highlightthickness=1, highlightbackground=BORDER_RED)
            box.pack(fill="x", padx=25, pady=8, ipady=4)
            tk.Label(box, text=title, font=FONT_MONO_STAMP, fg=ACCENT_GOLD, bg=BG_CARD).pack(anchor="w", padx=15, pady=(6, 2))
            tk.Label(box, text=text, font=FONT_BODY, fg=TEXT_IVORY, bg=BG_CARD, wraplength=1050, justify="left").pack(anchor="w", padx=15, pady=(0, 6))


if __name__ == "__main__":
    app = TheCaseFilesApp()
    app.mainloop()