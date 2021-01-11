---
title: ConcurrentHashMap.reduceValues()
permalink: Java/ConcurrentHashMap/reduceValues
date: 2021-01-11
key: JavaJava.C.ConcurrentHashMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="reduceValues" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V reduceValues(long parallelismThreshold, BiFunction<? super V,? super V,? extends V> reducer)
<U> U reduceValues(long parallelismThreshold, Function<? super V,? extends U> transformer, BiFunction<? super U,? super U,? extends U> reducer)
~~~

## Parámetros
* **? super V**,  {% include w3api/param_description.html metodo=_dato parametro="? super V" %}
* **? super U**,  {% include w3api/param_description.html metodo=_dato parametro="? super U" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_dato parametro="long parallelismThreshold" %}
* **BiFunction&lt;? super U**,  {% include w3api/param_description.html metodo=_dato parametro="BiFunction<? super U" %}
* **Function&lt;? super V**,  {% include w3api/param_description.html metodo=_dato parametro="Function<? super V" %}
* **? extends U&gt; transformer**,  {% include w3api/param_description.html metodo=_dato parametro="? extends U> transformer" %}
* **? extends V&gt; reducer**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> reducer" %}
* **? extends U&gt; reducer**,  {% include w3api/param_description.html metodo=_dato parametro="? extends U> reducer" %}
* **BiFunction&lt;? super V**,  {% include w3api/param_description.html metodo=_dato parametro="BiFunction<? super V" %}

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
