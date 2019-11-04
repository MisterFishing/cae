package hello

import (
	"fmt"
	"net/http"
)

func init() {
	http.HandleFunc("/", main)
}

func main(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "<h1 style='text-align: center;'>Hello Go</h1><p style='text-align: center;'>Welcom to Cloud APP World!</p>");
}
