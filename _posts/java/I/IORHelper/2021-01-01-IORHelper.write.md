---
title: IORHelper.write()
permalink: /Java/IORHelper/write/
date: 2021-01-11
key: Java.I.IORHelper
category: Java
tags: ['java se', 'org.omg.IOP', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IORHelper.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void write(OutputStream ostream, IOR value)
~~~

## Parámetros
* **IOR value**,  {% include w3api/param_description.html metodo=_dato parametro="IOR value" %}
* **OutputStream ostream**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream ostream" %}

## Clase Padre
[IORHelper](/Java/IORHelper/)

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
