---
title: Collector.Characteristics
permalink: Java/Collector/Characteristics
date: 2021-01-04
key: JavaJava.C.Collector.Characteristics
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'enumerado java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.Collector.Characteristics.description }}

## Sintaxis
~~~java
public static enum Collector.Characteristics extends Enum<Collector.Characteristics>
~~~

## Enumerados
* [CONCURRENT](/Java/Collector/Characteristics/CONCURRENT)
* [IDENTITY_FINISH](/Java/Collector/Characteristics/IDENTITY_FINISH)
* [UNORDERED](/Java/Collector/Characteristics/UNORDERED)

## Métodos
* [valueOf()](/Java/Collector/Characteristics/valueOf)
* [values()](/Java/Collector/Characteristics/values)

## Ejemplo
~~~java
{{ site.data.Java.C.Collector.Characteristics.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Collector.Characteristics.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
