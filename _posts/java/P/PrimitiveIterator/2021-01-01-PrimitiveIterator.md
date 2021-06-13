---
title: PrimitiveIterator
permalink: /Java/PrimitiveIterator/
date: 2021-01-11
key: Java.P.PrimitiveIterator
category: java
tags: ['java se', 'java.util', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PrimitiveIterator.description }}

## Sintaxis
~~~java
public interface PrimitiveIterator<T,T_CONS> extends Iterator<T>
~~~

## Métodos
* [forEachRemaining()](/Java/PrimitiveIterator/forEachRemaining)

## Ejemplo
~~~java
{{ site.data.Java.P.PrimitiveIterator.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrimitiveIterator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
