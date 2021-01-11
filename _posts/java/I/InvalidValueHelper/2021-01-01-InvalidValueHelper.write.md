---
title: InvalidValueHelper.write()
permalink: Java/InvalidValueHelper/write
date: 2021-01-11
key: JavaJava.I.InvalidValueHelper
category: java
tags: ['java se', 'org.omg.DynamicAny.DynAnyPackage', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InvalidValueHelper.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void write(OutputStream ostream, InvalidValue value)
~~~

## Parámetros
* **InvalidValue value**,  {% include w3api/param_description.html metodo=_dato parametro="InvalidValue value" %}
* **OutputStream ostream**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream ostream" %}

## Clase Padre
[InvalidValueHelper](/Java/InvalidValueHelper/)

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
