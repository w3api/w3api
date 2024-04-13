---
title: Hashtable.computeIfAbsent()
permalink: /Java/Hashtable/computeIfAbsent/
date: 2021-01-11
key: Java.H.Hashtable
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.Hashtable.metodos valor="computeIfAbsent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V computeIfAbsent(K key, Function<? super K,? extends V> mappingFunction)
~~~

## Parámetros
* **? extends V&gt; mappingFunction**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> mappingFunction" %}
* **K key**,  {% include w3api/param_description.html metodo=_dato parametro="K key" %}
* **Function&lt;? super K**,  {% include w3api/param_description.html metodo=_dato parametro="Function<? super K" %}

## Excepciones
[ConcurrentModificationException](/Java/ConcurrentModificationException/)

## Clase Padre
[Hashtable](/Java/Hashtable/)

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
