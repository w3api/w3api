---
title: JavaFileManager.getFileForOutput()
permalink: /Java/JavaFileManager/getFileForOutput/
date: 2021-01-11
key: Java.J.JavaFileManager
category: Java
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
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileManager.Location location" %}
* **FileObject sibling**,  {% include w3api/param_description.html metodo=_dato parametro="FileObject sibling" %}
* **String packageName**,  {% include w3api/param_description.html metodo=_dato parametro="String packageName" %}
* **String relativeName**,  {% include w3api/param_description.html metodo=_dato parametro="String relativeName" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

## Clase Padre
[JavaFileManager](/Java/JavaFileManager/)

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
