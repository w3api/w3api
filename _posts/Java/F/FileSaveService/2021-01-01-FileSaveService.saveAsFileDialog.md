---
title: FileSaveService.saveAsFileDialog()
permalink: /Java/FileSaveService/saveAsFileDialog/
date: 2021-01-11
key: Java.F.FileSaveService
category: Java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSaveService.metodos valor="saveAsFileDialog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
FileContents saveAsFileDialog(String pathHint, String[] extensions, FileContents contents) throws IOException
~~~

## Parámetros
* **FileContents contents**,  {% include w3api/param_description.html metodo=_dato parametro="FileContents contents" %}
* **String[] extensions**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extensions" %}
* **String pathHint**,  {% include w3api/param_description.html metodo=_dato parametro="String pathHint" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[FileSaveService](/Java/FileSaveService/)

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
