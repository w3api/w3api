---
title: FileObject.openReader()
permalink: /Java/FileObject/openReader/
date: 2021-01-11
key: Java.F.FileObject
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileObject.metodos valor="openReader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Reader openReader(boolean ignoreEncodingErrors) throws IOException
~~~

## Parámetros
* **boolean ignoreEncodingErrors**,  {% include w3api/param_description.html metodo=_dato parametro="boolean ignoreEncodingErrors" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalStateException](/Java/IllegalStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[FileObject](/Java/FileObject/)

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
