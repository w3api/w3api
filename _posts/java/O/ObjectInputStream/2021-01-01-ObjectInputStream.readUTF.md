---
title: ObjectInputStream.readUTF()
permalink: Java/ObjectInputStream/readUTF
date: 2021-01-11
key: JavaJava.O.ObjectInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectInputStream.metodos valor="readUTF" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String readUTF() throws IOException
~~~

## Excepciones
[UTFDataFormatException](/Java/UTFDataFormatException/), [IOException](/Java/IOException/)

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
