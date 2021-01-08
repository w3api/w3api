---
title: DataHandler.writeTo()
permalink: Java/DataHandler/writeTo
date: 2021-01-04
key: JavaJava.D.DataHandler
category: java
tags: ['java se', 'javax.activation', 'java.activation', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataHandler.metodos valor="writeTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void writeTo(OutputStream os) throws IOException
~~~

## Parámetros
* **OutputStream os**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream os" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[DataHandler](/Java/DataHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
