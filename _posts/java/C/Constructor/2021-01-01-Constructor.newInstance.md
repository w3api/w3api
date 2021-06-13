---
title: Constructor.newInstance()
permalink: /Java/Constructor/newInstance/
date: 2021-01-11
key: Java.C.Constructor
category: Java
tags: ['java se', 'java.lang.reflect', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Constructor.metodos valor="newInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public T newInstance(Object... initargs) throws InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException
~~~

## Parámetros
* **Object... initargs**,  {% include w3api/param_description.html metodo=_dato parametro="Object... initargs" %}

## Excepciones
[ExceptionInInitializerError](/Java/ExceptionInInitializerError/), [IllegalArgumentException](/Java/IllegalArgumentException/), [InvocationTargetException](/Java/InvocationTargetException/), [IllegalAccessException](/Java/IllegalAccessException/), [InstantiationException](/Java/InstantiationException/)

## Clase Padre
[Constructor](/Java/Constructor/)

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
