---
title: PackageDoc.findClass()
permalink: Java/PackageDoc/findClass
date: 2021-01-11
key: JavaJava.P.PackageDoc
category: java
tags: ['java se', 'com.sun.javadoc', 'jdk.javadoc', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PackageDoc.metodos valor="findClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ClassDoc findClass(String className)
~~~

## Parámetros
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Clase Padre
[PackageDoc](/Java/PackageDoc/)

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