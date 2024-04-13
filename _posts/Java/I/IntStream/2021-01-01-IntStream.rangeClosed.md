---
title: IntStream.rangeClosed()
permalink: /Java/IntStream/rangeClosed/
date: 2021-01-11
key: Java.I.IntStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntStream.metodos valor="rangeClosed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static IntStream rangeClosed(int startInclusive, int endInclusive)
~~~

## Parámetros
* **int startInclusive**,  {% include w3api/param_description.html metodo=_dato parametro="int startInclusive" %}
* **int endInclusive**,  {% include w3api/param_description.html metodo=_dato parametro="int endInclusive" %}

## Clase Padre
[IntStream](/Java/IntStream/)

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
