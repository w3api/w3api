---
title: OffsetTime.ofInstant()
permalink: Java/OffsetTime/ofInstant
date: 2021-01-04
key: JavaJava.O.OffsetTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OffsetTime.metodos valor="ofInstant" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static OffsetTime ofInstant(Instant instant, ZoneId zone)
~~~

## Parámetros
* **Instant instant**,  {% include w3api/param_description.html metodo=_data parametro="Instant instant" %}
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_data parametro="ZoneId zone" %}

## Clase Padre
[OffsetTime](/Java/OffsetTime/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OffsetTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
