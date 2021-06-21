---
title: ConcurrentHashMap.reduceValuesToDouble()
permalink: /Java/ConcurrentHashMap/reduceValuesToDouble/
date: 2021-01-11
key: Java.C.ConcurrentHashMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="reduceValuesToDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double reduceValuesToDouble(long parallelismThreshold, ToDoubleFunction<? super V> transformer, double basis, DoubleBinaryOperator reducer)
~~~

## Parámetros
* **ToDoubleFunction&lt;? super V&gt; transformer**,  {% include w3api/param_description.html metodo=_dato parametro="ToDoubleFunction<? super V> transformer" %}
* **DoubleBinaryOperator reducer**,  {% include w3api/param_description.html metodo=_dato parametro="DoubleBinaryOperator reducer" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_dato parametro="long parallelismThreshold" %}
* **double basis**,  {% include w3api/param_description.html metodo=_dato parametro="double basis" %}

## Clase Padre
[ConcurrentHashMap](/Java/ConcurrentHashMap/)

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
