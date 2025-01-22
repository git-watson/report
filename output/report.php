<?php
// Weather Report Data
date_default_timezone_set('America/Vancouver');
$date = 'January 21';
$data['Last Updated'] = 'January 21st, 2025 16:21 PM PST';
$data['Temperature'] = '-8°C';
$data['Wind'] = 'Strong';
$data['Skies'] = 'Overcast';
$data['Visibility'] = 'Unlimited';
$data['24hr Snowfall'] = '0';
$data['7 Day Snowfall'] = '5';
$data['Snow Base'] = '150';

// Output data
foreach ($data as $key => $value) {
    echo "$key: $value\n";
}
