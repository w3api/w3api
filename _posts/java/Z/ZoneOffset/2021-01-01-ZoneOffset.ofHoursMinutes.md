---
title: ZoneOffset.ofHoursMinutes()
permalink: Java/ZoneOffset/ofHoursMinutes
date: 2021-01-11
key: JavaJava.Z.ZoneOffset
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZoneOffset.metodos valor="ofHoursMinutes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ZoneOffset ofHoursMinutes(int hours, int minutes)
~~~

## Parámetros
* **int minutes**,  {% include w3api/param_description.html metodo=_dato parametro="int minutes" %}
* **int hours**,  {% include w3api/param_description.html metodo=_dato parametro="int hours" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[ZoneOffset](/Java/ZoneOffset/)

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
