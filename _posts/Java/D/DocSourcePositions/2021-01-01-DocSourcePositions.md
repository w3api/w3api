---
title: DocSourcePositions
permalink: /Java/DocSourcePositions/
date: 2021-01-11
key: Java.D.DocSourcePositions
category: Java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DocSourcePositions.description }}

## Sintaxis
~~~java
public interface DocSourcePositions extends SourcePositions
~~~

## Métodos
* [getEndPosition()](/Java/DocSourcePositions/getEndPosition/)
* [getStartPosition()](/Java/DocSourcePositions/getStartPosition/)

## Ejemplo
~~~java
{{ site.data.Java.D.DocSourcePositions.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DocSourcePositions.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
