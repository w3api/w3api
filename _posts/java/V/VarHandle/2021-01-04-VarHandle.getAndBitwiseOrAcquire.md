---
title: VarHandle.getAndBitwiseOrAcquire()
permalink: Java/VarHandle/getAndBitwiseOrAcquire
date: 2021-01-04
key: JavaJava.V.VarHandle
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VarHandle.metodos valor="getAndBitwiseOrAcquire" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final Object getAndBitwiseOrAcquire(Object... args)
~~~

## Parámetros
* **Object... args**,  {% include w3api/param_description.html metodo=_data parametro="Object... args" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [ClassCastException](/Java/ClassCastException/), [WrongMethodTypeException](/Java/WrongMethodTypeException/)

## Clase Padre
[VarHandle](/Java/VarHandle/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.V.VarHandle.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
