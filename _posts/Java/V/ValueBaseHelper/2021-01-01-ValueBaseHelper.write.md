---
title: ValueBaseHelper.write()
permalink: /Java/ValueBaseHelper/write/
date: 2021-01-11
key: Java.V.ValueBaseHelper
category: Java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.ValueBaseHelper.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void write(OutputStream ostream, Serializable value)
~~~

## Parámetros
* **Serializable value**,  {% include w3api/param_description.html metodo=_dato parametro="Serializable value" %}
* **OutputStream ostream**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream ostream" %}

## Clase Padre
[ValueBaseHelper](/Java/ValueBaseHelper/)

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
