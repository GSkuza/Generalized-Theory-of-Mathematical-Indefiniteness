[
# OT1 PL
        "Twierdzenie Operacyjne 1 (Dynamiczne Progi): Progi klasyfikacyjne dla cząstek wiedzy (Ψᴷ) i cieni wiedzy (Ψʰ) są dynamicznie ustalane na podstawie percentyli globalnego rozkładu ocen (score) fragmentów informacji, co zapewnia adaptacyjność systemu GTMØ do zmieniającego się kontekstu epistemicznego oraz jakości danych wejściowych.",
        # OT1 EN
        "Operational Theorem 1 (Dynamic Thresholds): Classification thresholds for knowledge particles (Ψᴷ) and knowledge shadows (Ψʰ) are dynamically established based on percentiles of the global score distribution of information fragments, ensuring the GTMØ system's adaptability to changing epistemic contexts and input data quality.",
        # Objaśnienie OT1 PL
        """
        --- Objaśnienie (PL) ---
        **Definicje Kluczowe (z głównego systemu GTMØ):**
        * `DEF1_dyn_pl`: "Definicja (dynamiczna): Cząstka wiedzy Ψᴷ – fragment, dla którego Ψ_GTMØ(x) ≥ próg_cząstek (dynamiczny percentyl)."
        * `DEF2_dyn_pl`: "Definicja (dynamiczna): Cień wiedzy Ψʰ – fragment, dla którego Ψ_GTMØ(x) ≤ próg_cieni (dynamiczny percentyl)."
        * **Ocena (Score)**: Wartość liczbowa $s(x)$ przypisana fragmentowi $x$ przez operator $\text{Ψ_GTMØ}(x)$, wskazująca na jego względną "określoność".

        **Równania Podstawowe:**
        1.  Próg cząstek ($K_{thr}$): $K_{thr} = \text{Percentyl}(S, P_K)$
            * Gdzie $S = \{s(x_1), s(x_2), ..., s(x_n)\}$ to zbiór ocen wszystkich fragmentów w systemie, $P_K$ to docelowy percentyl dla cząstek (np. 85%).
        2.  Próg cieni ($H_{thr}$): $H_{thr} = \text{Percentyl}(S, P_H)$
            * Gdzie $P_H$ to docelowy percentyl dla cieni (np. 15%).
        3.  Warunek klasyfikacji Ψᴷ: $s(x) \ge K_{thr}$
        4.  Warunek klasyfikacji Ψʰ: $s(x) \le H_{thr}$

        **Wyjaśnienie:**
        To twierdzenie operacyjne podkreśla, że GTMØ nie stosuje statycznych wartości granicznych do rozróżniania fragmentów wiedzy (Ψᴷ) od jej cieni (Ψʰ). Zamiast tego, progi $K_{thr}$ i $H_{thr}$ są elastycznie obliczane na podstawie aktualnej dystrybucji ocen wszystkich fragmentów w systemie. Implementacja wykorzystuje funkcję `numpy.percentile(all_scores, K_percentile)`. Dzięki temu system automatycznie dostosowuje swoją wrażliwość – jeśli ogólna "jakość" informacji w systemie rośnie lub maleje, progi również się zmieniają, pozwalając na konsekwentną identyfikację relatywnie najbardziej i najmniej określonych fragmentów. Zapewnia to kluczową zdolność adaptacji GTMØ.
        """,
        # Explanation OT1 EN
        """
        --- Explanation (EN) ---
        **Key Definitions (from the main GTMØ system):**
        * `DEF1_dyn`: "(Dynamic) Definition: Knowledge particle Ψᴷ – fragment with Ψ_GTMØ(x) ≥ particle threshold (dynamic percentile)."
        * `DEF2_dyn`: "(Dynamic) Definition: Knowledge shadow Ψʰ – fragment with Ψ_GTMØ(x) ≤ shadow threshold (dynamic percentile)."
        * **Score**: A numerical value $s(x)$ assigned to a fragment $x$ by the $\text{Ψ_GTMØ}(x)$ operator, indicating its relative "definiteness."

        **Basic Equations:**
        1.  Particle Threshold ($K_{thr}$): $K_{thr} = \text{Percentile}(S, P_K)$
            * Where $S = \{s(x_1), s(x_2), ..., s(x_n)\}$ is the set of scores of all fragments in the system, $P_K$ is the target percentile for particles (e.g., 85%).
        2.  Shadow Threshold ($H_{thr}$): $H_{thr} = \text{Percentile}(S, P_H)$
            * Where $P_H$ is the target percentile for shadows (e.g., 15%).
        3.  Ψᴷ Classification Condition: $s(x) \ge K_{thr}$
        4.  Ψʰ Classification Condition: $s(x) \le H_{thr}$

        **Explanation:**
        This operational theorem highlights that GTMØ does not use static boundary values to distinguish knowledge particles (Ψᴷ) from their shadows (Ψʰ). Instead, the thresholds $K_{thr}$ and $H_{thr}$ are flexibly calculated based on the current distribution of scores of all fragments in the system. The implementation uses the `numpy.percentile(all_scores, K_percentile)` function. This allows the system to automatically adjust its sensitivity – if the overall "quality" of information in the system increases or decreases, the thresholds also change, enabling consistent identification of relatively the most and least definite fragments. This ensures GTMØ's crucial adaptability.
        """
    ),
    (
        # OT2 PL
        "Twierdzenie Operacyjne 2 (Meta-Pętla Sprzężenia Zwrotnego): Meta-pętla sprzężenia zwrotnego GTMØ iteracyjnie optymalizuje proces klasyfikacji i zarządzania nieokreślonością poprzez dynamiczną rekalibrację progów klasyfikacyjnych (Ψᴷ, Ψʰ) oraz identyfikację i potencjalną asymilację emergentnych typów informacji (Ψᴺ).",
        # OT2 EN
        "Operational Theorem 2 (Meta-Feedback Loop): The GTMØ meta-feedback loop iteratively optimizes the classification and indefiniteness management process through dynamic recalibration of classification thresholds (Ψᴷ, Ψʰ) and the identification and potential assimilation of emergent information types (Ψᴺ).",
        # Objaśnienie OT2 PL
        """
        --- Objaśnienie (PL) ---
        **Definicje Kluczowe:**
        * **Progi dynamiczne $K_{thr}, H_{thr}$**: Jak zdefiniowano w OT1.
        * **Ψᴺ (Cząstka Nowa/Emergentna)**: Fragment informacji (np. zawierający paradoks, sprzeczność, meta-informację) wskazujący na potencjalną nowość lub przekroczenie obecnych ram systemu. W kodzie detekcja opiera się na słowach kluczowych: `if "paradoks" in frag.lower() or ... new_types_detected.add("Ψᴺ (novel/emergent)")`.
        * `TH9`: "GTMØ minimizes cognitive noise and adapts the boundary of sense through iterative self-evaluation of thresholds."

        **Równania/Procesy Podstawowe:**
        1.  Obliczenie progów w iteracji $i$: $K_{thr}(i), H_{thr}(i) = \text{dynamic_thresholds}(\text{scores}(i))$
        2.  Klasyfikacja fragmentów w iteracji $i$: $\text{Typy}(i) = \text{Klasyfikuj}(\text{Fragmenty}, K_{thr}(i), H_{thr}(i))$
        3.  Detekcja Ψᴺ w iteracji $i$: $\text{Ψᴺ_wykryte}(i) = \text{DetekcjaSłówKluczowych}(\text{Fragmenty})$
        4.  Adaptacja progów (uproszczona reguła z kodu `meta_feedback_loop`):
            * Jeśli $\frac{\text{liczba}(\text{Ψʰ})}{\text{liczba}(\text{Fragmenty})} > 0.5$, wtedy:
                $K_{thr}(i+1) = \min(K_{thr}(i) + 0.05, 1.0)$
                $H_{thr}(i+1) = \max(H_{thr}(i) - 0.05, 0.0)$

        **Wyjaśnienie:**
        Meta-pętla sprzężenia zwrotnego (`meta_feedback_loop`) jest sercem dynamicznej adaptacji GTMØ. W każdej iteracji pętla przetwarza zbiór fragmentów, klasyfikuje je używając bieżących progów, a następnie na podstawie wyników tej klasyfikacji (np. proporcji różnych typów cząstek) oraz detekcji nowych typów Ψᴺ, modyfikuje progi na potrzeby kolejnej iteracji. Celem jest dostrojenie systemu do charakterystyki przetwarzanych danych, co prowadzi do efektywniejszego zarządzania nieokreślonością i lepszego oddzielenia sygnału od szumu, zgodnie z TH9.
        """,
        # Explanation OT2 EN
        """
        --- Explanation (EN) ---
        **Key Definitions:**
        * **Dynamic thresholds $K_{thr}, H_{thr}$**: As defined in OT1.
        * **Ψᴺ (Novel/Emergent Particle)**: An information fragment (e.g., containing a paradox, contradiction, meta-information) indicating potential novelty or exceeding the system's current framework. In the code, detection is keyword-based: `if "paradoks" in frag.lower() or ... new_types_detected.add("Ψᴺ (novel/emergent)")`.
        * `TH9`: "GTMØ minimizes cognitive noise and adapts the boundary of sense through iterative self-evaluation of thresholds."

        **Basic Equations/Processes:**
        1.  Threshold calculation in iteration $i$: $K_{thr}(i), H_{thr}(i) = \text{dynamic_thresholds}(\text{scores}(i))$
        2.  Fragment classification in iteration $i$: $\text{Types}(i) = \text{Classify}(\text{Fragments}, K_{thr}(i), H_{thr}(i))$
        3.  Ψᴺ detection in iteration $i$: $\text{Ψᴺ_detected}(i) = \text{KeywordDetection}(\text{Fragments})$
        4.  Threshold adaptation (simplified rule from `meta_feedback_loop` code):
            * If $\frac{\text{count}(\text{Ψʰ})}{\text{count}(\text{Fragments})} > 0.5$, then:
                $K_{thr}(i+1) = \min(K_{thr}(i) + 0.05, 1.0)$
                $H_{thr}(i+1) = \max(H_{thr}(i) - 0.05, 0.0)$

        **Explanation:**
        The meta-feedback loop (`meta_feedback_loop`) is the heart of GTMØ's dynamic adaptation. In each iteration, the loop processes a set of fragments, classifies them using current thresholds, and then, based on the results of this classification (e.g., the proportion of different particle types) and the detection of new Ψᴺ types, it modifies the thresholds for the next iteration. The goal is to tune the system to the characteristics of the processed data, leading to more effective management of indefiniteness and better separation of signal from noise, in accordance with TH9.
        """
    ),
    (
        # OT3 PL
        "Twierdzenie Operacyjne 3 (Operator Oceny Ψ_GTMØ): Operator Ψ_GTMØ przypisuje każdemu fragmentowi informacji ocenę (score) i typ (Ψᴷ, Ψʰ, Ψᴺ). W przypadku operacji na symbolu nieokreśloności Ø, operator musi działać w trybie META, zwracając predefiniowany stan osobliwości, co jest niemożliwe dla operatorów działających w trybie STANDARDOWYM.",
        # OT3 EN
        "Operational Theorem 3 (Ψ_GTMØ Evaluation Operator): The Ψ_GTMØ operator assigns each information fragment a score and a type (Ψᴷ, Ψʰ, Ψᴺ). When operating on the indefiniteness symbol Ø, the operator must function in META mode, returning a predefined singularity state, which is impossible for operators functioning in STANDARD mode.",
        # Objaśnienie OT3 PL
        """
        --- Objaśnienie (PL) ---
        **Definicje Kluczowe:**
        * `AX9_v2`: "Operator irreducibility (strict): ¬∃Op ∈ StandardOperators: Op(Ø) = x, x ∈ Domain(GTMØ)"
        * `AX10`: "Meta-operator definition: Ψ_GTMØ, E_GTMØ are meta-operators acting on Ø"
        * `Operator.STANDARD`, `Operator.META`: Typy operatorów zdefiniowane w klasie `Operator`.
        * `Ø`: Symbol fundamentalnej nieokreśloności.

        **Równania/Logika Operacyjna (z funkcji `Ψ_GTMØ`):**
        1.  Jeśli argument $x = \text{"Ø"}$:
            * Jeśli `operator_type == Operator.META`:
                Wynik: `{'score': 1.0, 'type': "Ø (singularity)"}`
            * Jeśli `operator_type == Operator.STANDARD`:
                Wynik: `ValueError("Standard operators cannot process Ø")` (zgodnie z AX9_v2)
        2.  Jeśli argument $x \ne \text{"Ø"}$:
            * $s(x) = \text{random.uniform}(0, 1)$ (w uproszczonej implementacji)
            * Typ $T(x)$ jest określany na podstawie $s(x)$ i progów $K_{thr}, H_{thr}$.
            * Wynik: `{'score': s(x), 'type': T(x), ...}`

        **Wyjaśnienie:**
        To twierdzenie operacyjne opisuje dwoistą naturę kluczowego operatora $\text{Ψ_GTMØ}$. Dla standardowych fragmentów wiedzy, operator ten generuje ocenę (score) i klasyfikuje je (jako Ψᴷ, Ψʰ, lub inne Ψᴧ). Jednakże symbol Ø, reprezentujący fundamentalną nieokreśloność, nie może być przetwarzany przez standardowe mechanizmy (zgodnie z AX9_v2). Dlatego $\text{Ψ_GTMØ}$ musi działać jako meta-operator (zgodnie z AX10), aby móc rozpoznać Ø i przypisać mu specjalny status "osobliwości", zamiast próbować go oceniać w konwencjonalny sposób. To rozróżnienie jest kluczowe dla spójności GTMØ.
        """,
        # Explanation OT3 EN
        """
        --- Explanation (EN) ---
        **Key Definitions:**
        * `AX9_v2`: "Operator irreducibility (strict): ¬∃Op ∈ StandardOperators: Op(Ø) = x, x ∈ Domain(GTMØ)"
        * `AX10`: "Meta-operator definition: Ψ_GTMØ, E_GTMØ are meta-operators acting on Ø"
        * `Operator.STANDARD`, `Operator.META`: Operator types defined in the `Operator` class.
        * `Ø`: Symbol of fundamental indefiniteness.

        **Basic Equations/Operational Logic (from `Ψ_GTMØ` function):**
        1.  If argument $x = \text{"Ø"}$:
            * If `operator_type == Operator.META`:
                Result: `{'score': 1.0, 'type': "Ø (singularity)"}`
            * If `operator_type == Operator.STANDARD`:
                Result: `ValueError("Standard operators cannot process Ø")` (consistent with AX9_v2)
        2.  If argument $x \ne \text{"Ø"}$:
            * $s(x) = \text{random.uniform}(0, 1)$ (in the simplified implementation)
            * Type $T(x)$ is determined based on $s(x)$ and thresholds $K_{thr}, H_{thr}$.
            * Result: `{'score': s(x), 'type': T(x), ...}`

        **Explanation:**
        This operational theorem describes the dual nature of the key $\text{Ψ_GTMØ}$ operator. For standard knowledge fragments, this operator generates a score and classifies them (as Ψᴷ, Ψʰ, or other Ψᴧ). However, the symbol Ø, representing fundamental indefiniteness, cannot be processed by standard mechanisms (as per AX9_v2). Therefore, $\text{Ψ_GTMØ}$ must act as a meta-operator (as per AX10) to recognize Ø and assign it a special "singularity" status, rather than attempting to evaluate it conventionally. This distinction is crucial for GTMØ's consistency.
        """
    ),
    (
        # OT4 PL
        "Twierdzenie Operacyjne 4 (Minimalizacja Entropii Poznawczej): System GTMØ, poprzez działanie pętli sprzężenia zwrotnego i adaptacyjne dostosowywanie progów, operacyjnie dąży do minimalizacji globalnej entropii poznawczej (E_GTMØ), faworyzując przetwarzanie fragmentów o wysokiej określoności (Ψᴷ) i efektywne zarządzanie regionami wysokiej nieokreśloności (Ψʰ oraz Ø).",
        # OT4 EN
        "Operational Theorem 4 (Cognitive Entropy Minimization): The GTMØ system, through the operation of its feedback loop and adaptive threshold adjustments, operationally strives to minimize global cognitive entropy (E_GTMØ), favoring the processing of high-definiteness fragments (Ψᴷ) and effectively managing regions of high indefiniteness (Ψʰ and Ø).",
        # Objaśnienie OT4 PL
        """
        --- Objaśnienie (PL) ---
        **Definicje Kluczowe:**
        * `DEF3_pl`: "Definicja: Entropia poznawcza $E_{GTMØ}(x) = -\sum p_i \log_2 p_i$, $p_i$ – podziały semantyczne $x$."
        * `AX6`: "Heuristic extremum: $E_{GTMØ}(Ø) = \min E_{GTMØ}(x)$, $x \in \text{KnowledgeDomain}$" (Ø ma minimalną entropię).
        * `TH6`: "For any knowledge particle Ψᴷ, ... $E_{GTMØ}(Ψᴷ) \ll E_{GTMØ}(Ψʰ)$" (Ψᴷ ma znacznie niższą entropię niż Ψʰ).
        * `TH7`: "For any knowledge shadow Ψʰ, ... $E_{GTMØ}(Ψʰ) \gg E_{GTMØ}(Ψᴷ)$" (Ψʰ ma znacznie wyższą entropię niż Ψᴷ).

        **Równania Podstawowe:**
        1.  Wzór na entropię poznawczą: $E_{GTMØ}(x) = -\sum_{i} p_i(x) \log_2 p_i(x)$
            * Gdzie $p_i(x)$ to prawdopodobieństwo $i$-tego podziału semantycznego fragmentu $x$. W implementacji `E_GTMØ(x)` użyto stałej, przykładowej partycji.
        2.  Cel operacyjny: Dążenie do stanu, w którym średnia ważona entropia przetwarzanych fragmentów jest minimalizowana, lub w którym fragmenty Ψᴷ dominują.

        **Wyjaśnienie:**
        To twierdzenie operacyjne wskazuje na jeden z głównych celów GTMØ: zarządzanie i potencjalną minimalizację nieokreśloności w systemie, co jest kwantyfikowane za pomocą entropii poznawczej. Zgodnie z definicjami i twierdzeniami, cząstki wiedzy Ψᴷ charakteryzują się niską entropią, cienie wiedzy Ψʰ wysoką, a sama nieokreśloność Ø reprezentuje absolutne minimum entropii (AX6). Działania systemu, takie jak adaptacja progów w `meta_feedback_loop`, mają na celu takie skonfigurowanie percepcji systemu, aby efektywnie identyfikować i promować Ψᴷ, jednocześnie odpowiednio zarządzając (np. izolując lub badając) Ψʰ i Ø.
        """,
        # Explanation OT4 EN
        """
        --- Explanation (EN) ---
        **Key Definitions:**
        * `DEF3`: "Definition: Cognitive entropy $E_{GTMØ}(x) = -\sum p_i \log_2 p_i$, where $p_i$ are semantic partitions of $x$."
        * `AX6`: "Heuristic extremum: $E_{GTMØ}(Ø) = \min E_{GTMØ}(x)$, $x \in \text{KnowledgeDomain}$" (Ø has minimal entropy).
        * `TH6`: "For any knowledge particle Ψᴷ, ... $E_{GTMØ}(Ψᴷ) \ll E_{GTMØ}(Ψʰ)$" (Ψᴷ has significantly lower entropy than Ψʰ).
        * `TH7`: "For any knowledge shadow Ψʰ, ... $E_{GTMØ}(Ψʰ) \gg E_{GTMØ}(Ψᴷ)$" (Ψʰ has significantly higher entropy than Ψᴷ).

        **Basic Equations:**
        1.  Cognitive Entropy Formula: $E_{GTMØ}(x) = -\sum_{i} p_i(x) \log_2 p_i(x)$
            * Where $p_i(x)$ is the probability of the $i$-th semantic partition of fragment $x$. The `E_GTMØ(x)` implementation uses a fixed, dummy partition.
        2.  Operational Goal: Striving for a state where the weighted average entropy of processed fragments is minimized, or where Ψᴷ fragments dominate.

        **Explanation:**
        This operational theorem points to one of GTMØ's main goals: managing and potentially minimizing indefiniteness within the system, quantified by cognitive entropy. According to definitions and theorems, knowledge particles Ψᴷ are characterized by low entropy, knowledge shadows Ψʰ by high entropy, and indefiniteness Ø itself represents the absolute minimum of entropy (AX6). System operations, such as threshold adaptation in the `meta_feedback_loop`, aim to configure the system's perception to effectively identify and promote Ψᴷ, while appropriately managing (e.g., isolating or investigating) Ψʰ and Ø.
        """
    ),
    (
        # OT5 PL
        "Twierdzenie Operacyjne 5 (Obsługa Emergencji Ψᴺ): Wykrycie przez system GTMØ cząstek emergentnych (Ψᴺ), typowo na podstawie identyfikacji sprzeczności, paradoksów, autoreferencji lub nieklasyfikowalnych nowości, sygnalizuje przekroczenie bieżących zdolności adaptacyjnych systemu i uruchamia procedury mające na celu ewolucję bazy wiedzy lub modyfikację heurystyk GTMØ.",
        # OT5 EN
        "Operational Theorem 5 (Handling Emergence Ψᴺ): The detection by the GTMØ system of emergent particles (Ψᴺ), typically based on identifying contradictions, paradoxes, self-references, or unclassifiable novelties, signals that the system's current adaptive capabilities have been exceeded and initiates procedures aimed at evolving the knowledge base or modifying GTMØ heuristics.",
        # Objaśnienie OT5 PL
        """
        --- Objaśnienie (PL) ---
        **Definicje Kluczowe:**
        * **Ψᴺ (Cząstka Nowa/Emergentna)**: Koncepcyjnie zdefiniowana jako fragment wskazujący na nowość, nieoczekiwane własności lub ograniczenia systemu (np. w `README.md`).
        * W implementacji `meta_feedback_loop` detekcja Ψᴺ opiera się na prostych regułach tekstowych:
            `if "paradoks" in frag.lower() or "sprzeczność" in frag.lower() or "meta-" in frag.lower(): new_types_detected.add("Ψᴺ (novel/emergent)")`

        **Równania/Logika Operacyjna:**
        1.  Reguła detekcji Ψᴺ: $\text{JestΨᴺ}(f) \leftarrow \exists k \in K_{emerg} : k \subseteq \text{treść}(f)$
            * Gdzie $f$ to fragment, $K_{emerg}$ to zbiór słów kluczowych wskazujących na emergencję (np. {"paradoks", "sprzeczność", "meta-"}).
        2.  Konsekwencja operacyjna: Wykrycie Ψᴺ $\rightarrow$ Sygnał_Ewolucji_Systemu
            * Może to oznaczać np. zmianę strategii adaptacji progów, dodanie nowych reguł, lub alert dla użytkownika/operatora systemu.

        **Wyjaśnienie:**
        GTMØ ma za zadanie nie tylko przetwarzać znaną informację, ale również identyfikować momenty, gdy napotyka na coś fundamentalnie nowego lub problematycznego (Ψᴺ). Obecna implementacja wykorzystuje prostą heurystykę opartą na słowach kluczowych do detekcji takich fragmentów. Twierdzenie to postuluje, że operacyjnym skutkiem wykrycia Ψᴺ jest nie tylko jego etykietowanie, ale przede wszystkim uruchomienie w systemie GTMØ procesów adaptacyjnych wyższego rzędu. Może to obejmować modyfikację jego wewnętrznych modeli, heurystyk, a nawet celów, aby zasymilować nową informację lub rozwiązać wykryty problem. Jest to kluczowy mechanizm długoterminowej ewolucji i uczenia się systemu.
        """,
        # Explanation OT5 EN
        """
        --- Explanation (EN) ---
        **Key Definitions:**
        * **Ψᴺ (Novel/Emergent Particle)**: Conceptually defined as a fragment indicating novelty, unexpected properties, or system limitations (e.g., in `README.md`).
        * In the `meta_feedback_loop` implementation, Ψᴺ detection is based on simple text rules:
            `if "paradoks" in frag.lower() or "sprzeczność" in frag.lower() or "meta-" in frag.lower(): new_types_detected.add("Ψᴺ (novel/emergent)")`

        **Basic Equations/Operational Logic:**
        1.  Ψᴺ Detection Rule: $\text{IsΨᴺ}(f) \leftarrow \exists k \in K_{emerg} : k \subseteq \text{content}(f)$
            * Where $f$ is a fragment, $K_{emerg}$ is a set of keywords indicating emergence (e.g., {"paradox", "contradiction", "meta-"}).
        2.  Operational Consequence: Detection of Ψᴺ $\rightarrow$ System_Evolution_Signal
            * This might involve changing threshold adaptation strategies, adding new rules, or alerting a user/system operator.

        **Explanation:**
        GTMØ is designed not only to process known information but also to identify moments when it encounters something fundamentally new or problematic (Ψᴺ). The current implementation uses a simple keyword-based heuristic to detect such fragments. This theorem posits that the operational consequence of detecting Ψᴺ is not just its labeling, but primarily the initiation of higher-order adaptive processes within the GTMØ system. This may include modifying its internal models, heuristics, or even its goals to assimilate the new information or resolve the detected issue. This is a key mechanism for the system's long-term evolution and learning.
        """
    ),
    (
        # OT6 PL
        "Twierdzenie Operacyjne 6 (Topologiczna Interpretacja Emergencji z Ø): W modelu topologicznym GTMØ, stany systemu φ(t) znajdujące się w bezpośrednim, zdefiniowanym przez heurystykę E(x) otoczeniu osobliwości Ø, są traktowane jako punkty krytyczne. Przejście systemu przez taki punkt może operacyjnie inicjować proces emergencji (`trigger_emergence`), prowadzący do powstawania nowych cząstek wiedzy (Ψᴷ) lub struktur informacyjnych.",
        # OT6 EN
        "Operational Theorem 6 (Topological Interpretation of Emergence from Ø): In the GTMØ topological model, system states φ(t) located in the immediate vicinity of the Ø singularity, as defined by the E(x) heuristic, are treated as critical points. The system's transition through such a point can operationally initiate an emergence process (`trigger_emergence`), leading to the formation of new knowledge particles (Ψᴷ) or informational structures.",
        # Objaśnienie OT6 PL
        """
        --- Objaśnienie (PL) (w kontekście kodu `topologia.py`) ---
        **Definicje Kluczowe:**
        * **φ(t)**: Funkcja trajektorii poznawczej, mapująca parametr $t$ na stany systemu (np. $0, 1, \infty, \text{Ø_value}$).
        * **Ø_value**: Numeryczna reprezentacja osobliwości Ø (np. `999`).
        * **E(x, Ø_value)**: Heurystyka bliskości do Ø_value.
        * **Próg bliskości (closeness_threshold)**: Wartość, powyżej której $E(x, \text{Ø_value})$ wskazuje na "bliskość" do Ø.

        **Równania/Logika Operacyjna:**
        1.  Heurystyka bliskości: $E(x, \text{Ø_value}) = e^{-|x - \text{Ø_value}|}$
        2.  Warunek stanu krytycznego (bliskości Ø): $E(\phi(t), \text{Ø_value}) \ge \text{closeness_threshold}$
        3.  Proces emergencji: Jeśli warunek (2) jest spełniony, wywoływana jest funkcja `trigger_emergence(t, φ(t))`.
            * `trigger_emergence` $\rightarrow$ $\text{log_new_particle}(\text{ID_cząstki}, t, \phi(t))$

        **Wyjaśnienie:**
        To twierdzenie operacyjne łączy koncepcję topologiczną (opisaną w osobnym module `topologia.py`) z mechanizmem powstawania nowej wiedzy. Zakłada, że gdy trajektoria poznawcza systemu $\phi(t)$ zbliża się do punktu reprezentującego nieokreśloność Ø (co jest mierzone przez wysoką wartość heurystyki $E(x)$), system osiąga stan krytyczny. W tym stanie, GTMØ operacyjnie uruchamia procedurę (`trigger_emergence`), która symbolizuje "narodziny" nowej cząstki wiedzy lub struktury. Jest to manifestacja założenia, że Ø nie jest tylko pustką, ale aktywną przestrzenią, z której może wyłonić się nowa określoność.
        """,
        # Explanation OT6 EN
        """
        --- Explanation (EN) (in the context of the `topologia.py` code) ---
        **Key Definitions:**
        * **φ(t)**: Cognitive trajectory function, mapping parameter $t$ to system states (e.g., $0, 1, \infty, \text{Ø_value}$).
        * **Ø_value**: Numerical representation of the Ø singularity (e.g., `999`).
        * **E(x, Ø_value)**: Heuristic for closeness to Ø_value.
        * **Closeness Threshold**: A value above which $E(x, \text{Ø_value})$ indicates "closeness" to Ø.

        **Basic Equations/Operational Logic:**
        1.  Closeness Heuristic: $E(x, \text{Ø_value}) = e^{-|x - \text{Ø_value}|}$
        2.  Critical State Condition (nearness to Ø): $E(\phi(t), \text{Ø_value}) \ge \text{closeness_threshold}$
        3.  Emergence Process: If condition (2) is met, the `trigger_emergence(t, φ(t))` function is called.
            * `trigger_emergence` $\rightarrow$ $\text{log_new_particle}(\text{particle_ID}, t, \phi(t))$

        **Explanation:**
        This operational theorem links the topological concept (described in the separate `topologia.py` module) with the mechanism of new knowledge formation. It posits that when the system's cognitive trajectory $\phi(t)$ approaches the point representing indefiniteness Ø (as measured by a high value of the $E(x)$ heuristic), the system reaches a critical state. In this state, GTMØ operationally invokes a procedure (`trigger_emergence`) that symbolizes the "birth" of a new knowledge particle or structure. This is a manifestation of the assumption that Ø is not merely a void but an active space from which new definiteness can emerge.
        """
    )
]
