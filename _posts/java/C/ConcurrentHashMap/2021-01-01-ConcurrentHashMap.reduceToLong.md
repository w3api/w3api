---
title: ConcurrentHashMap.reduceToLong()
permalink: /Java/ConcurrentHashMap/reduceToLong/
date: 2021-01-11
key: Java.C.ConcurrentHashMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="reduceToLong" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long reduceToLong(long parallelismThreshold, ToLongBiFunction<? super K,? super V> transformer, long basis, LongBinaryOperator reducer)
~~~

## Parámetros
* **long basis**,  {% include w3api/param_description.html metodo=_dato parametro="long basis" %}
* **LongBinaryOperator reducer**,  {% include w3api/param_description.html metodo=_dato parametro="LongBinaryOperator reducer" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_dato parametro="long parallelismThreshold" %}
* **? super V&gt; transformer**,  {% include w3api/param_description.html metodo=_dato parametro="? super V> transformer" %}
* **ToLongBiFunction&lt;? super K**,  {% include w3api/param_description.html metodo=_dato parametro="ToLongBiFunction<? super K" %}

## Clase Padre
[ConcurrentHashMap](/Java/ConcurrentHashMap/)

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
