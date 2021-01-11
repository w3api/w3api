---
title: CountedCompleter.onExceptionalCompletion()
permalink: Java/CountedCompleter/onExceptionalCompletion
date: 2021-01-11
key: JavaJava.C.CountedCompleter
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CountedCompleter.metodos valor="onExceptionalCompletion" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean onExceptionalCompletion(Throwable ex, CountedCompleter<?> caller)
~~~

## Parámetros
* **Throwable ex**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable ex" %}
* **CountedCompleter&lt;?&gt; caller**,  {% include w3api/param_description.html metodo=_dato parametro="CountedCompleter<?> caller" %}

## Clase Padre
[CountedCompleter](/Java/CountedCompleter/)

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
