---
title: LinkerServices.asType()
permalink: Java/LinkerServices/asType
date: 2021-01-11
key: Java.L.LinkerServices
category: java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkerServices.metodos valor="asType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
MethodHandle asType(MethodHandle handle, MethodType fromType)
~~~

## Parámetros
* **MethodHandle handle**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle handle" %}
* **MethodType fromType**,  {% include w3api/param_description.html metodo=_dato parametro="MethodType fromType" %}

## Clase Padre
[LinkerServices](/Java/LinkerServices/)

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
