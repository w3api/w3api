---
title: LocalVariable.type()
permalink: /Java/LocalVariable/type/
date: 2021-01-11
key: Java.L.LocalVariable
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalVariable.metodos valor="type" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Type type() throws ClassNotLoadedException
~~~

## Excepciones
[ClassNotLoadedException](/Java/ClassNotLoadedException/)

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
