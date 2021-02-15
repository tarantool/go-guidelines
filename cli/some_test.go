package main

import (
	"testing"

	"github.com/tj/assert"
)

func TestTrueIsTrue(t *testing.T) {
	t.Parallel()
	assert := assert.New(t)

	assert.True(true)
}
