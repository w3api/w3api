---
title: DynAnyHelper.write()
permalink: Java/DynAnyHelper/write
date: 2021-01-11
key: JavaJava.D.DynAnyHelper
category: java
tags: ['java se', 'org.omg.DynamicAny', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DynAnyHelper.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void write(OutputStream ostream, DynAny value)
~~~

## Parámetros
* **DynAny value**,  {% include w3api/param_description.html metodo=_dato parametro="DynAny value" %}
* **OutputStream ostream**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream ostream" %}

## Clase Padre
[DynAnyHelper](/Java/DynAnyHelper/)

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
