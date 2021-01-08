---
title: LocalDate.atTime()
permalink: Java/LocalDate/atTime
date: 2021-01-04
key: JavaJava.L.LocalDate
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDate.metodos valor="atTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalDateTime atTime(int hour, int minute)
public LocalDateTime atTime(int hour, int minute, int second)
public LocalDateTime atTime(int hour, int minute, int second, int nanoOfSecond)
public LocalDateTime atTime(LocalTime time)
public OffsetDateTime atTime(OffsetTime time)
~~~

## Parámetros
* **int minute**,  {% include w3api/param_description.html metodo=_data parametro="int minute" %}
* **int nanoOfSecond**,  {% include w3api/param_description.html metodo=_data parametro="int nanoOfSecond" %}
* **OffsetTime time**,  {% include w3api/param_description.html metodo=_data parametro="OffsetTime time" %}
* **int hour**,  {% include w3api/param_description.html metodo=_data parametro="int hour" %}
* **LocalTime time**,  {% include w3api/param_description.html metodo=_data parametro="LocalTime time" %}
* **int second**,  {% include w3api/param_description.html metodo=_data parametro="int second" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[LocalDate](/Java/LocalDate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LocalDate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
