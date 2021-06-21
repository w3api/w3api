---
title: CountedCompleter.compareAndSetPendingCount()
permalink: /Java/CountedCompleter/compareAndSetPendingCount/
date: 2021-01-11
key: Java.C.CountedCompleter
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CountedCompleter.metodos valor="compareAndSetPendingCount" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final boolean compareAndSetPendingCount(int expected, int count)
~~~

## Parámetros
* **int expected**,  {% include w3api/param_description.html metodo=_dato parametro="int expected" %}
* **int count**,  {% include w3api/param_description.html metodo=_dato parametro="int count" %}

## Clase Padre
[CountedCompleter](/Java/CountedCompleter/)

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
