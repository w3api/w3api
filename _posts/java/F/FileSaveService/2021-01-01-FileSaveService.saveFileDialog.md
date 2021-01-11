---
title: FileSaveService.saveFileDialog()
permalink: Java/FileSaveService/saveFileDialog
date: 2021-01-11
key: JavaJava.F.FileSaveService
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSaveService.metodos valor="saveFileDialog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
FileContents saveFileDialog(String pathHint, String[] extensions, InputStream stream, String name) throws IOException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String[] extensions**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extensions" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream stream" %}
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
