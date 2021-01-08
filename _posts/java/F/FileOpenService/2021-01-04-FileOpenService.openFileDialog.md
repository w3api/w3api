---
title: FileOpenService.openFileDialog()
permalink: Java/FileOpenService/openFileDialog
date: 2021-01-04
key: JavaJava.F.FileOpenService
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileOpenService.metodos valor="openFileDialog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
FileContents openFileDialog(String pathHint, String[] extensions) throws IOException
~~~

## Parámetros
* **String pathHint**,  {% include w3api/param_description.html metodo=_data parametro="String pathHint" %}
* **String[] extensions**,  {% include w3api/param_description.html metodo=_data parametro="String[] extensions" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[FileOpenService](/Java/FileOpenService/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileOpenService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
