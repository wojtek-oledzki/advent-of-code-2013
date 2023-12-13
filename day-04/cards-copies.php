#!/usr/bin/php
<?php

$original_cards = file("/app/" . $argv[1]);;
$original_cards_count = count($original_cards);
$processed_cards = [];

// initial pass - get card numbers and count of winning numbers
foreach ($original_cards as $line) {
    $parts = preg_split("/ ?[|:] ?/", $line);

    $card_number = preg_split("/ +/", trim($parts[0]))[1];
    $winning_numbers = preg_split("/ +/", trim($parts[1]));
    $elf_numbers = preg_split("/ +/", trim($parts[2]));
    $elfs_winning_numbers = array_intersect($winning_numbers, $elf_numbers);

    $processed_cards[] = count($elfs_winning_numbers);
}

// make "pointers"
$add_one = function($value) {
    return $value +1;
};
$cards = array_map($add_one, array_keys($original_cards));

// expand!
for ($i = 0; $i < count($cards); $i++) {
    $card_number = $cards[$i];
    $elfs_winning_number_count = $processed_cards[$card_number - 1];

    if ($elfs_winning_number_count == 0) {
        continue;
    }

    for ($j = $card_number; $j < min($card_number + $elfs_winning_number_count, $original_cards_count); $j++) {
        $cards[] = $j+1;
    }
}

$total_cards = count($cards);
print "Total cards: {$total_cards}\n";
