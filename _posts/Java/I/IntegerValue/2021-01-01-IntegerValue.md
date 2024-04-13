---
title: IntegerValue
permalink: /Java/IntegerValue/
date: 2021-01-11
key: Java.I.IntegerValue
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.IntegerValue.description }}

## Sintaxis
~~~java
public interface IntegerValue extends PrimitiveValue, Comparable<IntegerValue>
~~~

## Métodos
* [equals()](/Java/IntegerValue/equals/)
* [hashCode()](/Java/IntegerValue/hashCode/)
* [value()](/Java/IntegerValue/value/)

## Ejemplo
~~~java
{{ site.data.Java.I.IntegerValue.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IntegerValue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
