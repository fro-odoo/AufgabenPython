# Keys für die Abteilungen
key1, key2, key3, key4 = 'Name', 'Abteilungsleiter', 'Anzahl Mitarbeiter', 'Mitarbeiter'
# Deklarieren der Mitarbeiter und ihrer Attribute
Mitarbeiter1 = {'Vorname': 'Erik', 'Nachname': 'Erdmann', 'Alter': 33}
Mitarbeiter2 = {'Vorname': 'Johannes', 'Nachname': 'Brennecke', 'Alter': 20}
Mitarbeiter3 = {'Vorname': 'Jolina', 'Nachname': 'Schäning', 'Alter': 19}
Mitarbeiter4 = {'Vorname': 'Magdalena', 'Nachname': 'Reinbrecht', 'Alter': 18}
Mitarbeiter5 = {'Vorname': 'Kacpar', 'Nachname': 'Zawislak', 'Alter': 21}
Mitarbeiter6 = {'Vorname': 'Max', 'Nachname': 'Tantow', 'Alter': 22}
Geschäftsführer = {'Vorname': 'Lars', 'Nachname': 'Liffson', 'Alter': 35}
# Zusammenfassen der Mitarbeiter in Listen je nach Abteilung. Ein Mitarbeiter kann in mehereren Abteilungen sein.
PM_Leute = [Mitarbeiter1, Mitarbeiter2]
QS_Leute = [Mitarbeiter2, Mitarbeiter3, Mitarbeiter4]
Entwickler = [Mitarbeiter6, Mitarbeiter5, Mitarbeiter1, Mitarbeiter3]
# Deklarieren der Abteilungen
Projektmanagement = {key1: 'Projektmanagement', key2: Mitarbeiter1, key3: 2, key4: PM_Leute}
Qualitätssicherung = {key1: 'Qualitätssicherung', key2: Mitarbeiter3, key3: 3, key4: QS_Leute}
Entwicklung = {key1: 'Entwicklung', key2: Mitarbeiter6, key3: 4, key4: Entwickler}
# Abteilungen in Liste 
Abteilungen = [Projektmanagement, Qualitätssicherung, Entwicklung]
###########################################################################
# aus allem die Firma zusammenbauen
firma_intero = {'Geschäftsführer': Geschäftsführer, 'Abteilungen': Abteilungen}

"""es wird davon ausgegangen, dass datenstruktur unbekannt ist.
    bekannt ist, dass dict und list vorhanden sind und dass je mitarbeiter 3 key/value paare hat mit 2 strings und ein int
    vorhanden sind"""
def compute_employee_infos(firma_intero, attribut):
    res = {"Abteilungen": [], "Abteilungsleiter": []}
    ### struktur von mitarbeiter dict ist bekannt und darf ausgenutzt werden
    def istMitarbeiter(node):
        return isinstance(node, dict) and len(node) == 3 and len(list(filter(lambda x: isinstance(x, str), node.values()))) == 2 and len(
            list(filter(lambda x: isinstance(x, int), node.values()))) == 1
    def rek_find_mitarbeiter(node, attribut, prev_node=None):
        ### wenn richtiger mitarbeiter gefunden wird -> bestimme abteilung und abteilungsleiter
        if istMitarbeiter(node) and attribut in node.values() and isinstance(prev_node, dict):
            res.update(node)
            ### da meherere abteilungen sowie abteilungsleiter vorhanden sein können -> in zusammengehörender reihenfolge geordnet und kann mit zip() bearbeitet werden
            [res["Abteilungen"].append(elem) for elem in prev_node.values() if isinstance(elem, str) and elem not in res["Abteilungen"]]
            [res["Abteilungsleiter"].append(elem) for elem in prev_node.values() if istMitarbeiter(elem) and elem not in res["Abteilungsleiter"]]
            return node, prev_node
        else:
            if isinstance(node, list):
                [rek_find_mitarbeiter(elem, attribut, prev_node=prev_node) for elem in node]
            elif isinstance(node, dict):
                [rek_find_mitarbeiter(elem, attribut, prev_node=node) for elem in node.values()]
    ### starte rekursive suche nach mitarbeiter
    rek_find_mitarbeiter(firma_intero, attribut)
    ### falls kein mitarbeiter gefunden wurde gebe None aus
    return res if len(res) > 2 else None

print(compute_employee_infos(firma_intero, "Erik"))
'''
Das hier ist übrigens ein Docstring, er wird benutzt für mehrzeilige Kommentare.
AUFGABE: 
Jeder Mitarbeiter hat drei Attribute bzw. Key/Value pairs. Schreibt eine Methode die 
als Parameter firma_intero und eine BELIEBIGE Value eines Mitarbeiters nimmt.
Anhand dieser Value sollen folgende Informationen ausgegeben werden:
1. Vorname, Nachname und Alter der Person
2. Die Abteilung in der sie/er Arbeitet
3. Wer ist sein Abteilungsleiter bzw. ist sie/er selbst der Abteilungsleiter
Wenn ihr das Fertig habt updated ihr das von mir eingetragene Alter um euer wahres Alter.
IHR DÜRFT AUSSCHLIEẞLICH MIT DER VARIABLE "firma_intero" ARBEITEN. DIE ANDEREN KÖNNT 
IHR EUCH ZUM VERSTÄNDNIS ANSEHEN ABER NICHT BENUTZEN!
TIPP: Nutzt Debugging und insbesondere Expressions
'''

liste = [1,6,8,4,]

liste = list(filter(lambda x: x > 5, liste))



