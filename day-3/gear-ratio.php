#!/usr/bin/php
<?php
$inputSchema = file("/app/" . $argv[1]);
$inputRowCount = count($inputSchema);
$foundParts = [];

for($rowNumber = 0; $rowNumber < count($inputSchema); ++$rowNumber) {
    $row = $inputSchema[$rowNumber];
    $foundPotentialPart = false;
    $partStart = 0;
    $partLen = 0;

    // "tokenise" and find numbers
    for ($i = 0; $i < strlen($row); $i++){
        switch (true) {
            case !is_numeric($row[$i]):
                if ($foundPotentialPart) {
                    isPartNumber($rowNumber, $partStart, $partLen);
                }
                $foundPotentialPart = false;
                $partLen = 0;
                $partStart = 0;
                break;
            case is_numeric($row[$i]):
                if (!$foundPotentialPart) {
                    $foundPotentialPart = true;
                    $partStart = $i;
                }
                $partLen++;
                break;
        }
    }
}

$gear_ratios = [];
foreach($foundParts as $potentialGears) {
    if (count($potentialGears) == 2) {
        $gear_ratios[] = $potentialGears[0] * $potentialGears[1];
    }
}

print "sum of all gear ratios: " . array_sum($gear_ratios) . "\n";

function isPartNumber($rowNumber, $start, $len) {
    global $inputSchema, $inputRowCount, $foundParts;
    $rowLength = strlen($inputSchema[$rowNumber]);
    $partNumber = substr($inputSchema[$rowNumber], $start, $len);
    $gears = [];

    $before = max($start-1, 0);
    $after = $start+$len;
    // check before
    if ($start > 0) {
        if (hasGearSymbol($inputSchema[$rowNumber][$before])) {
            $gears[] = "{$rowNumber}-{$before}";
        }
    }

    // check after
    if ($start + $len < $rowLength - 1) {
        if (hasGearSymbol($inputSchema[$rowNumber][$start+$len])) {
            $gears[] = "{$rowNumber}-{$after}";
        }
    }

    $lenPlus = $len + ($start > 0) + 1;
    // check row above
    if ($rowNumber > 0) {
        $rowAbove = $rowNumber - 1;
        $above = substr($inputSchema[$rowAbove], $before, $lenPlus);
        foreach(getGearsPosition($above) as $gearPosition => $isGear) {
            if ($isGear) {
                $pos = $before + $gearPosition;
                $gears[] = "{$rowAbove}-{$pos}";
            }
        }
    }

    // check row bellow
    if ($rowNumber < $inputRowCount - 1) {
        $rowBellow = $rowNumber + 1;
        $bellow = substr($inputSchema[$rowBellow], $before, $lenPlus);
        foreach(getGearsPosition($bellow) as $gearPosition => $isGear) {
            if ($isGear) {
                $pos = $before + $gearPosition;
                $gears[] = "{$rowBellow}-{$pos}";
            }
        }
    }

    // save found number to all adjacent gears unique position
    foreach ($gears as $gear_location) {
        $foundParts[$gear_location][] = $partNumber;
    }
}

function hasGearSymbol($str) {
    return preg_match('/\*/', trim($str));
}

function getGearsPosition($str) {
    $isGear = function($i) {
        return $i == "*";
    };
    return array_map($isGear, str_split($str));
}

?>
