---
title: DataInputStream.readUTF()
permalink: Java/DataInputStream-java-io/readUTF
date: 2021-01-04
key: JavaJava.D.DataInputStream-java-io
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataInputStream-java-io.metodos valor="readUTF" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final String readUTF() throws IOException
static String readUTF(DataInput in)
~~~

## Parámetros
* **DataInput in**,  {% include w3api/param_description.html metodo=_data parametro="DataInput in" %}

## Excepciones
[UTFDataFormatException](/Java/UTFDataFormatException/), [EOFException](/Java/EOFException/), [IOException](/Java/IOException/)

## Clase Padre
[DataInputStream](/Java/DataInputStream-java-io/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataInputStream-java-io.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
