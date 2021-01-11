---
title: VarHandle.getAndAddRelease()
permalink: Java/VarHandle/getAndAddRelease
date: 2021-01-11
key: JavaJava.V.VarHandle
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VarHandle.metodos valor="getAndAddRelease" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final Object getAndAddRelease(Object... args)
~~~

## Parámetros
* **Object... args**,  {% include w3api/param_description.html metodo=_dato parametro="Object... args" %}

## Excepciones
[WrongMethodTypeException](/Java/WrongMethodTypeException/), [ClassCastException](/Java/ClassCastException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[VarHandle](/Java/VarHandle/)

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
