---
title: LinkedHashMap.removeEldestEntry()
permalink: /Java/LinkedHashMap/removeEldestEntry/
date: 2021-01-11
key: Java.L.LinkedHashMap
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkedHashMap.metodos valor="removeEldestEntry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected boolean removeEldestEntry(Map.Entry<K,V> eldest)
~~~

## Parámetros
* **V&gt; eldest**,  {% include w3api/param_description.html metodo=_dato parametro="V> eldest" %}
* **Map.Entry&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="Map.Entry<K" %}

## Clase Padre
[LinkedHashMap](/Java/LinkedHashMap/)

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
