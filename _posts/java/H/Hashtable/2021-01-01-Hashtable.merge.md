---
title: Hashtable.merge()
permalink: /Java/Hashtable/merge/
date: 2021-01-11
key: Java.H.Hashtable
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.Hashtable.metodos valor="merge" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V merge(K key, V value, BiFunction<? super V,? super V,? extends V> remappingFunction)
~~~

## Parámetros
* **? super V**,  {% include w3api/param_description.html metodo=_dato parametro="? super V" %}
* **V value**,  {% include w3api/param_description.html metodo=_dato parametro="V value" %}
* **? extends V&gt; remappingFunction**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> remappingFunction" %}
* **K key**,  {% include w3api/param_description.html metodo=_dato parametro="K key" %}
* **BiFunction&lt;? super V**,  {% include w3api/param_description.html metodo=_dato parametro="BiFunction<? super V" %}

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
