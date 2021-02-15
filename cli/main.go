package main

import (
	"fmt"

	"github.com/apex/log"
	"github.com/spf13/cobra"
)

var (
	rootCmd = &cobra.Command{
		Use:     "supercli",
		Short:   "This is the most powerful CLI in the world!",
		Version: "Super CLI v0.1.0",
	}

	helloSubCmd = &cobra.Command{
		Use:   "hello",
		Short: "Say hello",
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Hello, world!\n")
		},
	}
)

func main() {
	// configure template for version command
	rootCmd.SetVersionTemplate("{{ .Version }}\n")

	// add hello sub-command
	rootCmd.AddCommand(helloSubCmd)

	// execute command
	if err := rootCmd.Execute(); err != nil {
		log.Fatalf(err.Error())
	}
}
