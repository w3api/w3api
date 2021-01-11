---
title: UnaryOperator
permalink: Java/UnaryOperator
date: 2021-01-11
key: JavaJava.U.UnaryOperator
category: java
tags: ['java se', 'java.util.function', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.U.UnaryOperator.description }}

## Sintaxis
~~~java
@FunctionalInterface public interface UnaryOperator<T> extends Function<T,T>
~~~

## Métodos
* [identity()](/Java/UnaryOperator/identity)

## Ejemplo
~~~java
{{ site.data.Java.U.UnaryOperator.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.UnaryOperator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
