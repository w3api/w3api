---
title: ContextList.item()
permalink: Java/ContextList/item
date: 2021-01-11
key: JavaJava.C.ContextList
category: java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'JDKJava 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ContextList.metodos valor="item" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract String item(int index) throws Bounds
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Clase Padre
[ContextList](/Java/ContextList/)

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