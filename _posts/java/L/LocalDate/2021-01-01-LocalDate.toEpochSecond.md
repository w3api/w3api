---
title: LocalDate.toEpochSecond()
permalink: Java/LocalDate/toEpochSecond
date: 2021-01-11
key: JavaJava.L.LocalDate
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDate.metodos valor="toEpochSecond" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long toEpochSecond(LocalTime time, ZoneOffset offset)
~~~

## Parámetros
* **ZoneOffset offset**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffset offset" %}
* **LocalTime time**,  {% include w3api/param_description.html metodo=_dato parametro="LocalTime time" %}

## Clase Padre
[LocalDate](/Java/LocalDate/)

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
