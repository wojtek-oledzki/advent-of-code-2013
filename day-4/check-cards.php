#!/usr/bin/php
<?php

$cards_input = file("/app/" . $argv[1]);
$points = [];

foreach ($cards_input as $line) {
    $parts = preg_split("/ ?[|:] ?/", $line);
    $winning_numbers = preg_split("/ +/", trim($parts[1]));
    $elf_numbers = preg_split("/ +/", trim($parts[2]));
    $elfs_winning_numbers = array_intersect($winning_numbers, $elf_numbers);

    if (count($elfs_winning_numbers) == 0) {
        continue;
    }

    $points[] = pow(2, count($elfs_winning_numbers) - 1);
}

$points_sum = array_sum($points);
print "Total points: {$points_sum}\n";
