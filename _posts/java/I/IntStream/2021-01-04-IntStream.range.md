---
title: IntStream.range()
permalink: Java/IntStream/range
date: 2021-01-04
key: JavaJava.I.IntStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntStream.metodos valor="range" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static IntStream range(int startInclusive, int endExclusive)
~~~

## Parámetros
* **int endExclusive**,  {% include w3api/param_description.html metodo=_data parametro="int endExclusive" %}
* **int startInclusive**,  {% include w3api/param_description.html metodo=_data parametro="int startInclusive" %}

## Clase Padre
[IntStream](/Java/IntStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IntStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
