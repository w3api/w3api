---
title: LongAccumulator
permalink: /Java/LongAccumulator/
date: 2021-01-11
key: Java.L.LongAccumulator
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'clase java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LongAccumulator.description }}

## Sintaxis
~~~java
public class LongAccumulator extends Number implements Serializable
~~~

## Constructores
* [LongAccumulator()](/Java/LongAccumulator/LongAccumulator/)

## Métodos
* [accumulate()](/Java/LongAccumulator/accumulate)
* [doubleValue()](/Java/LongAccumulator/doubleValue)
* [floatValue()](/Java/LongAccumulator/floatValue)
* [get()](/Java/LongAccumulator/get)
* [getThenReset()](/Java/LongAccumulator/getThenReset)
* [intValue()](/Java/LongAccumulator/intValue)
* [longValue()](/Java/LongAccumulator/longValue)
* [reset()](/Java/LongAccumulator/reset)
* [toString()](/Java/LongAccumulator/toString)

## Ejemplo
~~~java
{{ site.data.Java.L.LongAccumulator.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LongAccumulator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
