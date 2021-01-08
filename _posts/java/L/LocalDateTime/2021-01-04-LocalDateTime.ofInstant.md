---
title: LocalDateTime.ofInstant()
permalink: Java/LocalDateTime/ofInstant
date: 2021-01-04
key: JavaJava.L.LocalDateTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDateTime.metodos valor="ofInstant" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static LocalDateTime ofInstant(Instant instant, ZoneId zone)
~~~

## Parámetros
* **Instant instant**,  {% include w3api/param_description.html metodo=_data parametro="Instant instant" %}
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_data parametro="ZoneId zone" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[LocalDateTime](/Java/LocalDateTime/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LocalDateTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
