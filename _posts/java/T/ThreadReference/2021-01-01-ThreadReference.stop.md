---
title: ThreadReference.stop()
permalink: /Java/ThreadReference/stop/
date: 2021-01-11
key: Java.T.ThreadReference
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadReference.metodos valor="stop" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void stop(ObjectReference throwable) throws InvalidTypeException
~~~

## Parámetros
* **ObjectReference throwable**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectReference throwable" %}

## Excepciones
[VMCannotBeModifiedException](/Java/VMCannotBeModifiedException/), [InvalidTypeException](/Java/InvalidTypeException/)

## Clase Padre
[ThreadReference](/Java/ThreadReference/)

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
