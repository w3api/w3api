---
title: FileSystemException.FileSystemException()
permalink: Java/FileSystemException/FileSystemException
date: 2021-01-04
key: JavaJava.F.FileSystemException
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystemException.constructores valor="FileSystemException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FileSystemException(String file)
public FileSystemException(String file, String other, String reason)
~~~

## Parámetros
* **String file**,  {% include w3api/param_description.html metodo=_data parametro="String file" %}
* **String other**,  {% include w3api/param_description.html metodo=_data parametro="String other" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}

## Clase Padre
[FileSystemException](/Java/FileSystemException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileSystemException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
