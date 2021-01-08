---
title: ShortValue
permalink: Java/ShortValue
date: 2021-01-04
key: JavaJava.S.ShortValue
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.ShortValue.description }}

## Sintaxis
~~~java
public interface ShortValue extends PrimitiveValue, Comparable<ShortValue>
~~~

## Métodos
* [equals()](/Java/ShortValue/equals)
* [hashCode()](/Java/ShortValue/hashCode)
* [value()](/Java/ShortValue/value)

## Ejemplo
~~~java
{{ site.data.Java.S.ShortValue.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ShortValue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
