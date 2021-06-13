---
title: RecordingFile.readAllEvents()
permalink: /Java/RecordingFile/readAllEvents/
date: 2021-01-11
key: Java.R.RecordingFile
category: Java
tags: ['java se', 'jdk.jfr.consumer', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RecordingFile.metodos valor="readAllEvents" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static List<RecordedEvent> readAllEvents(Path path) throws IOException
~~~

## Parámetros
* **Path path**,  {% include w3api/param_description.html metodo=_dato parametro="Path path" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

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
