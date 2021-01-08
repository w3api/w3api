---
title: JavaFileManager.getFileForOutput()
permalink: Java/JavaFileManager/getFileForOutput
date: 2021-01-04
key: JavaJava.J.JavaFileManager
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaFileManager.metodos valor="getFileForOutput" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
FileObject getFileForOutput(JavaFileManager.Location location, String packageName, String relativeName, FileObject sibling) throws IOException
~~~

## Parámetros
* **FileObject sibling**,  {% include w3api/param_description.html metodo=_data parametro="FileObject sibling" %}
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_data parametro="JavaFileManager.Location location" %}
* **String relativeName**,  {% include w3api/param_description.html metodo=_data parametro="String relativeName" %}
* **String packageName**,  {% include w3api/param_description.html metodo=_data parametro="String packageName" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JavaFileManager](/Java/JavaFileManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JavaFileManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
