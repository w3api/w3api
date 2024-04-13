---
title: DataOutput.writeByte()
permalink: /Java/DataOutput/writeByte/
date: 2021-01-11
key: Java.D.DataOutput
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataOutput.metodos valor="writeByte" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeByte(int v) throws IOException
~~~

## Parámetros
* **int v**,  {% include w3api/param_description.html metodo=_dato parametro="int v" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[DataOutput](/Java/DataOutput/)

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
