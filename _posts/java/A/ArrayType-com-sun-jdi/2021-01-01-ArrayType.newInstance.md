---
title: ArrayType.newInstance()
permalink: Java/ArrayType-com-sun-jdi/newInstance
date: 2021-01-11
key: JavaJava.A.ArrayType-com-sun-jdi
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ArrayType-com-sun-jdi.metodos valor="newInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ArrayReference newInstance(int length)
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}

## Excepciones
[VMCannotBeModifiedException](/Java/VMCannotBeModifiedException/)

## Clase Padre
[ArrayType](/Java/ArrayType-com-sun-jdi/)

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
