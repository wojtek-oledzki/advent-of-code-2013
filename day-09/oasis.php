<?php

$input = file($argv[1]);
$size = count($input);
$predictions = [];

for ($i = 0; $i < $size; $i++) {
    $prediction = predictNext(getNumbers(trim($input[$i])));
    $predictions[] = end($prediction);
}

print("sum of all predictions: " . array_sum($predictions) . "\n");

function predictNext($numbers) {
    $count = count($numbers);
    $nextLine = [];
    $allZeros = true;

    // get next line
    for($i = 0; $i < $count-1; $i++) {
        $nextLine[] = $numbers[$i+1] - $numbers[$i];
        $allZeros &= ($numbers[$i+1] - $numbers[$i]) == 0;
    }

    // all done, or do we need one more?
    if ($allZeros) {
        $numbers[] = $numbers[$count-1] + $nextLine[$count-2];
    } else {
        $predictedNextLine = predictNext($nextLine);
        $numbers[] = $numbers[$count-1] + $predictedNextLine[$count-1];
    }

    return $numbers;
}

function getNumbers($string) {
    $numbers = [];
    foreach(explode(" ", trim($string)) as $ns) {
        $numbers[] = intval($ns);
    }

    return $numbers;
}
