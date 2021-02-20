import Data.List




data Color = White | Yellow | Orange | Red | Green | Blue
data Piece = Up | Down | Left | Right | Front | Back -- только для наглядности
           | UpFL | UpFR | UpBL | UpBR | DownFL | DownFR | DownBL | DownBR
           | LeftFU | LeftFD | LeftBU | LeftBD | RightFU | RightFD | RightBU | RightBD
           | FrontUL | FrontUR | FrontDL | FrontDR | BackUL | BackUR | BackDL | BackDR

record Cube where
    constructor MkCube
    stickers : List Color
    pieces : List Piece
    groups : List ( -- список возможных поворотов
                   List ( -- список групп перемещений наклеек
                         List Piece)) -- группа перемещений наклеек
    blocks : List (List Piece)

                         
cube1x1x1 : Cube
cube1x1x1 = MkCube [White, Yellow, Orange, Red, Green, Blue]
                   [Up, Down, Left, Right, Front, Back]
                   [ [ [Up, Back, Down, Front] ], -- x
                     [ [Up, Right, Down, Left] ], -- y
                     [ [Front, Right, Back, Left] ] ] -- z
                   []
                     
cube2x2x2 : Cube
cube2x2x2 = MkCube [White, White, White, White, Yellow, Yellow, Yellow, Yellow,
                    Orange, Orange, Orange, Orange, Red, Red, Red, Red,
                    Green, Green, Green, Green, Blue, Blue, Blue, Blue]
                   [UpFL, UpFR, UpBL, UpBR, DownFL, DownFR, DownBL, DownBR,
                    LeftFU, LeftFD, LeftBU, LeftBD, RightFU, RightFD, RightBU, RightBD,
                    FrontUL, FrontUR, FrontDL, FrontDR, BackUL, BackUR, BackDL, BackDR]
                   [ [ [UpFL, BackUL, DownBL, FrontDL],
                       [UpFR, BackUR, DownBR, FrontDR],
                       [UpBL, BackDL, DownFL, FrontUL],
                       [UpBR, BackDR, DownFR, FrontUR],
                       [LeftFU, LeftBU, LeftBD, LeftFD],
                       [RightFU, RightBU, RightBD, RightFD] ], -- x
                     [ [UpFL, RightFU, DownFR, LeftFD],
                       [UpFR, RightFD, DownFL, LeftFU],
                       [UpBL, RightBU, DownBR, LeftBD],
                       [UpBR, RightBD, DownBL, LeftBU],
                       [FrontUL, FrontUR, FrontDR, FrontDL],
                       [BackUL, BackUR, BackDR, BackDL] ], -- y
                     [ [UpFL, BackUL, DownBL, FrontDL],
                       [UpBL, BackDL, DownFL, FrontUL],
                       [LeftFU, LeftBU, LeftBD, LeftFD] ] ] -- L
                   []
                       
cube1x2x2 : Cube
cube1x2x2 = ?hole122
-- cube1x2x2 = record {blocks = []} cube2x2x2
    
    


toNat : Piece -> Nat
toNat Up = 0
toNat Down = 1
toNat Left = 2
toNat Right = 3
toNat Front = 4
toNat Back = 5
toNat UpFL = 0 -- zn as indexation list
toNat UpFR = 1
toNat UpBL = 2
toNat UpBR = 3
toNat DownFL = 4
toNat DownFR = 5
toNat DownBL = 6
toNat DownBR = 7
toNat LeftFU = 8
toNat LeftFD = 9
toNat LeftBU = 10
toNat LeftBD = 11
toNat RightFU = 12
toNat RightFD = 13
toNat RightBU = 14
toNat RightBD = 15
toNat FrontUL = 16
toNat FrontUR = 17
toNat FrontDL = 18
toNat FrontDR = 19
toNat BackUL = 20
toNat BackUR = 21
toNat BackDL = 22
toNat BackDR = 23
    
Cast Piece Nat where
    cast piece = toNat piece
    
Eq Piece where
    x == y = (toNat x) == (toNat y)

Cast (List Piece) (List Nat) where
    cast [] = []
    cast (x :: xs) = cast x :: cast xs
    
Cast (List (List Piece)) (List (List Nat)) where
    cast [] = []
    cast (x :: xs) = cast x :: cast xs
    
Eq (Nat, Color) where
    (n1,_) == (n2,_) = n1 == n2

Ord (Nat, Color) where
    compare (n1,_) (n2,_) = compare n1 n2
    
Show Color where
    show White = "White"
    show Yellow = "Yellow"
    show Orange = "Orange"
    show Red = "Red"
    show Green = "Green"
    show Blue = "Blue"
    
Show Cube where
    show cube = show (stickers cube)


rotate : Nat -> Cube -> Maybe Cube
rotate n cube = 
    let group = indexT n (groups cube) in
        case checkBlocked group (blocks cube) of
            True => Nothing
            False => Just (record {stickers = multiperm (cast group) (stickers cube)} cube) where
        
    -- TODO stdlib
    indexT : Nat -> List (List a) -> List a
    indexT _ [] = []
    indexT Z (x :: xs) = x
    indexT (S k) (_ :: xs) = indexT k xs
        
    checkBlocked : List (List Piece) -> List (List Piece) -> Bool
    checkBlocked xs ys = alienElem (flat xs) (flat ys) where
        
        -- TODO stdlib
        flat : List (List a) -> List a
        flat [] = []
        flat ([] :: xxs) = flat xxs
        flat (l@(x :: xs) :: xxs) = l ++ flat xxs 
        
        -- TODO stdlib
        isElem : Eq a => a -> List a -> Bool
        isElem _ [] = False
        isElem x (y :: ys) =
            if x == y
                then True
                else isElem x ys
                
        alienElem : Eq a => (checked : List a) -> (checker : List a) -> Bool
        alienElem [] _ = True -- not alien in first list
        alienElem _ [] = False -- find alien in first list
        alienElem (x :: xs) ys =
            if isElem x ys
                then alienElem xs ys
                else False
        

    multiperm : List (List Nat) -> List Color -> List Color
    multiperm [] xs = xs
    multiperm (i :: is) xs = multiperm is (perm i xs) where

        perm : List Nat -> List Color -> List Color
        perm is xs = new 0 xs . sort . get 0 xs . sort $ zip is (shift is) where
        
            new : (index : Nat) -> (elems : List Color) -> (saved : List (Nat, Color)) -> List Color
            new _ elems [] = elems
            new n (elem :: elems) saved@((i, savedElem) :: saveds) =
                if n == i
                    then savedElem :: new (n+1) elems saveds
                    else elem :: new (n+1) elems saved
            new _ _ _ = []
            
            get : (index : Nat) -> (elems : List Color) -> (indexs : List (Nat, Nat)) -> List (Nat, Color)
            get i (elem :: elems) indexs@((indexFrom, indexDest) :: indexsFromDest) =
                if i == indexFrom
                    then (indexDest, elem) :: get (i + 1) elems indexsFromDest
                    else get (i + 1) elems indexs
            get _ _ _ = []
            
            -- TODO stdlib
            shift : List Nat -> List Nat 
            shift [] = []
            shift (x :: xs) = xs ++ [x]

main : IO ()
main = putStrLn . show . rotate 1 $ cube2x2x2
