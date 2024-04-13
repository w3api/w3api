---
title: LongAdder
permalink: /Java/LongAdder/
date: 2021-01-11
key: Java.L.LongAdder
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'clase java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LongAdder.description }}

## Sintaxis
~~~java
public class LongAdder extends Number implements Serializable
~~~

## Constructores
* [LongAdder()](/Java/LongAdder/LongAdder/)

## Métodos
* [add()](/Java/LongAdder/add/)
* [decrement()](/Java/LongAdder/decrement/)
* [doubleValue()](/Java/LongAdder/doubleValue/)
* [floatValue()](/Java/LongAdder/floatValue/)
* [increment()](/Java/LongAdder/increment/)
* [intValue()](/Java/LongAdder/intValue/)
* [longValue()](/Java/LongAdder/longValue/)
* [reset()](/Java/LongAdder/reset/)
* [sum()](/Java/LongAdder/sum/)
* [sumThenReset()](/Java/LongAdder/sumThenReset/)
* [toString()](/Java/LongAdder/toString/)

## Ejemplo
~~~java
{{ site.data.Java.L.LongAdder.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LongAdder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
