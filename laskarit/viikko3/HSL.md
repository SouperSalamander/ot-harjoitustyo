```mermaid
 sequenceDiagram
    Main ->> rautatietori: Lataajalaite()
    Main ->> laitehallinto: lisaa_lataaja(rautatietori)
    Main ->> ratikka6: Lukijalaite()
    Main ->> laitehallinto: lisaa_lukija(ratikka6)
    Main ->> bussi244: Lukijalaite()
    Main ->> laitehallinto: lisaa_lukija(bussi244)
```
