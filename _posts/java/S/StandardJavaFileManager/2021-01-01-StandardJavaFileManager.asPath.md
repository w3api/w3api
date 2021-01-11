---
title: StandardJavaFileManager.asPath()
permalink: Java/StandardJavaFileManager/asPath
date: 2021-01-11
key: JavaJava.S.StandardJavaFileManager
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardJavaFileManager.metodos valor="asPath" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default Path asPath(FileObject file)
~~~

## Parámetros
* **FileObject file**,  {% include w3api/param_description.html metodo=_dato parametro="FileObject file" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[StandardJavaFileManager](/Java/StandardJavaFileManager/)

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
