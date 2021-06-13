---
title: LongStream.concat()
permalink: Java/LongStream/concat
date: 2021-01-11
key: Java.L.LongStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongStream.metodos valor="concat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static LongStream concat(LongStream a, LongStream b)
~~~

## Parámetros
* **LongStream b**,  {% include w3api/param_description.html metodo=_dato parametro="LongStream b" %}
* **LongStream a**,  {% include w3api/param_description.html metodo=_dato parametro="LongStream a" %}

## Clase Padre
[LongStream](/Java/LongStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
