import Data.List




data Color = White | Yellow | Orange | Red | Green | Blue | Black

data Piece = Up | Down | Left | Right | Front | Back 

record Cube where
    constructor MkCube
    stickers : List Color
    pieces : List Piece
    groups : List (List Piece)
    
cube1x1x1 : Cube
cube1x1x1 = MkCube [White, Yellow, Orange, Red, Green, Blue]
                   [Up, Down, Left, Right, Front, Back]
                   [ [Up, Back, Down, Front],
                     [Up, Right, Down, Left],
                     [Front, Right, Back, Left] ]
    
    
    
    
-- TODO proof
indexT : Nat -> List (List a) -> List a
indexT _ [] = []
indexT Z (x :: xs) = x
indexT (S k) (_ :: xs) = indexT k xs

-- TODO deriving
Cast Piece Nat where
    cast Up = 0
    cast Down = 1
    cast Left = 2
    cast Right = 3
    cast Front = 4
    cast Back = 5
    
Cast (List Piece) (List Nat) where
    cast [] = []
    cast (p :: ps) = cast p :: cast ps
    
Eq (Nat, a) where
    (n1,_) == (n2,_) = n1 == n2

Ord (Nat, a) where
    compare (n1,_) (n2,_) = compare n1 n2
    
Show Color where
    show White = "White"
    show Yellow = "Yellow"
    show Orange = "Orange"
    show Red = "Red"
    show Green = "Green"
    show Blue = "Blue"
    show Black = "Black"
    
Show Cube where
    show cube = show (stickers cube)
    
next : Nat -> List Nat -> Maybe Nat
next n [] = Nothing
next n y@(x :: xs) = next' n (y ++ [x]) where
    next' : Nat -> List Nat -> Maybe Nat
    next' n [] = Nothing
    next' n [x] = Nothing 
    next' n (x1 :: x2 :: xs) = if n == x1 then Just x2
                                          else next' n (x2 :: xs)
    
unify : List Nat -> List Nat -> List Nat
unify [] [] = []
unify [] ys = []
unify xs [] = xs
unify (x :: xs) ys =  
    case next x ys of
        Nothing => x :: unify xs ys
        Just a => a :: unify xs ys

unzipT : List (a, b) -> List b
unzipT [] = []
unzipT ((_,b) :: xs) = b :: unzipT xs
    
permutate : Nat -> List a -> List Nat -> List Nat -> List a
permutate n elems sorted nexted = 
    let perm = unify sorted nexted
     in unzipT (sort (zip perm elems))
    
rotate : Nat -> Cube -> Cube
rotate n cube = record {stickers = rotate' n (stickers cube) (pieces cube) (groups cube)} cube where
    rotate' : Nat -> List Color -> List Piece -> List (List Piece) -> List Color
    rotate' n stickers pieces groups = 
        let group = indexT n groups
         in permutate n stickers (cast pieces) (cast group)

main : IO ()
main = putStrLn (show (rotate 0 cube1x1x1))
