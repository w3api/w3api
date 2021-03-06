---
title: MethodDescriptor.MethodDescriptor()
permalink: /Java/MethodDescriptor/MethodDescriptor/
date: 2021-01-11
key: Java.M.MethodDescriptor
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodDescriptor.constructores valor="MethodDescriptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MethodDescriptor(Method method)
public MethodDescriptor(Method method, ParameterDescriptor[] parameterDescriptors)
~~~

## Parámetros
* **Method method**,  {% include w3api/param_description.html metodo=_dato parametro="Method method" %}
* **ParameterDescriptor[] parameterDescriptors**,  {% include w3api/param_description.html metodo=_dato parametro="ParameterDescriptor[] parameterDescriptors" %}

## Clase Padre
[MethodDescriptor](/Java/MethodDescriptor/)

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
