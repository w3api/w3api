---
title: IORHelper.insert()
permalink: /Java/IORHelper/insert/
date: 2021-01-11
key: Java.I.IORHelper
category: Java
tags: ['java se', 'org.omg.IOP', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IORHelper.metodos valor="insert" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void insert(Any a, IOR that)
~~~

## Parámetros
* **IOR that**,  {% include w3api/param_description.html metodo=_dato parametro="IOR that" %}
* **Any a**,  {% include w3api/param_description.html metodo=_dato parametro="Any a" %}

## Clase Padre
[IORHelper](/Java/IORHelper/)

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
