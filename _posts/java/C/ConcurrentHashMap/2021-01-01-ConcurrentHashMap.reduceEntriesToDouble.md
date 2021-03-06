---
title: ConcurrentHashMap.reduceEntriesToDouble()
permalink: /Java/ConcurrentHashMap/reduceEntriesToDouble/
date: 2021-01-11
key: Java.C.ConcurrentHashMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="reduceEntriesToDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double reduceEntriesToDouble(long parallelismThreshold, ToDoubleFunction<Map.Entry<K,V>> transformer, double basis, DoubleBinaryOperator reducer)
~~~

## Parámetros
* **ToDoubleFunction&lt;Map.Entry&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="ToDoubleFunction<Map.Entry<K" %}
* **DoubleBinaryOperator reducer**,  {% include w3api/param_description.html metodo=_dato parametro="DoubleBinaryOperator reducer" %}
* **double basis**,  {% include w3api/param_description.html metodo=_dato parametro="double basis" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_dato parametro="long parallelismThreshold" %}
* **V&gt;&gt; transformer**,  {% include w3api/param_description.html metodo=_dato parametro="V>> transformer" %}

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
