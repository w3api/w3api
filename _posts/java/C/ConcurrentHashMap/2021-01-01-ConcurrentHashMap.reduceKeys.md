---
title: ConcurrentHashMap.reduceKeys()
permalink: /Java/ConcurrentHashMap/reduceKeys/
date: 2021-01-11
key: Java.C.ConcurrentHashMap
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="reduceKeys" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public K reduceKeys(long parallelismThreshold, BiFunction<? super K,? super K,? extends K> reducer)
<U> U reduceKeys(long parallelismThreshold, Function<? super K,? extends U> transformer, BiFunction<? super U,? super U,? extends U> reducer)
~~~

## Parámetros
* **Function&lt;? super K**,  {% include w3api/param_description.html metodo=_dato parametro="Function<? super K" %}
* **? super K**,  {% include w3api/param_description.html metodo=_dato parametro="? super K" %}
* **BiFunction&lt;? super K**,  {% include w3api/param_description.html metodo=_dato parametro="BiFunction<? super K" %}
* **? super U**,  {% include w3api/param_description.html metodo=_dato parametro="? super U" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_dato parametro="long parallelismThreshold" %}
* **BiFunction&lt;? super U**,  {% include w3api/param_description.html metodo=_dato parametro="BiFunction<? super U" %}
* **? extends U&gt; reducer**,  {% include w3api/param_description.html metodo=_dato parametro="? extends U> reducer" %}
* **? extends K&gt; reducer**,  {% include w3api/param_description.html metodo=_dato parametro="? extends K> reducer" %}
* **? extends U&gt; transformer**,  {% include w3api/param_description.html metodo=_dato parametro="? extends U> transformer" %}

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
