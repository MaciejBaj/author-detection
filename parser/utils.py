#!/usr/bin/env python
# -*- coding: utf-8 -*-


def update_and_return_json(json_object, key, value):
  json_object[key] = value
  return json_object


def common_keys(match, match_with):
  return {x: match[x] for x in match if x in match_with}


stop_list = [
  'a', 'aby', 'ach', 'acz', 'aczkolwiek', 'aj', 'albo', 'ale', 'ależ',

  'ani', 'aż', 'bardziej', 'bardzo', 'bo', 'bowiem', 'by', 'byli',

  'bynajmniej', 'być', 'był', 'była', 'było', 'były', 'będzie',

  'będą', 'cali', 'cała', 'cały', 'ci', 'cię', 'ciebie', 'co', 'CO',

  'cokolwiek', 'coś', 'cóż', 'czasami', 'czasem', 'czemu', 'czy',

  'czyli', 'daleko', 'dla',

  'dlaczego', 'dlatego', 'do', 'dobrze', 'dokąd', 'dość', 'dużo',

  'dwa',

  'dwaj', 'dwie', 'dwoje', 'dziś', 'dzisiaj', 'gdy', 'gdyby', 'gdyż',

  'gdzie', 'gdziekolwiek', 'gdzieś', 'go', 'i', 'ich', 'ile', 'im',

  'inna', 'inne', 'inny', 'innych', 'iż', 'ja', 'ją', 'jak', 'jakaś',

  'jakby', 'jaki', 'jakichś', 'jakie', 'jakiś', 'jakiż', 'jakkolwiek',

  'jako', 'jakoś', 'je', 'jeden', 'jedna', 'jedno', 'jednak',

  'jednakże',

  'jego', 'jej', 'jemu', 'jest', 'jestem', 'jeszcze', 'jeśli',

  'jeżeli',

  'już', 'ją', 'każdy', 'kiedy', 'kilka', 'kimś', 'kto', 'ktokolwiek',

  'ktoś', 'która', 'które', 'którego', 'której', 'który', 'których',

  'którym', 'którzy', 'ku', 'lat', 'lecz', 'lub', 'ma', 'mają',

  'mało',

  'mam', 'mi', 'mimo', 'między', 'mną', 'mnie', 'mogą', 'moi', 'moim',

  'moja', 'moje', 'może', 'możliwe', 'można', 'mój', 'mu', 'musi',

  'my',

  'na', 'nad', 'nam', 'nami', 'nas', 'nasi', 'nasz', 'nasza', 'nasze',

  'naszego', 'naszych', 'natomiast', 'natychmiast', 'nawet', 'nią',

  'nic', 'nich', 'nie', 'niech', 'niego', 'niej', 'niemu', 'nigdy',

  'nikt', 'nim', 'nimi', 'niż', 'no', 'o', 'obok', 'od', 'około',

  'on', 'ona',

  'one', 'oni', 'ono', 'oraz', 'oto', 'owszem', 'pan', 'pana', 'pani',

  'po', 'pod', 'podczas', 'pomimo', 'ponad', 'ponieważ', 'powinien',

  'powinna', 'powinni', 'powinno', 'poza', 'prawie', 'przecież',

  'przed', 'przede', 'przedtem', 'przez', 'przy', 'raz', 'roku',

  'również',

  'sam', 'sama', 'są', 'się', 'skąd', 'sobie', 'sobą', 'sposób',

  'swoje', 'swój', 'swoja', 'ta', 'tak', 'taka', 'taki', 'takie', 'także', 'tam', 'te',

  'tego', 'tej', 'temu', 'ten', 'teraz', 'też', 'to', 'tobą', 'tobie',

  'toteż', 'trzeba', 'tu', 'tutaj', 'twoi', 'twoim', 'twoja', 'twoje',

  'twym', 'twój', 'ty', 'tych', 'tylko', 'tym', 'u', 'w', 'wam',

  'wami',

  'was', 'wasz', 'wasza', 'wasze', 'we', 'według', 'wiele', 'wielu',

  'więc', 'więcej', 'wszyscy', 'wszystkich', 'wszystkie',

  'wszystkim', 'wszystko', 'wtedy', 'wy', 'właśnie', 'z', 'za',

  'zapewne', 'zawsze', 'ze', 'zł', 'znowu', 'znów', 'został', 'żaden',

  'żadna', 'żadne', 'żadnych', 'że', 'żeby', '.', ',', '?', '!', '.', ',', ':', ';', '-', '#', '*', '(', ')', '"'
]
