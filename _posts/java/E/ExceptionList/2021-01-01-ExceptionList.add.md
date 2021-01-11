---
title: ExceptionList.add()
permalink: Java/ExceptionList/add
date: 2021-01-11
key: JavaJava.E.ExceptionList
category: java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'JDKJava 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExceptionList.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void add(TypeCode exc)
~~~

## Parámetros
* **TypeCode exc**,  {% include w3api/param_description.html metodo=_dato parametro="TypeCode exc" %}

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
