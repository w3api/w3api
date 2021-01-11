---
title: Chronology.period()
permalink: Java/Chronology/period
date: 2021-01-11
key: JavaJava.C.Chronology
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Chronology.metodos valor="period" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default ChronoPeriod period(int years, int months, int days)
~~~

## Parámetros
* **int months**,  {% include w3api/param_description.html metodo=_dato parametro="int months" %}
* **int years**,  {% include w3api/param_description.html metodo=_dato parametro="int years" %}
* **int days**,  {% include w3api/param_description.html metodo=_dato parametro="int days" %}

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
