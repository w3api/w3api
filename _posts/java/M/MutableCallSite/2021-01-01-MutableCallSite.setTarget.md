---
title: MutableCallSite.setTarget()
permalink: Java/MutableCallSite/setTarget
date: 2021-01-11
key: JavaJava.M.MutableCallSite
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MutableCallSite.metodos valor="setTarget" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setTarget(MethodHandle newTarget)
~~~

## Parámetros
* **MethodHandle newTarget**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle newTarget" %}

## Excepciones
[WrongMethodTypeException](/Java/WrongMethodTypeException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MutableCallSite](/Java/MutableCallSite/)

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
