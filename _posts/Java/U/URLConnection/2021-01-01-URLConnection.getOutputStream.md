---
title: URLConnection.getOutputStream()
permalink: /Java/URLConnection/getOutputStream/
date: 2021-01-11
key: Java.U.URLConnection
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLConnection.metodos valor="getOutputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public OutputStream getOutputStream() throws IOException
~~~

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
