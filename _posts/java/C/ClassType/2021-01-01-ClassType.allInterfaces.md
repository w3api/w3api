---
title: ClassType.allInterfaces()
permalink: /Java/ClassType/allInterfaces/
date: 2021-01-11
key: Java.C.ClassType
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassType.metodos valor="allInterfaces" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
List<InterfaceType> allInterfaces()
~~~

## Excepciones
[ClassNotPreparedException](/Java/ClassNotPreparedException/)

## Clase Padre
[ClassType](/Java/ClassType/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
