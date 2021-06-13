---
title: ConstantCallSite.ConstantCallSite()
permalink: /Java/ConstantCallSite/ConstantCallSite/
date: 2021-01-11
key: Java.C.ConstantCallSite
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConstantCallSite.constructores valor="ConstantCallSite" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ConstantCallSite(MethodHandle target)
protected ConstantCallSite(MethodType targetType, MethodHandle createTargetHook) throws Throwable
~~~

## Parámetros
* **MethodHandle createTargetHook**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle createTargetHook" %}
* **MethodHandle target**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle target" %}
* **MethodType targetType**,  {% include w3api/param_description.html metodo=_dato parametro="MethodType targetType" %}

## Excepciones
[WrongMethodTypeException](/Java/WrongMethodTypeException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConstantCallSite](/Java/ConstantCallSite/)

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
