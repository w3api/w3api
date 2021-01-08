---
title: NameHelper.write()
permalink: Java/NameHelper/write
date: 2021-01-04
key: JavaJava.N.NameHelper
category: java
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
* **OutputStream ostream**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream ostream" %}
* **NameComponent[] value**,  {% include w3api/param_description.html metodo=_data parametro="NameComponent[] value" %}

## Clase Padre
[NameHelper](/Java/NameHelper/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NameHelper.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
