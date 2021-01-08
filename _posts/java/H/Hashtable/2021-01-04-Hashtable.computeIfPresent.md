---
title: Hashtable.computeIfPresent()
permalink: Java/Hashtable/computeIfPresent
date: 2021-01-04
key: JavaJava.H.Hashtable
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.Hashtable.metodos valor="computeIfPresent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V computeIfPresent(K key, BiFunction<? super K,? super V,? extends V> remappingFunction)
~~~

## Parámetros
* **? super V**,  {% include w3api/param_description.html metodo=_data parametro="? super V" %}
* **K key**,  {% include w3api/param_description.html metodo=_data parametro="K key" %}
* **BiFunction&lt;? super K**,  {% include w3api/param_description.html metodo=_data parametro="BiFunction<? super K" %}
* **? extends V&gt; remappingFunction**,  {% include w3api/param_description.html metodo=_data parametro="? extends V> remappingFunction" %}

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
{%- for _ldc in site.data.Java.H.Hashtable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
