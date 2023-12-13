<?php

$input = file($argv[1]);
$size = count($input);
$predictions = [];

for ($i = 0; $i < $size; $i++) {
    $prediction = predictPrevious(getNumbers(trim($input[$i])));
    $predictions[] = $prediction[0];
}

print("sum of all historical predictions: " . array_sum($predictions) . "\n");

function predictPrevious($numbers) {
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
        array_unshift($numbers, $numbers[0] - $nextLine[0]);
    } else {
        $predictedNextLine = predictPrevious($nextLine);
        array_unshift($numbers, $numbers[0] - $predictedNextLine[0]);
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
