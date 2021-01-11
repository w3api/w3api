---
title: AbstractMap.SimpleEntry.AbstractMap.SimpleEntry()
permalink: Java/AbstractMap/SimpleEntry/AbstractMap/SimpleEntry
date: 2021-01-11
key: JavaJava.A.AbstractMap.SimpleEntry
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractMap.SimpleEntry.constructores valor="AbstractMap.SimpleEntry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SimpleEntry(Map.Entry<? extends K,? extends V> entry)
public SimpleEntry(K key, V value)
~~~

## Parámetros
* **? extends V&gt; entry**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> entry" %}
* **V value**,  {% include w3api/param_description.html metodo=_dato parametro="V value" %}
* **K key**,  {% include w3api/param_description.html metodo=_dato parametro="K key" %}
* **Map.Entry&lt;? extends K**,  {% include w3api/param_description.html metodo=_dato parametro="Map.Entry<? extends K" %}

## Clase Padre
[AbstractMap.SimpleEntry](/Java/AbstractMap/SimpleEntry/)

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
