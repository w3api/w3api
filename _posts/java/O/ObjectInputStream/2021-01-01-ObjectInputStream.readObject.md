---
title: ObjectInputStream.readObject()
permalink: Java/ObjectInputStream/readObject
date: 2021-01-11
key: JavaJava.O.ObjectInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectInputStream.metodos valor="readObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final Object readObject() throws IOException, ClassNotFoundException
~~~

## Excepciones
[InvalidClassException](/Java/InvalidClassException/), [OptionalDataException](/Java/OptionalDataException/), [IOException](/Java/IOException/), [StreamCorruptedException](/Java/StreamCorruptedException/), [ClassNotFoundException](/Java/ClassNotFoundException/)

## Clase Padre
[ObjectInputStream](/Java/ObjectInputStream/)

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
