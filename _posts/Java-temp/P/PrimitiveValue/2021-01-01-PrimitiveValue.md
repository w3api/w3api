---
title: PrimitiveValue
permalink: /Java/PrimitiveValue/
date: 2021-01-11
key: Java.P.PrimitiveValue
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PrimitiveValue.description }}

## Sintaxis
~~~java
public interface PrimitiveValue extends Value
~~~

## Métodos
* [booleanValue()](/Java/PrimitiveValue/booleanValue)
* [byteValue()](/Java/PrimitiveValue/byteValue)
* [charValue()](/Java/PrimitiveValue/charValue)
* [doubleValue()](/Java/PrimitiveValue/doubleValue)
* [floatValue()](/Java/PrimitiveValue/floatValue)
* [intValue()](/Java/PrimitiveValue/intValue)
* [longValue()](/Java/PrimitiveValue/longValue)
* [shortValue()](/Java/PrimitiveValue/shortValue)

## Ejemplo
~~~java
{{ site.data.Java.P.PrimitiveValue.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.PrimitiveValue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
