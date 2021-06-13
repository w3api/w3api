---
title: LongValue
permalink: /Java/LongValue/
date: 2021-01-11
key: Java.L.LongValue
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LongValue.description }}

## Sintaxis
~~~java
public interface LongValue extends PrimitiveValue, Comparable<LongValue>
~~~

## Métodos
* [equals()](/Java/LongValue/equals)
* [hashCode()](/Java/LongValue/hashCode)
* [value()](/Java/LongValue/value)

## Ejemplo
~~~java
{{ site.data.Java.L.LongValue.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LongValue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
