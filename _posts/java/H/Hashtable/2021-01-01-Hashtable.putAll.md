---
title: Hashtable.putAll()
permalink: /Java/Hashtable/putAll/
date: 2021-01-11
key: Java.H.Hashtable
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.Hashtable.metodos valor="putAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void putAll(Map<? extends K,? extends V> t)
~~~

## Parámetros
* **Map&lt;? extends K**,  {% include w3api/param_description.html metodo=_dato parametro="Map<? extends K" %}
* **? extends V&gt; t**,  {% include w3api/param_description.html metodo=_dato parametro="? extends V> t" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
