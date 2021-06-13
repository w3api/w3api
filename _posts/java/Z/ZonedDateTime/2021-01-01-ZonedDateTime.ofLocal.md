---
title: ZonedDateTime.ofLocal()
permalink: /Java/ZonedDateTime/ofLocal/
date: 2021-01-11
key: Java.Z.ZonedDateTime
category: Java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZonedDateTime.metodos valor="ofLocal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ZonedDateTime ofLocal(LocalDateTime localDateTime, ZoneId zone, ZoneOffset preferredOffset)
~~~

## Parámetros
* **ZoneOffset preferredOffset**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffset preferredOffset" %}
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneId zone" %}
* **LocalDateTime localDateTime**,  {% include w3api/param_description.html metodo=_dato parametro="LocalDateTime localDateTime" %}

## Clase Padre
[ZonedDateTime](/Java/ZonedDateTime/)

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
