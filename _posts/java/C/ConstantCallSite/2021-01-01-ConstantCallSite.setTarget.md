---
title: ConstantCallSite.setTarget()
permalink: /Java/ConstantCallSite/setTarget/
date: 2021-01-11
key: Java.C.ConstantCallSite
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConstantCallSite.metodos valor="setTarget" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setTarget(MethodHandle ignore)
~~~

## Parámetros
* **MethodHandle ignore**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle ignore" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
