---
title: IsoChronology
permalink: /Java/IsoChronology/
date: 2021-01-11
key: Java.I.IsoChronology
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'clase java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.IsoChronology.description }}

## Sintaxis
~~~java
public final class IsoChronology extends AbstractChronology implements Serializable
~~~

## Campos
* [INSTANCE](/Java/IsoChronology/INSTANCE)

## Métodos
* [date()](/Java/IsoChronology/date)
* [dateEpochDay()](/Java/IsoChronology/dateEpochDay)
* [dateNow()](/Java/IsoChronology/dateNow)
* [dateYearDay()](/Java/IsoChronology/dateYearDay)
* [epochSecond()](/Java/IsoChronology/epochSecond)
* [getCalendarType()](/Java/IsoChronology/getCalendarType)
* [getId()](/Java/IsoChronology/getId)
* [isLeapYear()](/Java/IsoChronology/isLeapYear)
* [localDateTime()](/Java/IsoChronology/localDateTime)
* [period()](/Java/IsoChronology/period)
* [resolveDate()](/Java/IsoChronology/resolveDate)
* [zonedDateTime()](/Java/IsoChronology/zonedDateTime)

## Ejemplo
~~~java
{{ site.data.Java.I.IsoChronology.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.I.IsoChronology.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
