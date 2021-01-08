---
title: DataContentHandler.writeTo()
permalink: Java/DataContentHandler/writeTo
date: 2021-01-04
key: JavaJava.D.DataContentHandler
category: java
tags: ['java se', 'javax.activation', 'java.activation', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataContentHandler.metodos valor="writeTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeTo(Object obj, String mimeType, OutputStream os) throws IOException
~~~

## Parámetros
* **String mimeType**,  {% include w3api/param_description.html metodo=_data parametro="String mimeType" %}
* **OutputStream os**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream os" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_data parametro="Object obj" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[DataContentHandler](/Java/DataContentHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataContentHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
