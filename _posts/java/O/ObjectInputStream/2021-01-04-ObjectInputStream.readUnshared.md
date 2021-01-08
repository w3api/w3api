---
title: ObjectInputStream.readUnshared()
permalink: Java/ObjectInputStream/readUnshared
date: 2021-01-04
key: JavaJava.O.ObjectInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectInputStream.metodos valor="readUnshared" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object readUnshared() throws IOException, ClassNotFoundException
~~~

## Excepciones
[OptionalDataException](/Java/OptionalDataException/), [ObjectStreamException](/Java/ObjectStreamException/), [ClassNotFoundException](/Java/ClassNotFoundException/), [StreamCorruptedException](/Java/StreamCorruptedException/), [IOException](/Java/IOException/)

## Clase Padre
[ObjectInputStream](/Java/ObjectInputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
