---
title: ClassType.interfaces()
permalink: /Java/ClassType/interfaces/
date: 2021-01-11
key: Java.C.ClassType
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassType.metodos valor="interfaces" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
List<InterfaceType> interfaces()
~~~

## Excepciones
[ClassNotPreparedException](/Java/ClassNotPreparedException/)

## Clase Padre
[ClassType](/Java/ClassType/)

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
