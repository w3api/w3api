---
title: ConcurrentHashMap.reduceEntriesToDouble()
permalink: Java/ConcurrentHashMap/reduceEntriesToDouble
date: 2021-01-04
key: JavaJava.C.ConcurrentHashMap
category: java
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
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_data parametro="long parallelismThreshold" %}
* **ToDoubleFunction&lt;Map.Entry&lt;K**,  {% include w3api/param_description.html metodo=_data parametro="ToDoubleFunction<Map.Entry<K" %}
* **DoubleBinaryOperator reducer**,  {% include w3api/param_description.html metodo=_data parametro="DoubleBinaryOperator reducer" %}
* **V&gt;&gt; transformer**,  {% include w3api/param_description.html metodo=_data parametro="V>> transformer" %}
* **double basis**,  {% include w3api/param_description.html metodo=_data parametro="double basis" %}

## Clase Padre
[ConcurrentHashMap](/Java/ConcurrentHashMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentHashMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
