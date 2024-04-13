---
title: Collector.combiner()
permalink: /Java/Collector/combiner/
date: 2021-01-11
key: Java.C.Collector
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collector.metodos valor="combiner" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
BinaryOperator<A> combiner()
~~~

## Clase Padre
[Collector](/Java/Collector/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
