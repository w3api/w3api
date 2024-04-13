---
title: Chronology.eraOf()
permalink: /Java/Chronology/eraOf/
date: 2021-01-11
key: Java.C.Chronology
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Chronology.metodos valor="eraOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Era eraOf(int eraValue)
~~~

## Parámetros
* **int eraValue**,  {% include w3api/param_description.html metodo=_dato parametro="int eraValue" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[Chronology](/Java/Chronology/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
