---
title: INV_OBJREF.INV_OBJREF()
permalink: /Java/INV_OBJREF/INV_OBJREF/
date: 2021-01-11
key: Java.I.INV_OBJREF
category: Java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.INV_OBJREF.constructores valor="INV_OBJREF" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public INV_OBJREF()
public INV_OBJREF(int minor, CompletionStatus completed)
public INV_OBJREF(String s)
public INV_OBJREF(String s, int minor, CompletionStatus completed)
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}
* **CompletionStatus completed**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStatus completed" %}
* **int minor**,  {% include w3api/param_description.html metodo=_dato parametro="int minor" %}

## Clase Padre
[INV_OBJREF](/Java/INV_OBJREF/)

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
