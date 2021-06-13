---
title: IntStream.concat()
permalink: /Java/IntStream/concat/
date: 2021-01-11
key: Java.I.IntStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntStream.metodos valor="concat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static IntStream concat(IntStream a, IntStream b)
~~~

## Parámetros
* **IntStream b**,  {% include w3api/param_description.html metodo=_dato parametro="IntStream b" %}
* **IntStream a**,  {% include w3api/param_description.html metodo=_dato parametro="IntStream a" %}

## Clase Padre
[IntStream](/Java/IntStream/)

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
