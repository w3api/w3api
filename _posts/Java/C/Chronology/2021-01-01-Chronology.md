---
title: Chronology
permalink: /Java/Chronology/
date: 2021-01-11
key: Java.C.Chronology
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.Chronology.description }}

## Sintaxis
~~~java
public interface Chronology extends Comparable<Chronology>
~~~

## Métodos
* [compareTo()](/Java/Chronology/compareTo/)
* [date()](/Java/Chronology/date/)
* [dateEpochDay()](/Java/Chronology/dateEpochDay/)
* [dateNow()](/Java/Chronology/dateNow/)
* [dateYearDay()](/Java/Chronology/dateYearDay/)
* [epochSecond()](/Java/Chronology/epochSecond/)
* [equals()](/Java/Chronology/equals/)
* [eraOf()](/Java/Chronology/eraOf/)
* [eras()](/Java/Chronology/eras/)
* [from()](/Java/Chronology/from/)
* [getAvailableChronologies()](/Java/Chronology/getAvailableChronologies/)
* [getCalendarType()](/Java/Chronology/getCalendarType/)
* [getDisplayName()](/Java/Chronology/getDisplayName/)
* [getId()](/Java/Chronology/getId/)
* [hashCode()](/Java/Chronology/hashCode/)
* [isLeapYear()](/Java/Chronology/isLeapYear/)
* [localDateTime()](/Java/Chronology/localDateTime/)
* [of()](/Java/Chronology/of/)
* [ofLocale()](/Java/Chronology/ofLocale/)
* [period()](/Java/Chronology/period/)
* [prolepticYear()](/Java/Chronology/prolepticYear/)
* [range()](/Java/Chronology/range/)
* [resolveDate()](/Java/Chronology/resolveDate/)
* [toString()](/Java/Chronology/toString/)
* [zonedDateTime()](/Java/Chronology/zonedDateTime/)

## Ejemplo
~~~java
{{ site.data.Java.C.Chronology.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.Chronology.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
