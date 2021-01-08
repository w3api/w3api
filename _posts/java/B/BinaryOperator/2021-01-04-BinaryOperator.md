---
title: BinaryOperator
permalink: Java/BinaryOperator
date: 2021-01-04
key: JavaJava.B.BinaryOperator
category: java
tags: ['java se', 'java.util.function', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BinaryOperator.description }}

## Sintaxis
~~~java
@FunctionalInterface public interface BinaryOperator<T> extends BiFunction<T,T,T>
~~~

## Métodos
* [maxBy()](/Java/BinaryOperator/maxBy)
* [minBy()](/Java/BinaryOperator/minBy)

## Ejemplo
~~~java
{{ site.data.Java.B.BinaryOperator.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BinaryOperator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
