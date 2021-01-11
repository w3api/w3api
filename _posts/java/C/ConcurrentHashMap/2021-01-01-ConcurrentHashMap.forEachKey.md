---
title: ConcurrentHashMap.forEachKey()
permalink: Java/ConcurrentHashMap/forEachKey
date: 2021-01-11
key: JavaJava.C.ConcurrentHashMap
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentHashMap.metodos valor="forEachKey" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void forEachKey(long parallelismThreshold, Consumer<? super K> action)
<U> void forEachKey(long parallelismThreshold, Function<? super K,? extends U> transformer, Consumer<? super U> action)
~~~

## Parámetros
* **Consumer&lt;? super U&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="Consumer<? super U> action" %}
* **Function&lt;? super K**,  {% include w3api/param_description.html metodo=_dato parametro="Function<? super K" %}
* **long parallelismThreshold**,  {% include w3api/param_description.html metodo=_dato parametro="long parallelismThreshold" %}
* **Consumer&lt;? super K&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="Consumer<? super K> action" %}
* **? extends U&gt; transformer**,  {% include w3api/param_description.html metodo=_dato parametro="? extends U> transformer" %}

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
