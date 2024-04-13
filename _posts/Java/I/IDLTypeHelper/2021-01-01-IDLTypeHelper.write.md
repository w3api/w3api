---
title: IDLTypeHelper.write()
permalink: /Java/IDLTypeHelper/write/
date: 2021-01-11
key: Java.I.IDLTypeHelper
category: Java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IDLTypeHelper.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void write(OutputStream ostream, IDLType value)
~~~

## Parámetros
* **IDLType value**,  {% include w3api/param_description.html metodo=_dato parametro="IDLType value" %}
* **OutputStream ostream**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream ostream" %}

## Clase Padre
[IDLTypeHelper](/Java/IDLTypeHelper/)

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
