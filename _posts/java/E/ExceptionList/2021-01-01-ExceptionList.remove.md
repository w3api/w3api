---
title: ExceptionList.remove()
permalink: /Java/ExceptionList/remove/
date: 2021-01-11
key: Java.E.ExceptionList
category: Java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'JDKJava 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExceptionList.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void remove(int index) throws Bounds
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Clase Padre
[ExceptionList](/Java/ExceptionList/)

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
