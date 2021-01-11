---
title: MemoryType
permalink: Java/MemoryType
date: 2021-01-11
key: JavaJava.M.MemoryType
category: java
tags: ['java se', 'java.lang.management', 'java.management', 'enumerado java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MemoryType.description }}

## Sintaxis
~~~java
public enum MemoryType extends Enum<MemoryType>
~~~

## Enumerados
* [HEAP](/Java/MemoryType/HEAP)
* [NON_HEAP](/Java/MemoryType/NON_HEAP)

## Métodos
* [toString()](/Java/MemoryType/toString)
* [valueOf()](/Java/MemoryType/valueOf)
* [values()](/Java/MemoryType/values)

## Ejemplo
~~~java
{{ site.data.Java.M.MemoryType.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MemoryType.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
