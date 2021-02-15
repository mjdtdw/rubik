data Color = White | Yellow | Orange | Red | Green | Blue | Black

record Cube where
    constructor MkCube
    Up, Down, Left, Right, Front, Back : Color
    
defaultCube : Cube
defaultCube = MkCube White Yellow Orange Red Green Blue

rotateX : Cube -> Cube
rotateX cube = record {Up = Front cube,
                       Down = Back cube,
                       Front = Down cube,
                       Back = Up cube
                      } cube
                      
rotateY : Cube -> Cube
rotateY cube = record {Left = Front cube,
                       Right = Back cube,
                       Front = Right cube,
                       Back = Left cube
                      } cube
                      
rotateZ : Cube -> Cube
rotateZ cube = record {Up = Left cube,
                       Down = Right cube,
                       Left = Down cube,
                       Right = Up cube
                      } cube


main : IO ()
main = putStrLn "ok"
