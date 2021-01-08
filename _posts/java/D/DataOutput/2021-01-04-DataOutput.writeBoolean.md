---
title: DataOutput.writeBoolean()
permalink: Java/DataOutput/writeBoolean
date: 2021-01-04
key: JavaJava.D.DataOutput
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataOutput.metodos valor="writeBoolean" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeBoolean(boolean v) throws IOException
~~~

## Parámetros
* **boolean v**,  {% include w3api/param_description.html metodo=_data parametro="boolean v" %}

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
{%- for _ldc in site.data.Java.D.DataOutput.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
