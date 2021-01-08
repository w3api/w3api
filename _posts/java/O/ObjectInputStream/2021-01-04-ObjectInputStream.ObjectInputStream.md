---
title: ObjectInputStream.ObjectInputStream()
permalink: Java/ObjectInputStream/ObjectInputStream
date: 2021-01-04
key: JavaJava.O.ObjectInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectInputStream.constructores valor="ObjectInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected ObjectInputStream() throws IOException, SecurityException
public ObjectInputStream(InputStream in) throws IOException
~~~

## Parámetros
* **InputStream in**,  {% include w3api/param_description.html metodo=_data parametro="InputStream in" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/), [StreamCorruptedException](/Java/StreamCorruptedException/), [IOException](/Java/IOException/)

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
