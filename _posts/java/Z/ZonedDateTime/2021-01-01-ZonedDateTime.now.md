---
title: ZonedDateTime.now()
permalink: Java/ZonedDateTime/now
date: 2021-01-11
key: JavaJava.Z.ZonedDateTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZonedDateTime.metodos valor="now" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ZonedDateTime now()
public static ZonedDateTime now(Clock clock)
public static ZonedDateTime now(ZoneId zone)
~~~

## Parámetros
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneId zone" %}
* **Clock clock**,  {% include w3api/param_description.html metodo=_dato parametro="Clock clock" %}

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
