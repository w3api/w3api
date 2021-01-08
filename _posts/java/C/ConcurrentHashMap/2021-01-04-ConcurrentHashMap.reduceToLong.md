---
title: ConcurrentHashMap.reduceToLong()
permalink: Java/ConcurrentHashMap/reduceToLong
date: 2021-01-04
key: JavaJava.C.ConcurrentHashMap
category: java
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
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_data parametro="long parallelismThreshold" %}
* **long basis**,  {% include w3api/param_description.html metodo=_data parametro="long basis" %}
* **ToLongBiFunction&lt;? super K**,  {% include w3api/param_description.html metodo=_data parametro="ToLongBiFunction<? super K" %}
* **? super V&gt; transformer**,  {% include w3api/param_description.html metodo=_data parametro="? super V> transformer" %}
* **LongBinaryOperator reducer**,  {% include w3api/param_description.html metodo=_data parametro="LongBinaryOperator reducer" %}

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
