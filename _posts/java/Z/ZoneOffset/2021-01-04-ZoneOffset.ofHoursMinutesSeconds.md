---
title: ZoneOffset.ofHoursMinutesSeconds()
permalink: Java/ZoneOffset/ofHoursMinutesSeconds
date: 2021-01-04
key: JavaJava.Z.ZoneOffset
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZoneOffset.metodos valor="ofHoursMinutesSeconds" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ZoneOffset ofHoursMinutesSeconds(int hours, int minutes, int seconds)
~~~

## Parámetros
* **int seconds**,  {% include w3api/param_description.html metodo=_data parametro="int seconds" %}
* **int hours**,  {% include w3api/param_description.html metodo=_data parametro="int hours" %}
* **int minutes**,  {% include w3api/param_description.html metodo=_data parametro="int minutes" %}

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
{%- for _ldc in site.data.Java.Z.ZoneOffset.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
