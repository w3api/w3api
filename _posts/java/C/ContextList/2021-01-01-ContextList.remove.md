---
title: ContextList.remove()
permalink: /Java/ContextList/remove/
date: 2021-01-11
key: Java.C.ContextList
category: Java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ContextList.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void remove(int index) throws Bounds
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Clase Padre
[ContextList](/Java/ContextList/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
