---
title: JapaneseDate.from()
permalink: /Java/JapaneseDate/from/
date: 2021-01-11
key: Java.J.JapaneseDate
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JapaneseDate.metodos valor="from" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static JapaneseDate from(TemporalAccessor temporal)
~~~

## Parámetros
* **TemporalAccessor temporal**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAccessor temporal" %}

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
