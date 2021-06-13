---
title: MethodHandleProxies.asInterfaceInstance()
permalink: /Java/MethodHandleProxies/asInterfaceInstance/
date: 2021-01-11
key: Java.M.MethodHandleProxies
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandleProxies.metodos valor="asInterfaceInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> T asInterfaceInstance(Class<T> intfc, MethodHandle target)
~~~

## Parámetros
* **MethodHandle target**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle target" %}
* **Class&lt;T&gt; intfc**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> intfc" %}

## Clase Padre
[MethodHandleProxies](/Java/MethodHandleProxies/)

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
