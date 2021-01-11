---
title: PathIterator
permalink: Java/PathIterator
date: 2021-01-11
key: JavaJava.P.PathIterator
category: java
tags: ['java se', 'java.awt.geom', 'java.desktop', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PathIterator.description }}

## Sintaxis
~~~java
public interface PathIterator
~~~

## Campos
* [SEG_CLOSE](/Java/PathIterator/SEG_CLOSE)
* [SEG_CUBICTO](/Java/PathIterator/SEG_CUBICTO)
* [SEG_LINETO](/Java/PathIterator/SEG_LINETO)
* [SEG_MOVETO](/Java/PathIterator/SEG_MOVETO)
* [SEG_QUADTO](/Java/PathIterator/SEG_QUADTO)
* [WIND_EVEN_ODD](/Java/PathIterator/WIND_EVEN_ODD)
* [WIND_NON_ZERO](/Java/PathIterator/WIND_NON_ZERO)

## Métodos
* [currentSegment()](/Java/PathIterator/currentSegment)
* [getWindingRule()](/Java/PathIterator/getWindingRule)
* [isDone()](/Java/PathIterator/isDone)
* [next()](/Java/PathIterator/next)

## Ejemplo
~~~java
{{ site.data.Java.P.PathIterator.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PathIterator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
