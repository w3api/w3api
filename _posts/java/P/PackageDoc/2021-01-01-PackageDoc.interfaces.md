---
title: PackageDoc.interfaces()
permalink: /Java/PackageDoc/interfaces/
date: 2021-01-11
key: Java.P.PackageDoc
category: Java
tags: ['java se', 'com.sun.javadoc', 'jdk.javadoc', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PackageDoc.metodos valor="interfaces" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ClassDoc[] interfaces()
~~~

## Clase Padre
[PackageDoc](/Java/PackageDoc/)

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
