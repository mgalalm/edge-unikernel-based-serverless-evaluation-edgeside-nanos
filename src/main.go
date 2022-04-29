package main

import (
	"os"
	"github.com/go-redis/redis"
	"time"

)
func main() {
	client := redis.NewClient(&redis.Options{
		Addr: "192.168.178.72:6379",
		Password: "",
		DB: 0,
	})
	time.Sleep(20 * time.Second)

    activaion_id := os.Getenv("IMAGE_NAME")
	msg := make(map[string]interface{})
	msg["message"] = "Hello World from Nanos"
	client.HMSet(activaion_id, msg)
	// os.Exit(0)
}

