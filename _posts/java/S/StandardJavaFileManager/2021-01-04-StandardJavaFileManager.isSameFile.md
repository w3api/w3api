---
title: StandardJavaFileManager.isSameFile()
permalink: Java/StandardJavaFileManager/isSameFile
date: 2021-01-04
key: JavaJava.S.StandardJavaFileManager
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardJavaFileManager.metodos valor="isSameFile" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean isSameFile(FileObject a, FileObject b)
~~~

## Parámetros
* **FileObject b**,  {% include w3api/param_description.html metodo=_data parametro="FileObject b" %}
* **FileObject a**,  {% include w3api/param_description.html metodo=_data parametro="FileObject a" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[StandardJavaFileManager](/Java/StandardJavaFileManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StandardJavaFileManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
