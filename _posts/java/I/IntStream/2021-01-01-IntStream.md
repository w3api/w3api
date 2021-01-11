---
title: IntStream
permalink: Java/IntStream
date: 2021-01-11
key: JavaJava.I.IntStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.IntStream.description }}

## Sintaxis
~~~java
public interface IntStream extends BaseStream<Integer,IntStream>
~~~

## Métodos
* [allMatch()](/Java/IntStream/allMatch)
* [anyMatch()](/Java/IntStream/anyMatch)
* [asDoubleStream()](/Java/IntStream/asDoubleStream)
* [asLongStream()](/Java/IntStream/asLongStream)
* [average()](/Java/IntStream/average)
* [boxed()](/Java/IntStream/boxed)
* [builder()](/Java/IntStream/builder)
* [collect()](/Java/IntStream/collect)
* [concat()](/Java/IntStream/concat)
* [count()](/Java/IntStream/count)
* [distinct()](/Java/IntStream/distinct)
* [dropWhile()](/Java/IntStream/dropWhile)
* [empty()](/Java/IntStream/empty)
* [filter()](/Java/IntStream/filter)
* [findAny()](/Java/IntStream/findAny)
* [findFirst()](/Java/IntStream/findFirst)
* [flatMap()](/Java/IntStream/flatMap)
* [forEach()](/Java/IntStream/forEach)
* [forEachOrdered()](/Java/IntStream/forEachOrdered)
* [generate()](/Java/IntStream/generate)
* [iterate()](/Java/IntStream/iterate)
* [limit()](/Java/IntStream/limit)
* [map()](/Java/IntStream/map)
* [mapToDouble()](/Java/IntStream/mapToDouble)
* [mapToLong()](/Java/IntStream/mapToLong)
* [mapToObj()](/Java/IntStream/mapToObj)
* [max()](/Java/IntStream/max)
* [min()](/Java/IntStream/min)
* [noneMatch()](/Java/IntStream/noneMatch)
* [of()](/Java/IntStream/of)
* [peek()](/Java/IntStream/peek)
* [range()](/Java/IntStream/range)
* [rangeClosed()](/Java/IntStream/rangeClosed)
* [reduce()](/Java/IntStream/reduce)
* [skip()](/Java/IntStream/skip)
* [sorted()](/Java/IntStream/sorted)
* [sum()](/Java/IntStream/sum)
* [summaryStatistics()](/Java/IntStream/summaryStatistics)
* [takeWhile()](/Java/IntStream/takeWhile)
* [toArray()](/Java/IntStream/toArray)

## Ejemplo
~~~java
{{ site.data.Java.I.IntStream.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IntStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
