---
title: Chronology.prolepticYear()
permalink: /Java/Chronology/prolepticYear/
date: 2021-01-11
key: Java.C.Chronology
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Chronology.metodos valor="prolepticYear" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int prolepticYear(Era era, int yearOfEra)
~~~

## Parámetros
* **Era era**,  {% include w3api/param_description.html metodo=_dato parametro="Era era" %}
* **int yearOfEra**,  {% include w3api/param_description.html metodo=_dato parametro="int yearOfEra" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/), [ClassCastException](/Java/ClassCastException/)

## Clase Padre
[Chronology](/Java/Chronology/)

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
