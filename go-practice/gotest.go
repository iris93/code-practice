package main
import "fmt"

func main(){
  fmt.Printf("hello world!")
  numbers := [4]string{"1", "2", "3", "5"}
  for i,x:= range numbers {
     fmt.Printf("%d",i)
     fmt.Printf(x+"\n")
  }
}
