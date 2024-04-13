---
title: Hashtable.remove()
permalink: /Java/Hashtable/remove/
date: 2021-01-11
key: Java.H.Hashtable
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.Hashtable.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V remove(Object key)
~~~

## Parámetros
* **Object key**,  {% include w3api/param_description.html metodo=_dato parametro="Object key" %}

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
