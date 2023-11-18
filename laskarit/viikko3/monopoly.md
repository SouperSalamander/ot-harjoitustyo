```mermaid
 classDiagram
    MonopolyGame "1" -- "2" Dice
    MonopolyGame "1" -- "1" Board
    Board "1" -- "40" Square
    Square "1" -- "1" Square : next
    Square "1" -- "0..8" Piece
    Piece "1" -- "1" Player
    Player "2..8" -- "1" MonopolyGame
    Player "2..8" -- "*" Money
```
