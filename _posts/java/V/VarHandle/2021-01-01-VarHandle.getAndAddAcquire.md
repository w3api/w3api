---
title: VarHandle.getAndAddAcquire()
permalink: /Java/VarHandle/getAndAddAcquire/
date: 2021-01-11
key: Java.V.VarHandle
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VarHandle.metodos valor="getAndAddAcquire" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final Object getAndAddAcquire(Object... args)
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
