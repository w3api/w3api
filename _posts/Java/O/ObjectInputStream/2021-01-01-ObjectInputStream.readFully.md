---
title: ObjectInputStream.readFully()
permalink: /Java/ObjectInputStream/readFully/
date: 2021-01-11
key: Java.O.ObjectInputStream
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectInputStream.metodos valor="readFully" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void readFully(byte[] buf) throws IOException
public void readFully(byte[] buf, int off, int len) throws IOException
~~~

## Parámetros
* **byte[] buf**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] buf" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int off**,  {% include w3api/param_description.html metodo=_dato parametro="int off" %}

## Excepciones
[IOException](/Java/IOException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [EOFException](/Java/EOFException/), [NullPointerException](/Java/NullPointerException/)

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
