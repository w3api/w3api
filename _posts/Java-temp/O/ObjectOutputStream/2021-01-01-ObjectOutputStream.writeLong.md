---
title: ObjectOutputStream.writeLong()
permalink: /Java/ObjectOutputStream/writeLong/
date: 2021-01-11
key: Java.O.ObjectOutputStream
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectOutputStream.metodos valor="writeLong" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void writeLong(long val) throws IOException
~~~

## Parámetros
* **long val**,  {% include w3api/param_description.html metodo=_dato parametro="long val" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[ObjectOutputStream](/Java/ObjectOutputStream/)

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
