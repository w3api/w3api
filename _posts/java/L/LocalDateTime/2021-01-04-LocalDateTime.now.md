---
title: LocalDateTime.now()
permalink: Java/LocalDateTime/now
date: 2021-01-04
key: JavaJava.L.LocalDateTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDateTime.metodos valor="now" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static LocalDateTime now()
public static LocalDateTime now(Clock clock)
public static LocalDateTime now(ZoneId zone)
~~~

## Parámetros
* **Clock clock**,  {% include w3api/param_description.html metodo=_data parametro="Clock clock" %}
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_data parametro="ZoneId zone" %}

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
