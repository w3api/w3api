---
title: JapaneseDate.now()
permalink: /Java/JapaneseDate/now/
date: 2021-01-11
key: Java.J.JapaneseDate
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JapaneseDate.metodos valor="now" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static JapaneseDate now()
public static JapaneseDate now(Clock clock)
public static JapaneseDate now(ZoneId zone)
~~~

## Parámetros
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneId zone" %}
* **Clock clock**,  {% include w3api/param_description.html metodo=_dato parametro="Clock clock" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[JapaneseDate](/Java/JapaneseDate/)

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
