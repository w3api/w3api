---
title: DataOutput.writeUTF()
permalink: /Java/DataOutput/writeUTF/
date: 2021-01-11
key: Java.D.DataOutput
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataOutput.metodos valor="writeUTF" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeUTF(String s) throws IOException
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}

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
