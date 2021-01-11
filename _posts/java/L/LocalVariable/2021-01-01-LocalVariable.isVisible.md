---
title: LocalVariable.isVisible()
permalink: Java/LocalVariable/isVisible
date: 2021-01-11
key: JavaJava.L.LocalVariable
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalVariable.metodos valor="isVisible" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean isVisible(StackFrame frame)
~~~

## Parámetros
* **StackFrame frame**,  {% include w3api/param_description.html metodo=_dato parametro="StackFrame frame" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[LocalVariable](/Java/LocalVariable/)

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
