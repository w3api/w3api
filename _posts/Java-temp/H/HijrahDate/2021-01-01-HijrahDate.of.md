---
title: HijrahDate.of()
permalink: /Java/HijrahDate/of/
date: 2021-01-11
key: Java.H.HijrahDate
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HijrahDate.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static HijrahDate of(int prolepticYear, int month, int dayOfMonth)
~~~

## Parámetros
* **int month**,  {% include w3api/param_description.html metodo=_dato parametro="int month" %}
* **int dayOfMonth**,  {% include w3api/param_description.html metodo=_dato parametro="int dayOfMonth" %}
* **int prolepticYear**,  {% include w3api/param_description.html metodo=_dato parametro="int prolepticYear" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[HijrahDate](/Java/HijrahDate/)

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
