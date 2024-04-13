---
title: MethodHandles.varHandleInvoker()
permalink: /Java/MethodHandles/varHandleInvoker/
date: 2021-01-11
key: Java.M.MethodHandles
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandles.metodos valor="varHandleInvoker" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MethodHandle varHandleInvoker(VarHandle.AccessMode accessMode, MethodType type)
~~~

## Parámetros
* **VarHandle.AccessMode accessMode**,  {% include w3api/param_description.html metodo=_dato parametro="VarHandle.AccessMode accessMode" %}
* **MethodType type**,  {% include w3api/param_description.html metodo=_dato parametro="MethodType type" %}

## Clase Padre
[MethodHandles](/Java/MethodHandles/)

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
