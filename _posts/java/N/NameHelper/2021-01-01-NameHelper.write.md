---
title: NameHelper.write()
permalink: /Java/NameHelper/write/
date: 2021-01-11
key: Java.N.NameHelper
category: Java
tags: ['java se', 'org.omg.CosNaming', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NameHelper.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void write(OutputStream ostream, NameComponent[] value)
~~~

## Parámetros
* **NameComponent[] value**,  {% include w3api/param_description.html metodo=_dato parametro="NameComponent[] value" %}
* **OutputStream ostream**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream ostream" %}

## Clase Padre
[NameHelper](/Java/NameHelper/)

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
