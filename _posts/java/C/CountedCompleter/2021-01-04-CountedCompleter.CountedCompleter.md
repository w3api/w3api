---
title: CountedCompleter.CountedCompleter()
permalink: Java/CountedCompleter/CountedCompleter
date: 2021-01-04
key: JavaJava.C.CountedCompleter
category: java
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
* **int initialPendingCount**,  {% include w3api/param_description.html metodo=_data parametro="int initialPendingCount" %}
* **CountedCompleter&lt;?&gt; completer**,  {% include w3api/param_description.html metodo=_data parametro="CountedCompleter<?> completer" %}

## Clase Padre
[CountedCompleter](/Java/CountedCompleter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CountedCompleter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
