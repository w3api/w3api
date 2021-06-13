---
title: ObjectInputStream.skipBytes()
permalink: /Java/ObjectInputStream/skipBytes/
date: 2021-01-11
key: Java.O.ObjectInputStream
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectInputStream.metodos valor="skipBytes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int skipBytes(int len) throws IOException
~~~

## Parámetros
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}

## Excepciones
[IOException](/Java/IOException/)

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
