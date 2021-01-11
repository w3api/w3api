---
title: URLConnection.getContent()
permalink: Java/URLConnection/getContent
date: 2021-01-11
key: JavaJava.U.URLConnection
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLConnection.metodos valor="getContent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getContent() throws IOException
public Object getContent(Class<?>[] classes) throws IOException
~~~

## Parámetros
* **Class&lt;?&gt;[] classes**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?>[] classes" %}

## Excepciones
[UnknownServiceException](/Java/UnknownServiceException/), [IOException](/Java/IOException/)

## Clase Padre
[URLConnection](/Java/URLConnection/)

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
