<?php

$input = file($argv[1]);
$map = [];

$instructions = $input[0];

for ($i = 2; $i < count($input); $i++) {
    $a = substr($input[$i], 0, 3);
    $b = substr($input[$i], 7, 3);
    $c = substr($input[$i], 12, 3);
    $map[$a] = [$b, $c];
}


// walk
$step = $map["AAA"]; //$map[0]; // "AAA" == 0
$endTarget = "ZZZ";
$steps = 0;
$instructionsLength = strlen(trim($instructions));
$finalSize = pow(2, count($map));
while(true) {
    for($i = 0; $i < $instructionsLength; $i++) {
        $nextStep = 0;
        $steps++;

        if ($instructions[$i] == "L") {
            $nextStep = $step[0];
        } else {
            $nextStep = $step[1];
        }
        $step = $map[$nextStep];
    }

    // are we there yet?
    if ($nextStep == $endTarget) {
        break;
    }
    print("not there yet ... next loop\n");
}
var_dump("steps", $steps, "final step", $nextStep);

function stringToNumber($string) {
    $A = ord("A");
    $base = 10;
    $number = 0;
    for ($i = 0; $i < strlen($string); $i++) {
        $number += pow($base, $i) * (ord($string[$i]) - $A);
    }

    return $number;
}
