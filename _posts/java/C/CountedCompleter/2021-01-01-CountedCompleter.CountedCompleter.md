---
title: CountedCompleter.CountedCompleter()
permalink: /Java/CountedCompleter/CountedCompleter/
date: 2021-01-11
key: Java.C.CountedCompleter
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CountedCompleter.constructores valor="CountedCompleter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected CountedCompleter()
protected CountedCompleter(CountedCompleter<?> completer)
protected CountedCompleter(CountedCompleter<?> completer, int initialPendingCount)
~~~

## Parámetros
* **CountedCompleter&lt;?&gt; completer**,  {% include w3api/param_description.html metodo=_dato parametro="CountedCompleter<?> completer" %}
* **int initialPendingCount**,  {% include w3api/param_description.html metodo=_dato parametro="int initialPendingCount" %}

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
