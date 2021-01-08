---
title: ConcurrentHashMap.reduceKeys()
permalink: Java/ConcurrentHashMap/reduceKeys
date: 2021-01-04
key: JavaJava.C.ConcurrentHashMap
category: java
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
* **Function&lt;? super K**,  {% include w3api/param_description.html metodo=_data parametro="Function<? super K" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_data parametro="long parallelismThreshold" %}
* **? super U**,  {% include w3api/param_description.html metodo=_data parametro="? super U" %}
* **? extends K&gt; reducer**,  {% include w3api/param_description.html metodo=_data parametro="? extends K> reducer" %}
* **? extends U&gt; reducer**,  {% include w3api/param_description.html metodo=_data parametro="? extends U> reducer" %}
* **? super K**,  {% include w3api/param_description.html metodo=_data parametro="? super K" %}
* **BiFunction&lt;? super U**,  {% include w3api/param_description.html metodo=_data parametro="BiFunction<? super U" %}
* **? extends U&gt; transformer**,  {% include w3api/param_description.html metodo=_data parametro="? extends U> transformer" %}
* **BiFunction&lt;? super K**,  {% include w3api/param_description.html metodo=_data parametro="BiFunction<? super K" %}

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
