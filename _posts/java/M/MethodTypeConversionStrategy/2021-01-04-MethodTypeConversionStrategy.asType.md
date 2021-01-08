---
title: MethodTypeConversionStrategy.asType()
permalink: Java/MethodTypeConversionStrategy/asType
date: 2021-01-04
key: JavaJava.M.MethodTypeConversionStrategy
category: java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodTypeConversionStrategy.metodos valor="asType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
MethodHandle asType(MethodHandle target, MethodType newType)
~~~

## Parámetros
* **MethodType newType**,  {% include w3api/param_description.html metodo=_data parametro="MethodType newType" %}
* **MethodHandle target**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle target" %}

## Clase Padre
[MethodTypeConversionStrategy](/Java/MethodTypeConversionStrategy/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodTypeConversionStrategy.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
