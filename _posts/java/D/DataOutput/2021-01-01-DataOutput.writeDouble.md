---
title: DataOutput.writeDouble()
permalink: Java/DataOutput/writeDouble
date: 2021-01-11
key: JavaJava.D.DataOutput
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataOutput.metodos valor="writeDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeDouble(double v) throws IOException
~~~

## Parámetros
* **double v**,  {% include w3api/param_description.html metodo=_dato parametro="double v" %}

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
