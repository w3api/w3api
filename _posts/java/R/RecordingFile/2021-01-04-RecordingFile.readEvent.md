---
title: RecordingFile.readEvent()
permalink: Java/RecordingFile/readEvent
date: 2021-01-04
key: JavaJava.R.RecordingFile
category: java
tags: ['java se', 'jdk.jfr.consumer', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RecordingFile.metodos valor="readEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RecordedEvent readEvent() throws IOException
~~~

## Excepciones
[EOFException](/Java/EOFException/), [IOException](/Java/IOException/)

## Clase Padre
[RecordingFile](/Java/RecordingFile/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RecordingFile.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
