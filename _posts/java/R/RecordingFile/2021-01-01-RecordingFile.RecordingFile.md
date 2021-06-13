---
title: RecordingFile.RecordingFile()
permalink: Java/RecordingFile/RecordingFile
date: 2021-01-11
key: Java.R.RecordingFile
category: java
tags: ['java se', 'jdk.jfr.consumer', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RecordingFile.constructores valor="RecordingFile" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RecordingFile(Path file) throws IOException
~~~

## Parámetros
* **Path file**,  {% include w3api/param_description.html metodo=_dato parametro="Path file" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NoSuchFileException](/Java/NoSuchFileException/), [IOException](/Java/IOException/)

## Clase Padre
[RecordingFile](/Java/RecordingFile/)

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
