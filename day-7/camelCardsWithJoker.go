package main

import (
	"bufio"
	"os"
	"reflect"
	"slices"
	"strconv"
	"strings"
    "flag"
    "fmt"
)

type Card struct {
	Hand string
	Bid  int
	Type int
	Rank int
}

const (
	CARD_TYPE_FIVE_OF_A_KIND  = 7
	CARD_TYPE_FOUR_OF_A_KIND  = 6
	CARD_TYPE_FULL_HOUSE      = 5
	CARD_TYPE_THREE_OF_A_KIND = 4
	CARD_TYPE_TWO_PAIR        = 3
	CARD_TYPE_ONE_PAIR        = 2
	CARD_TYPE_HIGH_CARD       = 1
)

func main() {
	wordPtr := flag.String("input", "input", "path to input file")
	flag.Parse()

	file, err := os.Open(*wordPtr)

	if err != nil {
		fmt.Println("Error finding file %v", err)
		os.Exit(1)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)
	var cards []Card
	for scanner.Scan() {
		cards = append(cards, parseLine(scanner.Text()))
	}

	slices.SortFunc(cards, compareHands)

	// add rank
	rank := 1
	for i := 0; i < len(cards); i++ {
		cards[i].Rank = rank
		rank++
	}

	totalWinning := 0
	for i := 0; i < len(cards); i++ {
		totalWinning += cards[i].Rank * cards[i].Bid
	}

	fmt.Println("total winning", totalWinning)
}

func compareHands(a, b Card) int {
	cardsOrder := map[byte]int{
		0x41: 13,
		0x4b: 12,
		0x51: 11,
		0x54: 9,
		0x39: 8,
		0x38: 7,
		0x37: 6,
		0x36: 5,
		0x35: 4,
		0x34: 3,
		0x33: 2,
		0x32: 1,
		0x4a: 0,
	}

	if a.Type == b.Type {
		if (cardsOrder[a.Hand[0]] == cardsOrder[b.Hand[0]]) {
			if (cardsOrder[a.Hand[1]] == cardsOrder[b.Hand[1]]) {
				if (cardsOrder[a.Hand[2]] == cardsOrder[b.Hand[2]]) {
					if (cardsOrder[a.Hand[3]] == cardsOrder[b.Hand[3]]) {
						return cardsOrder[a.Hand[4]] - cardsOrder[b.Hand[4]]
					}
					return cardsOrder[a.Hand[3]] - cardsOrder[b.Hand[3]]
				}
				return cardsOrder[a.Hand[2]] - cardsOrder[b.Hand[2]]
			}
			return cardsOrder[a.Hand[1]] - cardsOrder[b.Hand[1]]
		}
		return cardsOrder[a.Hand[0]] - cardsOrder[b.Hand[0]]
	}

	return a.Type - b.Type
}

func parseLine(rawLine string) Card {
	line := strings.Split(rawLine, " ")
	hand := line[0]
	bid, err := strconv.Atoi(line[1])
	if err != nil {
		panic(err)
	}

	return NewCard(hand, bid)
}

func NewCard(hand string, bid int) Card {
	card := Card{
		Hand: hand,
		Bid: bid,
	}

	// count cards
	count := map[byte]int{}
	jokers := 0
	for i := 0; i < len(card.Hand); i++ {
		if card.Hand[i] == 0x4a {
			jokers++
			continue
		}
		count[card.Hand[i]]++
	}
	typeSlice := []int{}
	for _, value := range count {
		typeSlice = append(typeSlice, value)
	}
	slices.Sort(typeSlice)

	// decide what to do with jokers
	if jokers == 5 {
		typeSlice = []int{5}
	} else if jokers == 4 { // 1 card
		typeSlice = []int{5}
	} else if jokers == 3 { // 2 cards
		// can I make 5?
		if len(typeSlice) == 1 {
			typeSlice = []int{5}
		} else {
			typeSlice = []int{1, 4}
		}
	} else if jokers == 2 { // 3 cards
		if len(typeSlice) == 3 { // with 3 different cards I can only make "three of a kind"
			typeSlice = []int{1, 1, 3}
		} else if len(typeSlice) == 2 { // with (1, 2) and 2 jokers I can make "four of a kind", "full house" is weaker
			typeSlice = []int{1, 4}
		} else {
			typeSlice = []int{5}
		}
	} else if jokers == 1 {
		if len(typeSlice) == 4 { // with 4 different cards I can only make "one pair"
			typeSlice = []int{1, 1, 1, 2}
		} else if len(typeSlice) == 3 { // with (1, 1, 2) cards I can only make "three of a kind" (two pairs is weaker)
			typeSlice = []int{1, 1, 3}
		} else if len(typeSlice) == 2 { // with (2, 2) cards and 1 jokers I can make "full house"
			if typeSlice[0] == 1 { // (1, 3)
				typeSlice = []int{1, 4}
			} else { // (2, 2)
				typeSlice = []int{2, 3}
			}
		} else {
			typeSlice = []int{5}
		}
	}

	// decide on the type of hand
	if reflect.DeepEqual(typeSlice, []int{5}) {
		card.Type = CARD_TYPE_FIVE_OF_A_KIND
	} else if reflect.DeepEqual(typeSlice, []int{1, 4}) {
		card.Type = CARD_TYPE_FOUR_OF_A_KIND
	} else if reflect.DeepEqual(typeSlice, []int{2, 3}) {
		card.Type = CARD_TYPE_FULL_HOUSE
	} else if reflect.DeepEqual(typeSlice, []int{1, 1, 3}) {
		card.Type = CARD_TYPE_THREE_OF_A_KIND
	} else if reflect.DeepEqual(typeSlice, []int{1, 2, 2}) {
		card.Type = CARD_TYPE_TWO_PAIR
	} else if reflect.DeepEqual(typeSlice, []int{1, 1, 1, 2}) {
		card.Type = CARD_TYPE_ONE_PAIR
	} else if reflect.DeepEqual(typeSlice, []int{1, 1, 1, 1, 1}) {
		card.Type = CARD_TYPE_HIGH_CARD
	}

	return card
}
