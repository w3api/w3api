---
title: Collector
permalink: Java/Collector
date: 2021-01-04
key: JavaJava.C.Collector
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.Collector.description }}

## Sintaxis
~~~java
public interface Collector<T,A,R>
~~~

## Métodos
* [accumulator()](/Java/Collector/accumulator)
* [characteristics()](/Java/Collector/characteristics)
* [combiner()](/Java/Collector/combiner)
* [finisher()](/Java/Collector/finisher)
* [of()](/Java/Collector/of)
* [supplier()](/Java/Collector/supplier)

## Ejemplo
~~~java
{{ site.data.Java.C.Collector.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Collector.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
