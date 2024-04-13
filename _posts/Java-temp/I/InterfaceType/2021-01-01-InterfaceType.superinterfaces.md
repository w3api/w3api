---
title: InterfaceType.superinterfaces()
permalink: /Java/InterfaceType/superinterfaces/
date: 2021-01-11
key: Java.I.InterfaceType
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InterfaceType.metodos valor="superinterfaces" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
List<InterfaceType> superinterfaces()
~~~

## Excepciones
[ClassNotPreparedException](/Java/ClassNotPreparedException/)

## Clase Padre
[InterfaceType](/Java/InterfaceType/)

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
