---
title: DayOfWeek
permalink: Java/DayOfWeek
date: 2021-01-04
key: JavaJava.D.DayOfWeek
category: java
tags: ['java se', 'java.time', 'java.base', 'enumerado java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DayOfWeek.description }}

## Sintaxis
~~~java
public enum DayOfWeek extends Enum<DayOfWeek> implements TemporalAccessor, TemporalAdjuster
~~~

## Enumerados
* [FRIDAY](/Java/DayOfWeek/FRIDAY)
* [MONDAY](/Java/DayOfWeek/MONDAY)
* [SATURDAY](/Java/DayOfWeek/SATURDAY)
* [SUNDAY](/Java/DayOfWeek/SUNDAY)
* [THURSDAY](/Java/DayOfWeek/THURSDAY)
* [TUESDAY](/Java/DayOfWeek/TUESDAY)
* [WEDNESDAY](/Java/DayOfWeek/WEDNESDAY)

## Métodos
* [adjustInto()](/Java/DayOfWeek/adjustInto)
* [from()](/Java/DayOfWeek/from)
* [get()](/Java/DayOfWeek/get)
* [getDisplayName()](/Java/DayOfWeek/getDisplayName)
* [getLong()](/Java/DayOfWeek/getLong)
* [getValue()](/Java/DayOfWeek/getValue)
* [isSupported()](/Java/DayOfWeek/isSupported)
* [minus()](/Java/DayOfWeek/minus)
* [of()](/Java/DayOfWeek/of)
* [plus()](/Java/DayOfWeek/plus)
* [query()](/Java/DayOfWeek/query)
* [range()](/Java/DayOfWeek/range)
* [valueOf()](/Java/DayOfWeek/valueOf)
* [values()](/Java/DayOfWeek/values)

## Ejemplo
~~~java
{{ site.data.Java.D.DayOfWeek.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DayOfWeek.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
