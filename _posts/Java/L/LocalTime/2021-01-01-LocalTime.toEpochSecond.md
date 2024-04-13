---
title: LocalTime.toEpochSecond()
permalink: /Java/LocalTime/toEpochSecond/
date: 2021-01-11
key: Java.L.LocalTime
category: Java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalTime.metodos valor="toEpochSecond" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long toEpochSecond(LocalDate date, ZoneOffset offset)
~~~

## Parámetros
* **ZoneOffset offset**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffset offset" %}
* **LocalDate date**,  {% include w3api/param_description.html metodo=_dato parametro="LocalDate date" %}

## Clase Padre
[LocalTime](/Java/LocalTime/)

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
